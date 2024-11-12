# minimos_cuadrados.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Función para cargar datos de CSV
def cargar_datos_minimos_cuadrados(archivo):
    datos = pd.read_csv(archivo)
    x_datos = datos['x'].values
    y_datos = datos['y'].values
    return x_datos, y_datos

# Función para calcular el polinomio de mínimos cuadrados
def calcular_minimos_cuadrados(x_datos, y_datos, grado):
    coeficientes = np.polyfit(x_datos, y_datos, grado)
    polinomio = np.poly1d(coeficientes)
    return polinomio

# Función para graficar el polinomio de mínimos cuadrados
def graficar_minimos_cuadrados(x_datos, y_datos, x_vals, y_vals):
    plt.plot(x_datos, y_datos, 'o', label='Datos')
    plt.plot(x_vals, y_vals, label='Polinomio de Mínimos Cuadrados')
    plt.title("Polinomio de Mínimos Cuadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
