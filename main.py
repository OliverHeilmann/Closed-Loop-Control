# Created by Oliver Heilmann
# Date Created: 11/10/2021

from time import time
import matplotlib.pyplot as plt
import numpy as np
import random
import pdb

# Try changing the below parameters to see how the output plot changes...

reference = 1
controller_gain = 0.5
plant_gain = 1
sensor_gain = 1
timeDelay = 5

# Keep reference constant?
refConst = False

################################################################

y = 0
ymax = (controller_gain * plant_gain * reference) / (1 + controller_gain * plant_gain * sensor_gain)

storeX=[]; storeY=[]; storeRef=[]
for i in range(0,100): # change this to while y ~ ymax ... perhaps 5% off? Have break condition if not met e.g. after 1000 loops...
    if not refConst:
        reference = reference + (random.random()*random.randint(-1, 1))
    
    if i % int(timeDelay) == 0:
        error = reference - y
        y = error * controller_gain * plant_gain

    storeX.append(i)
    storeY.append(y)
    storeRef.append(reference)

# Collect all the values (to be displayed...)
if not refConst:
    reference = 'varied'

values = '\nref: {} | Cgain: {} | pGain: {} | sGain: {} | tDelay: {}'.format(reference,
                                                                            controller_gain,
                                                                            plant_gain,
                                                                            sensor_gain,
                                                                            timeDelay)

plt.title(values)
plt.plot(storeX, storeY, '-')
plt.plot(storeX, storeRef)
if refConst:
    plt.plot(storeX, np.ones(i+1)*ymax, '--')
    plt.ylabel('y'.format(round(ymax,2)))
    plt.legend(['y', 'ref', 'ymax'])

else:
    plt.ylabel('y')
    plt.legend(['y', 'ref'])

plt.xlabel('Time Step (T)')
plt.show()