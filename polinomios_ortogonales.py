# polinomios_ortogonales.py

import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import Legendre

# Función para calcular el polinomio ortogonal (Legendre)
def calcular_polinomio_ortogonal(x_datos, y_datos, grado):
    polinomio_legendre = Legendre.fit(x_datos, y_datos, grado)
    return polinomio_legendre

# Función para graficar el polinomio ortogonal
def graficar_polinomio_ortogonal(x_datos, y_datos, x_vals, y_vals):
    plt.plot(x_datos, y_datos, 'o', label='Datos')
    plt.plot(x_vals, y_vals, label='Polinomio Ortogonal (Legendre)')
    plt.title("Polinomio Ortogonal (Legendre)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
