import unittest
from unittest import mock

import assignment_three


class MyTestCase(unittest.TestCase):
        def test_input(self):
            with mock.patch('assignment_three.input', return_value="3"):
                assert type(assignment_three.get_side_length()) == float
        def test_input(self):
            with mock.patch('assignment_three.input', return_value="blue"):
                assert type(assignment_three.get_center_color()) == str
        def test_input(self):
            with mock.patch('assignment_three.input', return_value="red"):
                assert type(assignment_three.get_petal_color()) == str
        # add assertion here


if __name__ == '__main__':
    unittest.main()
