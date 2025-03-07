import unittest
import addition
from volume_cone import cone
import volume_cone



class MyTestCase(unittest.TestCase):
    def test_addition_smaller_first(self):
        """
        You will use this function as a template for your own tests. You don't need to know what most of this means
        for right now, but the important thing is to change two lines: the addition.add_two() and the assert output
        lines. Everything else can stay the same.
        :return:
        """
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(2, 4)
            output = out.getvalue().strip()
            assert output == "The sum of 2 and 4 is 6"
        finally:
            sys.stdout = saved_stdout

    def test_addition_larger_first(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(12, 9)
            output = out.getvalue().strip()
            assert output == "The sum of 12 and 9 is 21"
        finally:
            sys.stdout = saved_stdout

    def test_adding_one_negative(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(-5, 10)
            output = out.getvalue().strip()
            assert output == "The sum of -5 and 10 is 5"
        finally:
            sys.stdout = saved_stdout

    def test_adding_two_negatives(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            addition.add_two(-5, -9)
            output = out.getvalue().strip()
            assert output == "The sum of -5 and -9 is -14"
        finally:
            sys.stdout = saved_stdout
    def test_volume_cone_0_height(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            volume_cone.cone(5, 0)
            output = out.getvalue().strip()
            assert output == "The volume of the cone is 0.0"
        finally:
            sys.stdout = saved_stdout
    def test_volume_cone_multiples_of_3_and_10(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            volume_cone.cone(30, 60)
            output = out.getvalue().strip()
            assert output == "The volume of the cone is 56548.67"
        finally:
            sys.stdout = saved_stdout
    def test_volume_cone_anything(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            volume_cone.cone(5, 8)
            output = out.getvalue().strip()
            assert output == "The volume of the cone is 209.44"
        finally:
            sys.stdout = saved_stdout





if __name__ == '__main__':
    unittest.main()
