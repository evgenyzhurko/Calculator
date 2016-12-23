 #!/usr/bin/env python2

import unittest
from math import *
from calculator import evaluate

class TestCalcExpression(unittest.TestCase):

    def test_notation(self):
        self.assertEqual(8, evaluate("0b1000"))
        self.assertEqual(8, evaluate("0o10"))
        self.assertEqual(8, evaluate("0x8"))  
        self.assertEqual(64, evaluate("0x40"))
        self.assertEqual(11, evaluate("0xB"))      

    def test_unary(self):
        self.assertEqual(2, evaluate("6-4"))
        self.assertEqual(10, evaluate("6--4"))
        self.assertEqual(-10, evaluate("-6+-4"))
        self.assertEqual(2, evaluate("6-+4"))
        self.assertEqual(10, evaluate("6-(-(-(-4)))"))

    def test_priority(self):
        self.assertEqual(3, evaluate("1+1*2"))
        self.assertEqual(-1, evaluate("1+1*-2"))
        self.assertEqual(0.25, evaluate("2**-2"))
        self.assertEqual(1, evaluate("1 & 2 + 3"))

    def test_functions(self):
        self.assertEqual(1, evaluate("log10(10)"))
        self.assertEqual(0, evaluate("tan(0)"))
        self.assertEqual(5, evaluate("pow(2, 2) + 1"))
        self.assertEqual(0, evaluate("sin(0)"))
        self.assertEqual(1, evaluate("abs(-1)"))
        self.assertEqual(1, evaluate("round(1.49)"))
        self.assertEqual(2, evaluate("round(1.51)"))

    def test_constants(self):
        self.assertEqual(pi + 1, evaluate("pi+1"))
        self.assertEqual(e + 2, evaluate("e + 2"))

    def test_comparison(self):
        self.assertEqual(1 == 1, evaluate("1 == 1"))
        self.assertEqual(1 != 2, evaluate("1 != 2"))
        self.assertEqual(1 <> 1, evaluate("1 <> 1"))
        self.assertEqual(1 > 2, evaluate("1 > 2"))
        self.assertEqual(1 + 1 <= 5 + 5, evaluate("1 + 1 <= 5 + 5"))

    def test_full(self):
        self.assertEqual(-100, evaluate("-pow(1*4+3.3/(3 + .3)*3(sqrt(4))/(sin(pi - pi) + 1), 0b10)"))
        self.assertEqual(10*e**0*log10(.4* -5/ -0.1-10) - -abs(-53//10) + -5,
            evaluate("10*e**0*log10(.4* -5/ -0.1-10) - -abs(-53//10) + -5"))
        self.assertEqual((-100)**(2/2), evaluate("(-100)^(2/2)"))
        self.assertEqual(((6+4)*-5), evaluate("((6+4)*-5)"))
        self.assertEqual((2 << 2 != 100)+ 1, evaluate("(2 << 2 != 100)+ 1"))
        self.assertEqual(2**2 > 3, evaluate("0b10 ^ 0b10 > 0o3"))

if __name__ == '__main__':
    unittest.main()