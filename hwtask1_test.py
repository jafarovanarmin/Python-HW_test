import Task_1
import unittest
from unittest.mock import patch
from io import StringIO
from random import choice


class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["2", "6"])
    def test_main_input_calls(self, mock_input):
        Task_1.main()
        expected_calls = ["Enter a num1: ", "Enter a num2: "]
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def _test_with_input(self, input_value, expected_output):
        with patch('builtins.input', side_effect=input_value), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_1.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
 
    def test_input(self):
        data = [[2,3,5,6,2.5],[-4,6,2,-24,1.0],[-6,-2,-8,12,-4.0],[3,78,81,234,40.5]]
        for test in data:
            expected_output = f"Total: {test[2]}\nProduct: {test[3]}\nAverage: {test[4]}\n"
            self._test_with_input(test[:2], expected_output)
