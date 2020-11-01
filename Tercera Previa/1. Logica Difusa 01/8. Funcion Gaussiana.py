# Funcion de Membresia gaussiana

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Se define la variable independiente
x = np.arange(0, 11, 0.1)

# Se define la varible dependiente gaussiana de membresia
vd_gaussiana = sk.gaussmf(x, np.mean(x), np.std(x))

# Se grafica la funcion de Membresia
plt.figure()
plt.plot(x, vd_gaussiana, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresia')
plt.xlabel('Nivel de Servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True,shadow=True)