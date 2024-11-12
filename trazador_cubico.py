# trazador_cubico.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import pandas as pd

# Función para cargar datos de CSV
def cargar_datos_trazador(archivo):
    datos = pd.read_csv(archivo)
    x_datos = datos['x'].values
    y_datos = datos['y'].values
    return x_datos, y_datos

# Función para calcular el trazador cúbico
def calcular_trazador_cubico(x_datos, y_datos, x_vals):
    trazador_cubico = CubicSpline(x_datos, y_datos, bc_type='natural')
    y_vals = trazador_cubico(x_vals)
    return y_vals

# Función para graficar el trazador cúbico
def graficar_trazador_cubico(x_datos, y_datos, x_vals, y_vals):
    plt.plot(x_datos, y_datos, 'o', label='Datos')
    plt.plot(x_vals, y_vals, label='Trazador Cúbico Sujeto')
    plt.title("Trazador Cúbico Sujeto")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
