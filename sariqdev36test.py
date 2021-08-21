import unittest
from sariqdev36 import tub_son, fibonaci, max_son, upper_list

class Test36(unittest.TestCase):
    def test_tub(self):
        l = [31, 235, 35, 55, 8, 7, 41, 22, 35, 68, 78, 65, 589, 74]
        self.assertEqual(tub_son(l), [8, 22, 68, 78, 74])
    def test_fib(self):
        self.assertEqual(fibonaci(5, 5), True)
        self.assertFalse(fibonaci(6, 6))
    def test_max(self):
        self.assertEqual(max_son(22, 21, 55), 55)
        self.assertNotEqual(max_son(552, 54, 4), 54)
    def test_u(self):
        l = ['ahror', 'dilmurod', 'azizbek']
        self.assertEqual(upper_list(l),['Ahror', 'Dilmurod', 'Azizbek'])

unittest.main()


































