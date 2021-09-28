import unittest
import return_addtion
import triangle_area

class MyTestCase(unittest.TestCase):

    def test_return_addtion(self):

        self.assertEqual(15, return_addtion.add_two(7, 8))
        self.assertEqual(45, return_addtion.add_two(40, 5))
        self.assertEqual(-15, return_addtion.add_two(-10, -5))
        self.assertEqual(5, return_addtion.add_two(-5, 10))
        # Add two more tests of your own below here

    def test_triangle_area(self):
        self.assertEqual(6.0, triangle_area.triangle_area(3, 4, 5))
        self.assertEqual(30.0, triangle_area.triangle_area(5, 12, 13))
        self.assertEqual(24.0, triangle_area.triangle_area(6, 8, 10))


if __name__ == '__main__':
    unittest.main()
