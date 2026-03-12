import numpy as np
import matplotlib.pyplot as plt

def createTimeAxis(sr,length):
    ar = np.linspace(0, length-(1/sr), sr*length, endpoint=True)
    return ar
    

def createCos(t, A, f, phi, tau=0):

    cos_t = A*np.cos(2*np.pi*f*(t-tau)+phi)

    return cos_t #output is scalar array


def createComplexWaves(t, C, r, f, phi, tau=0):

    x_t = np.abs(C) * np.exp((r+1j*2*np.pi*f)*(t-tau)+1j*phi)

    comp_cos_t = np.real(x_t)

    comp_sin_t = np.imag(x_t)

    return comp_cos_t, comp_sin_t

def runTask(sr, length, cos_amplitude, cos_frequency, cos_phase, cos_time_behavior, tau=0):
  
    # Fixed cos
    x_axis_fixed = createTimeAxis(sr,length)
    
    # Complex cos unshifted
    y_axis_comp_cos = createComplexWaves(x_axis_fixed, cos_amplitude, cos_time_behavior, cos_frequency, cos_phase)[0]

    # Complex cos shifted
    y_axis_comp_cos_shift = createComplexWaves(x_axis_fixed, cos_amplitude, cos_time_behavior, cos_frequency, cos_phase, tau)[0] 

    # Complex sin unshifted
    y_axis_comp_sin = createComplexWaves(x_axis_fixed, cos_amplitude, cos_time_behavior, cos_frequency, cos_phase)[1]

    # Complex sin shifted
    y_axis_comp_sin_shift = createComplexWaves(x_axis_fixed, cos_amplitude, cos_time_behavior, cos_frequency, cos_phase, tau)[1]


    # output 
    plt.plot(x_axis_fixed, y_axis_comp_cos, linestyle='--', color='y') #comp cos
    plt.plot(x_axis_fixed, y_axis_comp_cos_shift, linestyle='-', color='b')

    plt.plot(x_axis_fixed, y_axis_comp_sin, linestyle='--',color='g') #comp sin
    plt.plot(x_axis_fixed, y_axis_comp_sin_shift, linestyle='-', color='r')

    plt.legend(["Complex Cos", "Complex Cos shifted", "Complex Sine", "Complex Sine shifted"])
    


if __name__ == "__main__":
    """
    Example values
    """
    sr = 100
    length = 1
    cos_amplitude = 1
    cos_phase = 0
    cos_frequency = 1
    cos_time_behavior = 0
    tau = 0.25

    runTask(sr, length, cos_amplitude, cos_frequency, cos_phase, cos_time_behavior, tau)
    plt.show()
