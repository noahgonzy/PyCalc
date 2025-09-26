#unit testing for calculator.py
import calculator
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.calculate("3+5"), "8.0")
    
    def test_subtraction(self):
        self.assertEqual(calculator.calculate("8-3"), "5.0")
    
    def test_multiplication(self):
        self.assertEqual(calculator.calculate("2*3"), "6.0")
    
    def test_division(self):
        self.assertEqual(calculator.calculate("10/2"), "5.0")
    
    def test_division_by_zero(self):
        self.assertEqual(calculator.calculate("10/0"), None)

    #test parentheses extensively
    def test_parentheses(self):
        self.assertEqual(calculator.calculate("(3+5)*2"), "16.0")
        self.assertEqual(calculator.calculate("((2+3)*4)-5"), "15.0")
        self.assertEqual(calculator.calculate("(((2+3)*4)-5)"), "15.0")
        self.assertEqual(calculator.calculate("(3+(2*5))"), "13.0")
        self.assertEqual(calculator.calculate("((1+2)*(3+4))"), "21.0")
        self.assertEqual(calculator.calculate("((1+2)*((3+4)-1))"), "18.0")

    def test_implicit_multiplication(self):
        self.assertEqual(calculator.calculate("2(3+4)"), "14.0")
        self.assertEqual(calculator.calculate("(1+2)(3+4)"), "21.0")
        self.assertEqual(calculator.calculate("3(2+5)(1+1)"), "42.0")
        self.assertEqual(calculator.calculate("2(3)(4)"), "24.0")

    def test_unbalanced_parentheses(self):
        #self.assertEqual(calculator.calculate("(3+5*2"), None)
        self.assertEqual(calculator.calculate("3+5)*2"), None)
    
    def test_combined_operations(self):
        self.assertEqual(calculator.calculate("3+5*2"), "13.0")
        self.assertEqual(calculator.calculate("(3+5)*2"), "16.0")
    
    def test_invalid_characters(self):
        self.assertEqual(calculator.calculate("3+5a"), None)
        self.assertEqual(calculator.calculate("3 5"), None)
    
    def test_whitespace_handling(self):
        self.assertEqual(calculator.calculate(" 3 + 5 "), "8.0")
        self.assertEqual(calculator.calculate(" ( 3 + 5 ) * 2 "), "16.0")
    
    def test_multiple_minuses(self):
        self.assertEqual(calculator.calculate("3--5"), "8.0")
        self.assertEqual(calculator.calculate("3---5"), "-2.0")
        self.assertEqual(calculator.calculate("3----5"), "8.0")
        self.assertEqual(calculator.calculate("3-----5"), "-2.0")

    def test_minuses_followed_by_pluses(self):
        self.assertEqual(calculator.calculate("3-+5"), "-2.0")
        self.assertEqual(calculator.calculate("3-++5"), "-2.0")
        self.assertEqual(calculator.calculate("3-+-5"), "8.0")
        self.assertEqual(calculator.calculate("3--+5"), "8.0")
    
    def test_plus_followed_by_minus(self):
        self.assertEqual(calculator.calculate("3+-5"), "-2.0")
        self.assertEqual(calculator.calculate("3++-5"), "-2.0")
        self.assertEqual(calculator.calculate("3+++-5"), "-2.0")
        self.assertEqual(calculator.calculate("3++++-5"), "-2.0")
    
    def test_complex_expressions(self):
        self.assertEqual(calculator.calculate("((2+3)*4)-5/((1+1)*2)"), "18.75")
        self.assertEqual(calculator.calculate("5+(6*3-(4/2))"), "21.0")
        self.assertEqual(calculator.calculate("10/(2+3)*(4-1)"), "6.0")
    



if __name__ == '__main__':
    unittest.main()