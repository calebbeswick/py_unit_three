import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
        def test_input(self):
            with mock.patch('assignment_three.input', return_value="3"):
                assert type(assignment_three.get_side_length()) == float

        # add assertion here


if __name__ == '__main__':
    unittest.main()
