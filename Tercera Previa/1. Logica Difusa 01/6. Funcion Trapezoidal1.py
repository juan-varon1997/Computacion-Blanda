# Funcion de Membresia trapeizodal

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Se define la variable independiente
x = np.arange(0, 11, 1)

# Se define la varible dependiente trapezoidal de membresia
vd_trapezoidal = sk.trimf(x, [0, 0, 5, 5])

# Se grafica la funcion de Membresia
plt.figure()
plt.plot(x, vd_trapezoidal, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresia')
plt.xlabel('Nivel de Servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True,shadow=True)