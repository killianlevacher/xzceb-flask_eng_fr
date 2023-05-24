import unittest
from translator import english_to_french, french_to_english

class MyTestCase(unittest.TestCase):
    def test_english_to_french(self):
        result = english_to_french('Hello')
        fr_translation = result['translations'][0]['translation']
        self.assertEqual(fr_translation, 'Bonjour')

        with self.assertRaises(ValueError) as context:
            english_to_french(None)

    
    def test_french_to_english(self):
        result = french_to_english('Bonjour')
        en_translation = result['translations'][0]['translation']
        self.assertEqual(en_translation, 'Hello')

        with self.assertRaises(ValueError) as context:
            french_to_english(None)

if __name__ == '__main__':
    unittest.main()