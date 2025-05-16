# correr desde una terminal: python -m unittest test_semana_02.py
# no me funciono si hacia: run test_semana_02.py

from semana_02 import (
    invertir_lista,
    collatz,
    contar_definiciones,
    cantidad_de_claves_letra,
    propagar,
)
import unittest


# Ejercicio 1: Invertir una lista
class TestInvertirLista(unittest.TestCase):

    def test_lista_vacia(self):
        self.assertEqual(invertir_lista([]), [])

    def test_un_elemento(self):
        self.assertEqual(invertir_lista([3]), [3])

    def test_varios_elementos(self):
        self.assertEqual(invertir_lista([5, 2, 3]), [3, 2, 5])

    def test_elementos_repetidos(self):
        self.assertEqual(invertir_lista([1, 2, 2, 3]), [3, 2, 2, 1])

    def test_tipos_mixtos(self):
        self.assertEqual(invertir_lista([1, "a", True]), [True, "a", 1])


# Ejercicio 2: conjetura Collatz
class TestCollatz(unittest.TestCase):

    def test_collatz_calcuables_mano(self):
        self.assertEqual(collatz(1), 0)  # Ya en 1, sin pasos
        self.assertEqual(collatz(2), 1)  # 2 → 1 (1 paso)
        self.assertEqual(collatz(3), 7)  # 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (7 pasos)
        self.assertEqual(collatz(6), 8)  # 6 → 3 → ... → 1 (1 paso + pasos de 3 = 8)


    def test_valor_invalido(self):
        with self.assertRaises(ValueError):
            collatz(-5)
        with self.assertRaises(ValueError):
            collatz(0)


# Ejercicio 3: diccionarios
class TestDiccionarios(unittest.TestCase):

    def test_diccionario_vacio(self):
        self.assertEqual(contar_definiciones({}), {})
        self.assertEqual(cantidad_de_claves_letra({}, "a"), 0)

    def test_diccionario_definiciones(self):
        d = {
            "perro": ["mamífero", "doméstico"],
            "gato": ["mamífero", "doméstico", "cazador"],
        }
        expected = {"perro": 2, "gato": 3}
        self.assertEqual(contar_definiciones(d), expected)

    def test_cantidad_letra_no_existe(self):
        d = {"manzana": ["fruta"], "naranja": ["fruta"]}
        self.assertEqual(cantidad_de_claves_letra(d, "z"), 0)

    def test_case_sensitivity(self):
        d = {"Auto": [], "avión": []}
        # lo hice sensible a mayusculas, lo que en realidad se podria cambiar
        self.assertEqual(cantidad_de_claves_letra(d, "A"), 1)


# Ejercicio 4
class TestPropagar(unittest.TestCase):

    def test_propagacion_simple(self): # no hay quemados y hay 1
        self.assertEqual(
            propagar([0, 0, 0, 1, 0, 0]), [1, 1, 1, 1, 1, 1]
        )  
        self.assertEqual(propagar([1, 0, 0]), [1, 1, 1])
        self.assertEqual(propagar([0, 0, 1]), [1, 1, 1])

    def test_bloqueo_con_carbonizados(self):
        self.assertEqual(
            propagar([0, -1, 1, 0, 0, -1, 0, 1, 0]), [0, -1, 1, 1, 1, -1, 1, 1, 1]
        )

    def test_sin_propagacion(self):
        self.assertEqual(propagar([0, 0, 0]), [0, 0, 0])
        self.assertEqual(propagar([-1, -1]), [-1, -1])

    def test_todo_encendido(self):
        self.assertEqual(propagar([1, 1, 1]), [1, 1, 1])

    def test_bordes(self):
        self.assertEqual(propagar([]), [])
        self.assertEqual(propagar([1]), [1])
        self.assertEqual(propagar([0]), [0])
        self.assertEqual(propagar([-1]), [-1])


if __name__ == "__main__":
    unittest.main()
