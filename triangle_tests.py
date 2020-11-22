import unittest
from triangle import Point, Triangle, TaskSolver


class TestPointAddMethod(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Point(2, 3) + Point(3, 3), (5, 6))
        self.assertEqual(Point(2.5, 3.0) + Point(1.2, 3.2), (3.7, 6.2))
        self.assertEqual(Point(-2, -3) + Point(2, 3), (0, 0))


class TestTriangleMethods(unittest.TestCase):
    def test_is_triangle(self):
        tr = Triangle(Point(0, 0), Point(0, 3), Point(4, 0))
        self.assertTrue(tr.is_triangle())

        tr = Triangle(Point(0, 0), Point(0, 3), Point(10, 0))
        self.assertTrue(tr.is_triangle())

        tr = Triangle(Point(0, 1.5), Point(3, 0), Point(1.5, 1))
        self.assertTrue(tr.is_triangle())

        tr = Triangle(Point(0, 1), Point(0, 3), Point(0, 6))
        self.assertFalse(tr.is_triangle())

        tr = Triangle(Point(0, 1.23), Point(0, 1.23), Point(0, 6))
        self.assertFalse(tr.is_triangle())

        tr = Triangle(Point(0, 0), Point(0, 0), Point(0, 0))
        self.assertFalse(tr.is_triangle())


class TestTaskSolverMethods(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
