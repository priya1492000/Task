#Run command - >python -m unittest .\test_task_1.py

import unittest
from io import StringIO
from unittest.mock import patch

from task_1 import *

class TestTask1(unittest.TestCase):

    def test_generate_outcome(self):
        prob_map = [{"Head": 35}, {"Tail": 65}]
        output = generate_outcome(prob_map)

        assert output in ['Head', 'Tail']

    def test_print_outcome_with_frequency(self):
        prob_map_1 = [{"Head": 35}, {"Tail": 65}]

        with patch("sys.stdout", new=StringIO()) as fake_out:

            print_outcome_with_frequency(prob_map_1, 1000)

            assert "Head: 3" in fake_out.getvalue()
            assert "Tail: 6" in fake_out.getvalue()
