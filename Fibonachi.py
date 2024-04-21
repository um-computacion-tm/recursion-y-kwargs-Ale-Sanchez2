import unittest


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class testfibonacci(unittest.TestCase):
    def test0(self):
        resultado=fibonacci(0)
        self.assertEqual(resultado, 0)
    def test1(self):
        resultado=fibonacci(1)
        self.assertEqual(resultado, 1)
    def test2(self):
        resultado=fibonacci(2)
        self.assertEqual(resultado, 1)
    def test3(self):
        resultado=fibonacci(3)
        self.assertEqual(resultado, 2)
    def test4(self):
        resultado=fibonacci(4)
        self.assertEqual(resultado, 3)
    def test5(self):
        resultado=fibonacci(5)
        self.assertEqual(resultado, 5)
    def test6(self):
        resultado=fibonacci(6)
        self.assertEqual(resultado, 8)
    def test7(self):
        resultado=fibonacci(7)
        self.assertEqual(resultado, 13)
    def test8(self):
        resultado=fibonacci(8)
        self.assertEqual(resultado, 21)
    def test9(self):
        resultado=fibonacci(9)
        self.assertEqual(resultado, 34)
    def test10(self):
        resultado=fibonacci(10)
        self.assertEqual(resultado, 55)
    def test11(self):
        resultado=fibonacci(11)
        self.assertEqual(resultado, 89)
    def test12(self):
        resultado=fibonacci(12)
        self.assertEqual(resultado, 144)
    def test13(self):
        resultado=fibonacci(13)
        self.assertEqual(resultado, 233)
    def test14(self):
        resultado=fibonacci(14)
        self.assertEqual(resultado, 377)
    def test15(self):
        resultado=fibonacci(15)
        self.assertEqual(resultado, 610)
    def test16(self):
        resultado=fibonacci(16)
        self.assertEqual(resultado, 987)
    def test17(self):
        resultado=fibonacci(17)
        self.assertEqual(resultado, 1597)
    def test18(self):
        resultado=fibonacci(18)
        self.assertEqual(resultado, 2584)
    def test19(self):
        resultado=fibonacci(19)
        self.assertEqual(resultado, 4181)
    def test20(self):
        resultado=fibonacci(20)
        self.assertEqual(resultado, 6765)
    def test21(self):
        resultado=fibonacci(21)
        self.assertEqual(resultado, 10946)
    def test22(self):
        resultado=fibonacci(22)
        self.assertEqual(resultado, 17711)
    
if __name__ == '__main__':
    unittest.main()
