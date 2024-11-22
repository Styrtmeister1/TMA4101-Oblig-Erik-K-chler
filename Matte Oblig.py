import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit
%matplotlib inline

    
Tk = -17.0
T01 = 38.8
T02 = 39.6

tid1 = np.array([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60])
tid2 = np.arange(0,81,2)
Termometer1 = np.array([38.8, 37.1, 35.5, 34.0, 32.6, 31.2, 29.8, 28.6, 27.3, 26.1, 24.9, 23.9, 22.9, 21.9, 21.0, 20.1, 19.2, 18.3, 17.4, 16.6, 15.7, 14.9, 14.1, 13.3, 12.6, 11.8, 11.1, 10.4, 9.7, 9.0, 8.4])
Termometer2 = np.array([39.6, 37.5, 34.6, 33.0, 30.4, 29.0, 26.8, 25.4, 23.4, 22.3, 20.5, 19.4, 17.8, 16.9, 15.4, 14.5, 13.3, 12.5, 11.4, 10.7, 9.6, 9.1, 8.1, 7.6, 6.8, 6.3, 5.3, 4.6, 4.0, 4.1, 3.5, 3.0, 2.4, 2.1, 1.6, 1.4, 1.0, 0.8, 0.5, 0.3, 0.1])

def avkjølingsmodel(t, α):
    return Tk + np.exp(-α*t)*(T01 - Tk)

popt1, pcov1 = curve_fit(avkjølingsmodel, tid1, Termometer1, p0=[0.1])
α1 = popt1[0]
print(f"Tilpasset α {α1:.4f}")
Tilpasning1 = avkjølingsmodel(tid1, α1)

popt2, pcov2 = curve_fit(avkjølingsmodel, tid2, Termometer2, p0=[0.1])
α2 = popt2[0]
print(f"Tilpasset α {α2:.4f}")
Tilpasning2 = avkjølingsmodel(tid2, α2)

plt.plot(tid1, Termometer1, "o-", label="Boks 1", color="cornflowerblue")
plt.plot(tid1, Tilpasning1, "-", label=f"Tilpasset modell1\nα={α1:.4f}", color="red")
plt.plot(tid2, Termometer2, "o-", label="Boks 2 (Tørkle)", color="darkorange")
plt.plot(tid2, Tilpasning2, "-", label=f"Tilpasset modell2\nα={α2:.4f}", color="lime")
plt.xlabel("Tid(minutter)")
plt.ylabel("Temperatur(C)")
plt.legend()
plt.grid(1)
plt.show()
