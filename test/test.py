from carpeta1.archivo1 import suma

import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(suma(1, 1), 2)
        