import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(20, 5), 25)
        self.assertEqual(katas.add(-5, 5), 0)
        self.assertEqual(katas.add(-2, -2), -4)

    def test_multiply(self):
        self.assertEqual(katas.multiply(10, 5), 50)
        self.assertEqual(katas.multiply(-1, 1), -1)
        self.assertEqual(katas.multiply(-1, -1), 1)

    def test_power(self):
        self.assertEqual(katas.power(2, 3), 8)

    def test_factorial(self):
        self.assertEqual(katas.factorial(6), 720)
        self.assertEqual(katas.factorial(10), 3628800)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(9), 21)
        self.assertEqual(katas.fibonacci(11), 55)


if __name__ == '__main__':
    unittest.main()
