import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate, correlation_lags 
from scipy import signal


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

    correlation = correlate(x, y, mode="full")
    lags = correlation_lags(x.size, y.size, mode="full")
    lag = lags[np.argmax(correlation)]

    return lag, lags, correlation

def genFreqDomain(x, sr):

    fSamples = np.fft.fft(x) # y axis = |X(jw)|
    n = fSamples.size
    fSamples = np.abs(np.fft.fftshift(fSamples))/n # sample array normalized
    
    freqs = np.fft.fftfreq(n, 1/sr) # f axis (omega values)
    freqs = np.fft.fftshift(freqs)


    return fSamples, freqs


def createIR_RC(t, R, C):
    """
    2. Erzeugen Sie nun eine Funktion, welche auf Basis der Parameter "R" und "C" eine Impulsantwort
    über den Zeitraum "t" erzeugt. Die zu erzeugende Impulsantwort generiert sich aus der Modellbildung
    für ein sog. RC-Glied, welches in der analogen Umsetzung einem Tiefpassfilter 1.Ordnung entspricht.
    Die Werte für R und C entsprechen hierbei dem Widerstand (in Ohm) des verwendeten Widerstandes und der Kapazität 
    (in Farad) des verwendeten Kondensators. Die analytische Gleichung der Impulsantwort und eine Schematik des 
    Systems finden Sie in den SU-Unterlagen unter "Beispiel zeitkontinuierliche Systeme". Bitte implentieren Sie diese!
    Die Funktion soll eine Variable "hRC_t" zurückliefern, welche die Impulsantwort darstellt. Hierbei soll die 
    Variable hRC_t auf 1/RC normiert werden, sodass die Maximale Amplitude der Impulsantwort = 1 gesetzt wird. 

    Hinweis: Gehen Sie davon aus, dass nur positive zeitliche Räume betrachtet werden, sprich t > 0. 
    Dieses ist insbesondere für den einfachen Umgang mit der Sprungfunktion in der Gleichung interessant!
    """
    tau = R*C
    hRC_t = (1/tau) * np.exp((-t/tau))
    hRC_t *= tau 
    return hRC_t # arraylike output


def createRect(t, f, Ti, Tp, phi):
    """
    3. Weiterhin soll eine Funktion erzeugt werden, mithilfe derer ein parametrisierbares Rechtecksignal über die
    Zeit "t" erzeugt werden kann. Die Parameter "f" und "phi" sind analog vorherer Betrachtungen, während "Ti" und "Tp"
    analog zum SU in Kombination das Tastverhältnis (-> Duty cycle, Ti/Tp, "Einschaltdauer"/Gesamtperiodendauer) widerspiegeln.
    Erzeugen Sie mithilfe der scipy.signal.square() Funktion ein parametrisierbares Rechtecksignal!
    Die Funktion soll eine Variable "rect" zurückliefern, welche das Rechtecksignal enthält.
    Das Rechecktsignal soll zusätzlich auf den Wertebereich der Amplitude auf [0,1] begrenzt werden. Nutzen Sie hierzu die Funktion
    np.clip().
    """
    duty = Ti/Tp
    rect = signal.square((f * 2 * np.pi * t + phi), duty=duty) # 
    rect = np.clip(rect, 0, 1)

    return rect


def runTask(sr, length, f, phi, Ti, Tp, R, C):
    """
    4. Überlegen Sie sich eine neue Routine, in der Sie sowohl das Rechecktsignal als auch die Impulsantwort
    darstellen und die Korrektheit der Funktionen überprüfen können.
    """
    x_axis = createTimeAxis(sr,length)
    y_axis_square = createRect(x_axis, f, Ti, Tp, phi)
    y_axis_h = createIR_RC(x_axis, R, C) # impulse response

    # output 
    plt.plot(x_axis, y_axis_square, color='r') # Rechteckssignal
    plt.plot(x_axis, y_axis_h, color='y') # Impulsantwort
    plt.legend(["Rechteckssignal", "Impulsantwort"])



if __name__ == "__main__":
    """
    Example values
    """
    sr = 100
    length = 2
    f = 1
    phi = 0
    Ti = 1
    Tp = 4
    R = 1e5 #Ohm
    C = 1e-6 #Farad

    runTask(sr, length, f, phi, Ti, Tp, R, C)
    plt.show()
