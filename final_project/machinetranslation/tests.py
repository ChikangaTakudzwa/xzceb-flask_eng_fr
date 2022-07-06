import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglish(unittest.TestCase):
    def test_eng(self):
        self.assertEqual(englishToFrench(None), ' ')
        self.assertNotEqual(englishToFrench('Hello'), 'Bonjour')

class TestFrench(unittest.TestCase):
    def test_fr(self):
        self.assertEqual(frenchToEnglish(None), ' ')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Hello')


unittest.main()
