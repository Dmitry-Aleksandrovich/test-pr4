# test_data_processing.py
import unittest
from data_processing import process_data

class TestProcessData(unittest.TestCase):
    def test_positive_numbers(self):
        """
        Тестирует обработку списка с положительными числами.
        """
        self.assertEqual(process_data([1, 2, 3]), [1, 4, 9])
    
    def test_negative_numbers(self):
        """
        Тестирует обработку списка с отрицательными числами.
        """
        self.assertEqual(process_data([-1, -2, 3]), [9])
    
    def test_mixed_numbers(self):
        """
        Тестирует обработку списка с положительными, отрицательными числами и нулями.
        """
        self.assertEqual(process_data([0, -1, 4]), [16])

if __name__ == "__main__":
    unittest.main()

