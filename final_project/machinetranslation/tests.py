import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglish(unittest.TestCase):
    """ Test en class """
    def test_eng(self):
        """ Test en method """
        self.assertEqual(englishToFrench(None), ' ')
        self.assertNotEqual(englishToFrench('Hello'), 'Bonjour')

class TestFrench(unittest.TestCase):
    """ Test fr class """
    def test_fr(self):
        """ Test fr method """
        self.assertEqual(frenchToEnglish(None), ' ')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Hello')


unittest.main()
