import unittest
from operaciones.suma import sumar
from operaciones.resta import restar
from operaciones.multiplicacion import multiplicar
from operaciones.division import dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(5, 3), 8)
        self.assertEqual(sumar(0, 0), 0)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(0, 3), -3)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)
        self.assertEqual(multiplicar(0, 5), 0)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(7, 3), 2)  # División entera
        self.assertEqual(dividir(0, 5), 0)
        self.assertEqual(dividir(5, 0), "Error: división por cero")  # Manejo de error

if __name__ == "__main__":
    unittest.main()