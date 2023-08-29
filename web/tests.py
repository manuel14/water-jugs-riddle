import unittest

from .models import Solution


class TestSolution(unittest.TestCase):
    def test_solution_ok(self):
        sol = Solution(5, 3, 4)
        self.assertEquals(len(sol.minSteps()), 6)

    def test_no_solution(self):
        sol = Solution(6, 4, 3)
        self.assertEquals(len(sol.minSteps()), 0)


if __name__ == '__main__':
    unittest.main()
