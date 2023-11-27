import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.random_number import generate_random_number

class TestRandomNumber(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', '10'])
    def test_generate_random_number_valid_input(self, mock_input):
        output = StringIO()
        with patch('sys.stdout', output):
            generate_random_number()

        expected_output = "Generated Random Number: "
        self.assertTrue(output.getvalue().startswith(expected_output))

    @patch('builtins.input', side_effect=['abc', '10'])
    def test_generate_random_number_invalid_input(self, mock_input):
        output = StringIO()
        with patch('sys.stdout', output):
            generate_random_number()

        expected_output = "Error:"
        self.assertTrue(expected_output in output.getvalue())

if __name__ == '__main__':
    unittest.main()
