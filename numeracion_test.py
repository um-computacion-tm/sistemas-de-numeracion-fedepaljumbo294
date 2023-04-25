import unittest

from numeracion import decimal_binario,decimal_octal,decimal_hexa,binario_decimal,octal_decimal,hexa_decimal,binario_octal,binario_hexa,octal_hexa,hexa_octal

class Test(unittest.TestCase):
    def test_decimal_binario(self):
        resultado=decimal_binario(666)
        self.assertEqual(resultado,'1010011010')
        
    def test_decimal_octal(self):
        resultado=decimal_octal(666)
        self.assertEqual(resultado,'1232')
        
    def test_decimal_hexa(self):
        resultado=decimal_hexa(666)
        self.assertEqual(resultado,'29A')
        
    def test_binario_decimal(self):
        resultado=binario_decimal('1010011010')
        self.assertEqual(resultado,666)
        
    def test_octal_decimal(self):
        resultado=octal_decimal('1232')
        self.assertEqual(resultado,666)
    
    def test_hexa_decimal(self):
        resultado=hexa_decimal('29A')
        self.assertEqual(resultado,666)
        
    def test_binario_octal(self):
        resultado=binario_octal('1010011010')
        self.assertEqual(resultado,1232)
        
    def test_binario_hexa(self):
        resultado=binario_hexa('1010011010')
        self.assertEqual(resultado,'29A')
    
    def test_octal_hexa(self):
        resultado=octal_hexa('1232')
        self.assertEqual(resultado,'29A')
        
    def test_hexa_octal(self):
        resultado=hexa_octal('29A')
        self.assertEqual(resultado,1232)
        
if __name__=="__main__":
    unittest.main()