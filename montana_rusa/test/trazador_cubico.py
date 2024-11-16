# trazador_cubico.py

import numpy as np
import unittest
from scipy.interpolate import CubicSpline
from pandas import read_csv
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from src.principal import trazado_cubico

class TestCubico(unittest.TestCase):
    def test_trazador(self):
        archivo = os.path.join(os.path.dirname(__file__), "..", "src", "datos_trazador.csv")
        datos = read_csv(archivo)
        x_datos = datos['x'].values
        y_datos = datos['y'].values
        x_values = np.linspace(0,5,100)
        trazador = trazado_cubico(x_datos,y_datos,x_values)
        np.testing.assert_allclose(trazador,trazador, atol=0.1)

unittest.main()
