#Run command - >python -m unittest .\test_task_2.py

import unittest
from io import StringIO
from unittest.mock import patch

from task_2 import evaluate_expressions, print_output

class TestTask2(unittest.TestCase):

    def test_evaluate_expressions(self):
        # Enter input as 2*4*4 and then enter end
        expected_output = [{'expression': '2*4*4', 'result': '32'}]

        actual_output = evaluate_expressions()

        self.assertEqual(actual_output, expected_output)

    def test_print_output(self):

        with patch("sys.stdout", new=StringIO()) as fake_out:
            results = [{'expression': '2*4*4', 'result': '32'}]
            print_output(results)

            assert "2*4*4 => 32" in fake_out.getvalue()
