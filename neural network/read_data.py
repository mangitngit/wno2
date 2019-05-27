import numpy as np
import matplotlib.pyplot as plt

odczyt = np.load("sroda_rano/test.npy")
odczytk = np.load("sroda_rano/testk.npy")

fig1, ax1 = plt.subplots(1, sharex='col', sharey='row')

print(odczytk[9])
plt.imshow(odczyt[9])
plt.show()
