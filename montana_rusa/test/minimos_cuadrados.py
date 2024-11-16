
import numpy as np
import unittest
from pandas import read_csv
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),"..","src"))
from principal import polinomio_cuadrado

class TestCuadrado(unittest.TestCase):
    def test_polinomio_ortogonal(self):
        archivo = os.path.join(os.path.dirname(__file__), "..", "src", "datos_minimos_cuadrados.csv")
        datos = read_csv(archivo)
        x_datos = datos['x'].values
        y_datos = datos['y'].values
        x_values = np.linspace(0,4,100)
        minimos = polinomio_cuadrado(x_datos,y_datos,x_values)
        np.testing.assert_allclose(minimos, minimos, atol=0.1)

unittest.main()