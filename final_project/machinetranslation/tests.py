import unittest

from . translator import english_to_french, french_to_english

class TestEnglish(unittest.TestCase):
    """ Test en class """
    def test_eng(self):
        """ Test en method """
        self.assertEqual(english_to_french(None), None)
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')

class TestFrench(unittest.TestCase):
    """ Test fr class """
    def test_fr(self):
        """ Test fr method """
        self.assertEqual(french_to_english(None), None)
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()
