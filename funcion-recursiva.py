import unittest

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

class testfactorial(unittest.TestCase):
    
    def test0(self):
        resultado=factorial(0)
        self.assertEqual(resultado, 1)
    def test1(self):
        resultado=factorial(1)
        self.assertEqual(resultado, 1)
    def test2(self):
        resultado=factorial(2)
        self.assertEqual(resultado, 2)
    def test3(self):
        resultado=factorial(3)
        self.assertEqual(resultado, 6)
    def test4(self):
        resultado=factorial(4)
        self.assertEqual(resultado, 24)
    def test5(self):
        resultado=factorial(5)
        self.assertEqual(resultado, 120)
    def test6(self):
        resultado=factorial(6)
        self.assertEqual(resultado, 720)
    def test7(self):
        resultado=factorial(7)
        self.assertEqual(resultado, 5040)
    def test8(self):
        resultado=factorial(8)
        self.assertEqual(resultado, 40320)
    def test9(self):
        resultado=factorial(9)
        self.assertEqual(resultado, 362880)

if __name__ == "__main__":
    unittest.main()