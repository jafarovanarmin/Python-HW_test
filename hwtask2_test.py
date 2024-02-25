import Task_2
import unittest
from unittest.mock import patch
from io import StringIO
from random import choice


class TestMainFunction(unittest.TestCase):
    
    @patch('builtins.input', side_effect=["2", "6.5", "30.9"])
    def test_main_input_calls(self, mock_input):
        Task_2.main()
        expected_calls = ["Side 1: ", "Side 2: ", "Angle(degree): "]
        self.assertEqual(mock_input.call_args_list, [unittest.mock.call(arg) for arg in expected_calls])

    def _test_with_input(self, input_value, expected_output):
        with patch('builtins.input', side_effect=input_value), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Task_2.main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
 
    def test_input(self):
        data = [[8,9,45,25.46],[12,23,126,111.64],[3,4,90,6.00],[7.6,9.8,30.4,18.84]]
        for test in data:
            expected_output = f"Area: {test[3]:.2f}\n"
            self._test_with_input(test[:3], expected_output)
