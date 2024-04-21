import unittest
from recursiva_y_kwargs import buscar_datos, database

class TestBuscarDatos(unittest.TestCase):
    
    def test_persona1(self):
        self.assertEqual(buscar_datos("pablo", "emilio", "gomez", "Picasso", **database), "La persona persona1 existe en la base de datos.")
    
    def test_persona_no_existente(self):
        self.assertEqual(buscar_datos("ricardo", "alejandro", "vera", "martinez", **database), "La persona que buscas no existe en la base de datos.")

    def test_persona2(self):
        self.assertEqual(buscar_datos("juan", "antonio", "perez", "lopez", **database), "La persona persona2 existe en la base de datos.")

    def test_persona_no_existente_2(self):
        self.assertEqual(buscar_datos("juan", "pedro", "goma", "martinez", **database), "La persona que buscas no existe en la base de datos.")
    
    def test_persona3(self):
        self.assertEqual(buscar_datos("maria", "luisa", "garcia", "martinez", **database), "La persona persona3 existe en la base de datos.")

    def test_persona4(self):
        self.assertEqual(buscar_datos("luis", "gomez", "garcia", **database), "La persona persona4 existe en la base de datos.")

    def test_persona_no_existente_3(self):
        self.assertEqual(buscar_datos("nombre1", "nombre2", "apellido", "apellido", **database), "La persona que buscas no existe en la base de datos.")

    def persona5(self):
        self.assertEqual(buscar_datos("luis", "antonio", "gomez", **database), "La persona persona5 existe en la base de datos.")

    def test_datos_insuficientes(self):
        self.assertEqual(buscar_datos("luis", "antonio", **database), "Datos ingresados insuficientes para verificar en la base de datos.")
   
    def test_persona6(self):
        self.assertEqual(buscar_datos("luis", "antonio", "gomez", "lopez", **database), "La persona persona6 existe en la base de datos.")
    
    def test_persona7(self):
        self.assertEqual(buscar_datos("luis", "antonio", "gomez", "lopez", "martinez", **database), "La persona persona7 existe en la base de datos.")
    
    def test_persona8(self):
        self.assertEqual(buscar_datos("luis", "antonio", "gomez", "lopez", "martinez", "perez", **database), "La persona persona8 existe en la base de datos.")
    
    def test_persona9(self):
        self.assertEqual(buscar_datos("luis", "antonio", "gomez", "lopez", "martinez", "perez", "garcia", **database), "La persona persona9 existe en la base de datos.")
    
    def test_persona10(self):
        self.assertEqual(buscar_datos("luis", "antonio", "gomez", "lopez", "martinez", "perez", "garcia", "gomez", **database), "La persona persona10 existe en la base de datos.")
    
    def test_persona11(self):
        self.assertEqual(buscar_datos("luis", "antonio", "gomez", "lopez", "martinez", "perez", "garcia", "gomez", "perez", **database), "La persona persona11 existe en la base de datos.")

if __name__ == "__main__":        
    unittest.main()