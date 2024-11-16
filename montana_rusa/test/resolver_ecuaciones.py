# resolver_ecuaciones.py

import numpy as np
import pandas as pd
from pandas import read_csv
from scipy.linalg import solve
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from src.principal import reso_ec

# Función para cargar el sistema de ecuaciones desde un archivo CSV
def cargar_sistema_ecuaciones(archivo):
    datos = pd.read_csv(archivo)
    archivo = os.path.join(os.path.dirname(__file__), "..", "src", "datos_trazador.csv")
    datos = read_csv(archivo)
    A = datos[['a11', 'a12', 'a13']].values
    b = datos['b'].values
    return A, b

# Función para resolver el sistema de ecuaciones lineales
def resolver_ecuaciones_lineales(A, b):
    return solve(A, b)
