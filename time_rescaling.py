import numpy as np
import matplotlib.pyplot as plt

def createTimeAxis(sr,length):
    ar = np.linspace(0, length-(1/sr), sr*length, endpoint=True)
    return ar
    
def createCos(t, A, f, phi):
    cos_t = A*np.cos(2*np.pi*f*t+phi)

    return cos_t #output is scalar array

def rescaleTimeAxis(t, alpha):
    if(alpha == 0):
        return t
    return t*alpha

def runTask(sr, length, cos_amplitude, cos_frequency, cos_phase, alpha):
    
    # Fixed cos
    x_axis_fixed = createTimeAxis(sr,length)
    y_axis_fixed = createCos(x_axis_fixed, cos_amplitude, cos_frequency, cos_phase)
    plt.xlabel("time")
    plt.ylabel("amplitude")

    # Rescaled cos 
    x_axis_rescaled = rescaleTimeAxis(x_axis_fixed, alpha)


    # output area
    plt.plot(x_axis_fixed, y_axis_fixed, color='r') #fixed cosinus output
    plt.plot(x_axis_rescaled, y_axis_fixed, color='y') #rescaled cosinus output



if __name__ == "__main__":
    """
    Example values
    """
    sr = 100
    length = 1
    cos_amplitude = 1
    cos_phase = 0
    cos_frequency = 1
    alpha = 0.25

    runTask(sr, length, cos_amplitude, cos_frequency, cos_phase, alpha)
    plt.show()
    