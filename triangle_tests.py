import unittest
from triangle import Point, Triangle, TaskSolver


class TestPointAddMethod(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Point(2, 3) + Point(3, 3), (5, 6))
        self.assertEqual(Point(2.5, 3.0) + Point(1.2, 3.2), (3.7, 6.2))
        self.assertEqual(Point(-2, -3) + Point(2, 3), (0, 0))


class TestTriangleMethods(unittest.TestCase):
    pass


class TestTaskSolverMethods(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
