# principal.py

import numpy as np
from trazador_cubico import cargar_datos_trazador, calcular_trazador_cubico, graficar_trazador_cubico
from minimos_cuadrados import cargar_datos_minimos_cuadrados, calcular_minimos_cuadrados, graficar_minimos_cuadrados
from polinomios_ortogonales import calcular_polinomio_ortogonal, graficar_polinomio_ortogonal
from resolver_ecuaciones import cargar_sistema_ecuaciones, resolver_ecuaciones_lineales
import matplotlib.pyplot as plt

def main():
    # Paso 1: Trazador Cúbico Sujeto
    x_datos_trazador, y_datos_trazador = cargar_datos_trazador("datos/datos_trazador.csv")
    x_vals_trazador = np.linspace(min(x_datos_trazador), max(x_datos_trazador), 100)
    y_vals_trazador = calcular_trazador_cubico(x_datos_trazador, y_datos_trazador, x_vals_trazador)
    graficar_trazador_cubico(x_datos_trazador, y_datos_trazador, x_vals_trazador, y_vals_trazador)

    # Paso 2: Polinomio de Mínimos Cuadrados
    x_datos_ls, y_datos_ls = cargar_datos_minimos_cuadrados("datos/datos_minimos_cuadrados.csv")
    grado_ls = 2
    polinomio_ls = calcular_minimos_cuadrados(x_datos_ls, y_datos_ls, grado_ls)
    x_vals_ls = np.linspace(min(x_datos_ls), max(x_datos_ls), 100)
    y_vals_ls = polinomio_ls(x_vals_ls)
    graficar_minimos_cuadrados(x_datos_ls, y_datos_ls, x_vals_ls, y_vals_ls)

    # Paso 3: Polinomios Ortogonales (Legendre)
    grado_legendre = 3
    polinomio_legendre = calcular_polinomio_ortogonal(x_datos_ls, y_datos_ls, grado_legendre)
    y_vals_legendre = polinomio_legendre(x_vals_ls)
    graficar_polinomio_ortogonal(x_datos_ls, y_datos_ls, x_vals_ls, y_vals_legendre)

    # Paso 4: Resolución de Ecuaciones Lineales
    A, b = cargar_sistema_ecuaciones("datos/sistema_ecuaciones.csv")
    fuerzas = resolver_ecuaciones_lineales(A, b)
    print("Fuerzas en los puntos criticos:", fuerzas)

if __name__ == "__main__":
    main()
