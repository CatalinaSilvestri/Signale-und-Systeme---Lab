import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate, correlation_lags 
# from scipy import signal

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


def genFreqDomain(x, sr):
    """
    2. Im folgenden sollen Sie eine Funktion erzeugen, die das Signal "x" mit Hilfe der als ebenfalls als Funktionsparameter
    übergebenen Samplerate "sr" in den Frequenzbereich konvertiert. Nutzen Sie hierzu die Teilbibliothek "fft" der Numpy-Bibliothek,
    dort finde Sie alle notwendigen Funktionen. Die Funktion soll die Variablen "fSamples" und "freqs" zurückliefern, wobei
    fSamples das in den Frequenzbereich übertragene Signal als Betrag der Fouriertransformierten und freqs die Frequenzachse darstellt.
    Bitte beachten Sie, dass fSamples für ein gut lesbares Spektrum auf die Länge des Vektors fSamples normiert werden muss. 
    """
    fSamples = np.fft.fft(x) # y axis = |X(jw)|
    n = fSamples.size
    fSamples = np.abs(np.fft.fftshift(fSamples))/n
    
    freqs = np.fft.fftfreq(n, 1/sr) # f axis (omega values)
    freqs = np.fft.fftshift(freqs)


    return fSamples, freqs


def runTask(sr, length, cos_amplitude, cos_frequency, cos_phase, cos_time_behavior, tau):

    x_axis_time = createTimeAxis(sr, length)
    y_axis_comp_cos = createComplexWaves(x_axis_time, cos_amplitude, cos_time_behavior, cos_frequency, cos_phase, tau)[0]

    # Spectrum generation
    x_axis_f = genFreqDomain(x_axis_time, sr)[1] 
    y_axis_f = genFreqDomain(y_axis_comp_cos, sr)[0]
    
    # Plotting
    plt.figure()
    plt.plot(x_axis_time, y_axis_comp_cos, linestyle='-', color='y') #comp cos in t, potentially shifted

    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.legend(["Cos in t"])

    # Second plot   
    
    plt.figure()
    plt.plot(x_axis_f, np.abs(y_axis_f), linestyle='-', color='r') # comp cos in f (Spectrum)
    plt.xlabel("frequency")
    plt.ylabel("|X(jw)|")
    plt.legend(["Cos in f"])




if __name__ == "__main__":
    """
    Example values
    """
    sr =  100
    length = 2
    cos_amplitude = 1
    cos_phase = 0
    cos_frequency = 10
    cos_time_behavior = 0
    tau = 0.25

    runTask(sr, length, cos_amplitude, cos_frequency, cos_phase, cos_time_behavior, tau)
    plt.show()
    
    """
    HINWEISE: 
            1. Bitte beachten Sie, dass Sie ein Amplitudenspektrum mit negativen und positiven Frequenzen,
            wie dem SU zu entnehmen, erwarten. Dies bedeutet, dass Sie ebenfalls einen sog. fftshift vornehmen müssen, 
            um das Spektrum richtig darzustellen.
    """