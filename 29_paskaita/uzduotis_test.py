import unittest
from uzduotis import ar_lyginis, ar_nelyginis, ar_palindromas, prideti_unikalu, palyginti_sarasus
class TestUzduotis(unittest.TestCase):

 #1 UZDUOTIS

    def setUp(self):
        self.sarasas = [1, 3, 5, 7, 9]

    def tearDown(self):
        self.sarasas = None

    def test_prideti_elementa(self):
        prideti_unikalu(self.sarasas, 4)
        self.assertEqual(self.sarasas, [1, 3, 4, 5, 7, 9])

    def test_prideti_egzistuojanti_elementa(self):
        prideti_unikalu(self.sarasas, 5)
        self.assertEqual(self.sarasas, [1, 3, 5, 7, 9])
#SARUNO:
    # def setUp(self):
    #     self.x = [1,3,5,7,9]
    #     self.y = [2,4,6,8,10]
    #     self.rezultatas = [2]
    #     self.vienodi = [2,2]
    
    # def tearDown(self):
    #     self.x = None
    #     self.y = None
    # def test_prideti_elementa_sarasas(self):
    #     rezult = prideti_elementa(2, self.x)
    #     self.assertEqual(rezult, [1,2,3,5,7,9])
    # def test_prideti_elementa_sarasas2(self):
    #     rezult = prideti_elementa(3, self.x)
    #     self.assertEqual(rezult, 'Elementas jau yra sarase')
    # def test_prideti_elementa_sarasas3(self):
    #     sar = []
    #     for sk in self.y:
    #         sar = prideti_elementa(sk, sar)
    #     self.assertEqual(self.y, sar)
            
    # def test_prideti_elementa_sarasas4(self):
    #     sar = []
    #     for sk in self.vienodi:
    #         sar = prideti_elementa(sk, sar)
    #     self.assertEqual(sar, 'Elementas jau yra sarase')

 #2 UZDUOTIS


    def test_ar_lyginis_nelyginis(self):
        rezultatas = ar_lyginis(9)
        self.assertTrue(rezultatas)

    def test_ar_lyginis(self):
        rezultatas = ar_lyginis(8)
        self.assertFalse(rezultatas)
#MANTVYDO:
    def test_ar_nelyginis(self):
        rezultatas = ar_nelyginis(9)
        self.assertTrue(rezultatas)   
        # self.assertTrue(ar_nelyginis(3))
    def test_ar_nelyginis2(self):
        rezultatas = ar_nelyginis(2)
        self.assertFalse(rezultatas)
        # self.assertFalse(ar_nelyginis(2))
 
 #3 UZDUOTIS

    def test_palindromas(self):
        rezultatas = ar_palindromas("sos")
        self.assertTrue(rezultatas)
        rezultatas = ar_palindromas("eye")
        self.assertTrue(rezultatas)
    
    def test_ne_palindromas(self):
        rezultatas = ar_palindromas("hello")
        self.assertFalse(rezultatas)
        rezultatas = ar_palindromas("python")
        self.assertFalse(rezultatas)
        

 #4 UZDUOTIS   

    def test_lygus_sarasai(self):
        self.assertEqual(palyginti_sarasus([1, 2, 3], [1, 2, 3]), True)
        self.assertEqual(palyginti_sarasus([], []), True)
        self.assertEqual(palyginti_sarasus(['a', 'b', 'c'], ['a', 'b', 'c']), True)
    
    def test_skirtingi_sarasai(self):
        self.assertNotEqual(palyginti_sarasus([1, 2, 3], [1, 2]), True)
        self.assertNotEqual(palyginti_sarasus([1, 2, 3], [3, 2, 1]), True)
        self.assertNotEqual(palyginti_sarasus(['a', 'b', 'c'], ['c', 'b', 'a']), True)

#ANOS:
class TestPalygintiSarasus(unittest.TestCase):
    def test_lygus_sarasai(self):
        sarasai = palyginti_sarasus([1, 2, 3], [1, 2, 3])
        self.assertEqual(sarasai, True)
    def test_skirtingi_sarasai(self):
        sarasai = palyginti_sarasus([1, 2, 3], [2, 5, 8])
        self.assertNotEqual(sarasai, True)


if __name__ == '__main__':
    unittest.main()