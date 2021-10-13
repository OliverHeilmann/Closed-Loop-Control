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
refConst = True

################################################################

# Main script below
if __name__ == "__main__":
    # y (output) is 0 at time T0
    y = 0

    storeX=[]; storeY=[]; storeRef=[]; storeYInf=[]
    for i in range(0,100): # change this to while y ~ yInf ... perhaps 5% off? Have break condition if not met e.g. after 1000 loops...        
        # + or - a value from reference value if refConst == False only
        if not refConst:
            reference = reference + (random.random()*random.randint(-1, 1))
        
        # With no time delay, what should yInf be now...
        # Note that when refConst is set to True, yInf is a constant
        yInf = (controller_gain * plant_gain * reference) / (1 + controller_gain * plant_gain * sensor_gain)

        # If the remainder of current time step 'i' / plant time delay == 0 then the
        # signal has had sufficient time to be fed back to the start i.e. recalculate
        # error and y...
        if timeDelay > 0:
            if i % int(timeDelay) == 0:
                error = reference - y
        else: error = reference - yInf
        y = error * controller_gain * plant_gain

        storeX.append(i)
        storeY.append(y)
        storeRef.append(reference)
        storeYInf.append(yInf)

    # Collect all the values (to be displayed...)
    if not refConst:
        reference = 'varied'
    values = '\nref: {} | Cgain: {} | pGain: {} | sGain: {} | tDelay: {}'.format(reference,
                                                                                controller_gain,
                                                                                plant_gain,
                                                                                sensor_gain,
                                                                                timeDelay)

    # Plot and label the graph
    plt.title(values)
    plt.plot(storeX, storeY, '-')
    plt.plot(storeX, storeRef)
    plt.plot(storeX, storeYInf) # np.ones(i+1)*yInf, '--')
    plt.ylabel('y')
    plt.legend(['y', 'ref', 'yInf'])
    plt.xlabel('Time Step (T)')
    plt.show()