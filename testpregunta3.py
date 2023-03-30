import unittest 
from Pregunta3 import alumno

class TestAlumno(unittest.TestCase):
    def test_alumno(self):
        alumno1 = alumno("Juan", 5)
        alumno2 = alumno("Pedro", 4)
        alumno3 = alumno("Maria", 10)
        self.assertEqual(alumno1.nombre, None)
        self.assertEqual(alumno1.nota, 5)
        self.assertEqual(alumno1.__str__(),"Juan")
        self.assertEqual(alumno1.__cali__(),5)
        self.assertEqual(alumno2.nombre, None)
        self.assertEqual(alumno2.nota, 4)
        self.assertEqual(alumno2.__str__(), "Pedro")
        self.assertEqual(alumno2.__cali__(),  4)
        self.assertEqual(alumno3.nombre, "Maria")
        self.assertEqual(alumno3.nota, 10)
        self.assertEqual(alumno3.__str__(),"Maria")
        self.assertEqual(alumno3.__cali__(),10)
        
