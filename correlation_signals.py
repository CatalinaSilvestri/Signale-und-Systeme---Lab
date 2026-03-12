import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate, correlation_lags 


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

def corrSignals(x, y):
    """
    2. Im folgenden sollen Sie eine Funktion erzeugen, die die Korrelationfunktion der beiden Signale x und y
    berechnet. Dieses ermöglicht Ihnen in weiteren Schritten die Darstellung der Korrelation als plot, wie aus dem SU bekannt. Ebenfalls sollen
    Sie mithilfe einschlägiger Funktionen den zeitlichen Versatz zwischen den Signalen x und y direkt bestimmen.
    Benutzen sie hierfür die folgenden Funktionen der scipy.signal bibliothek: correlate und correlation_lags.
    Korrelieren Sie zuerst die beiden Signale x und y und speichern Sie das entstehende Array der Korrelation in einer Variable correlation.

    """
    
    correlation = correlate(x, y, mode="full")
    lags = correlation_lags(x.size, y.size, mode="full")
    lag = lags[np.argmax(correlation)]

    return lag, lags, correlation

def runTask(sr, length, cos_amplitude, cos_frequency, cos_phase, cos_time_behavior, tau):

    x_axis_fixed = createTimeAxis(sr, length)

    # Complex cos unshifted
    y_axis_comp_cos = createComplexWaves(x_axis_fixed, cos_amplitude, cos_time_behavior, cos_frequency, cos_phase)[0]

    # Complex cos shifted
    y_axis_comp_cos_shift = createComplexWaves(x_axis_fixed, cos_amplitude, cos_time_behavior, cos_frequency, cos_phase, tau)[0] 

    # Plotting cos Signals
    plt.figure()
    plt.plot(x_axis_fixed, y_axis_comp_cos, linestyle='-', color='y') # comp cos
    plt.plot(x_axis_fixed, y_axis_comp_cos_shift, linestyle='-', color='b') # comp cos shifted

    # Correlation
    correlation_info = corrSignals(y_axis_comp_cos, y_axis_comp_cos_shift)

    # Second plot -> correlation
    plt.figure()
    plt.plot(correlation_info[1], correlation_info[2], linestyle='--', color='r')




if __name__ == "__main__":
    """
    Example values
    """
    sr = 100
    length = 2
    cos_amplitude = 1
    cos_phase = 0
    cos_frequency = 1
    cos_time_behavior = 0
    tau = 0.25

    runTask(sr, length, cos_amplitude, cos_frequency, cos_phase, cos_time_behavior, tau)
    plt.show()
    
    """
    HINWEISE: 
            1. Bitte bedenken Sie, das Sie hier mit zeitdiskreten (=digitalen) Signalen arbeiten. 
            Die Variable "lag" liefert ihnen somit bei korrekter Anwendung keinen "Zeitwert" der Verschiebung zurück,
            sondern einen Anzahl an Samples, um die Y zu X verschoben ist. Diese Anzahl von Samples können Sie einfach
            in eine Zeitverschiebung zurückrechnen indem Sie sie durch die samplerate teilen (tau = lag/sr). 
    """