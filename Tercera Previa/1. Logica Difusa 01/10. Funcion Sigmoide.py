# Funcion de Membresia sigmoide

import numpy as np
import skfuzzy as sk
import matplotlib.pyplot as plt

# Se define la variable independiente
x= np.arange(-11, 11, 1)

# Se define la varible dependiente sigmoide de membresia
vd_sigmoide = sk.sigmf (x, 0,1)

# Se grafica la funcion de Membresia
plt.figure()
plt.plot(x, vd_sigmoide, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad del servicio en un restaurante')
plt.ylabel('Membresia')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)