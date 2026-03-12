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
    

def createComplexWaves(t, C, r, f, phi):

    x_t = np.abs(C) * np.exp((r+1j*2*np.pi*f)*t+1j*phi)

    comp_cos_t = np.real(x_t)

    comp_sin_t = np.imag(x_t)

    return comp_cos_t, comp_sin_t
    



def runTask(sr, length, cos_amplitude, cos_frequency, cos_phase, cos_time_behavior):
    """
    3. Erzeugen Sie mithilfe der bereits bestehenden Funktionsdefinition eine 
    Funktion "runTask" order erweitern Sie Ihre Funktion aus der letzten Aufgabe. 
    Diese Funktion bekommt 6 Parameter übergeben: sr, length, cos_amplitude ("amplitude cosinus"),
    cos_freq ("frequency cosinus"), cos_phase ("phase cosinus") und cos_time_behavior ("time bahvior cosinus"). 
    Mithilfe dieser Parameter können die bereits erzeugten Funktionen angesprochen werden. 
    Im weiteren Verlauf sollen sowohl der reel erzeugte Kosinus (createCos) als auch die beiden komplexen 
    Schwingungen (createComplexWaves) erzeugt und dargestellt werden. Gehen Sie vor wie in der zuvor gelösten Aufgabe:
        1. Erzeugen Sie ein neues figure.
        2. Plotten Sie alle 3 Signale in die gleiche Darstellung. Wählen Sie selbständig unterschiedliche Farben nach 
           Ihrer Wahl zur Unterscheidung. Sorgen Sie mithilfe des Parameters "linestyle" der plot Funktion dafür, 
           dass die beiden complex generierten Schwingungen mit einer gestrichelten Linie dargestellt werden.
        3. Benennen Sie die einzelnen Schwingungen mithilfe des Parameters "label" der plot Funktion. 
           Verwenden Sie eindeutige und unterschiedliche Namen! Zeigen Sie diese mithilfe einer Legende in der Darstellung
           auf (-> funktion "legend").
        4. Setzen sie auch dieses mal mithilfe der Befehle xlabel() und ylabel() die Namen der Achsen, wobei die Beschriftung 
           der x-Achse "time" und die der y-Achse "amplitude" lauten soll. 

    Achtung: diese Funktion gibt keine Werte zurück!
    """
    # Fixed cos creation
    x_axis_fixed = createTimeAxis(sr,length)
    y_axis_fixed = createCos(x_axis_fixed, cos_amplitude, cos_frequency, cos_phase)
    plt.xlabel("time")
    plt.ylabel("amplitude")

    # Complex cos values
    y_axis_comp_cos = createComplexWaves(x_axis_fixed, cos_amplitude, cos_time_behavior, cos_frequency, cos_phase)[0] 

    # Complex sin values
    y_axis_comp_sin = createComplexWaves(x_axis_fixed, cos_amplitude, cos_time_behavior, cos_frequency, cos_phase)[1]

    # output (plotting)
    plt.plot(x_axis_fixed, y_axis_fixed, color='r')
    plt.plot(x_axis_fixed, y_axis_comp_cos, linestyle='--', color='y')
    plt.plot(x_axis_fixed, y_axis_comp_sin, linestyle='--',color='g')

    plt.legend(["Fixed cos", "Complex Cos", "Complex Sine"])




if __name__ == "__main__":
    """
    Example values:
    """
    sr = 100
    length = 1
    cos_amplitude = 1
    cos_phase = 0
    cos_frequency = 1
    cos_time_behavior = 0

    runTask(sr, length, cos_amplitude, cos_frequency, cos_phase, cos_time_behavior)
    plt.show()
