# test_data_validator.py
import unittest
from data_validator import validate_data

class TestValidateData(unittest.TestCase):
    def test_all_integers(self):
        """
        Тестирует список, содержащий только целые числа.
        """
        self.assertTrue(validate_data([1, 2, 3, 4]))
    
    def test_with_strings(self):
        """
        Тестирует список, содержащий строки.
        """
        self.assertFalse(validate_data([1, "a", 3]))
    
    def test_empty_list(self):
        """
        Тестирует пустой список.
        """
        self.assertTrue(validate_data([]))

if __name__ == "__main__":
    unittest.main()

