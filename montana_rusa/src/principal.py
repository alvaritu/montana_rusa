# principal.py

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from test.resolver_ecuaciones import cargar_sistema_ecuaciones, resolver_ecuaciones_lineales

def trazado_cubico(x_datos, y_datos, x_vals):
    # Paso 1: Trazador Cúbico Sujeto
    trazador_cubico = sp.interpolate.CubicSpline(x_datos, y_datos, bc_type='natural')
    y_vals = trazador_cubico(x_vals)
    plt.plot(x_datos, y_datos, 'o', label='Datos')
    plt.plot(x_vals, y_vals, label='Trazador Cúbico Sujeto')
    plt.title("Trazador Cúbico Sujeto")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    return y_vals


def polinomio_cuadrado(x_datos, y_datos, x_vals):
    polinomio_ls = np.polynomial.Polynomial.fit(x_datos,y_datos,2)
    y_vals = polinomio_ls(x_vals)
    plt.plot(x_datos, y_datos, 'o', label='Datos')
    plt.plot(x_vals, y_vals, label='Polinomio de Mínimos Cuadrados')
    plt.title("Polinomio de Mínimos Cuadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    return y_vals
    

def polinomio_ortogonal(x_datos,y_datos,x_vals):
    polinomio_legendre = np.polynomial.legendre.Legendre.fit(x_datos, y_datos, 3)
    y_vals = polinomio_legendre(x_vals)
    plt.plot(x_datos, y_datos, 'o', label='Datos')
    plt.plot(x_vals, y_vals, label='Polinomio Ortogonal (Legendre)')
    plt.title("Polinomio Ortogonal (Legendre)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    return y_vals


def reso_ec():
    # Paso 4: Resolución de Ecuaciones Lineales
    A, b = cargar_sistema_ecuaciones("datos/sistema_ecuaciones.csv")
    fuerzas = resolver_ecuaciones_lineales(A, b)
    print("Fuerzas en los puntos criticos:", fuerzas)
