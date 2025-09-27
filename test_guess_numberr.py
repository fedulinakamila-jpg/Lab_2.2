import unittest
from typing import Tuple

from guess_numberr import guess_number


class TestMath(unittest.TestCase):
    def test_start(self):  # угадать первое число
        self.assertEqual(guess_number(1, [1, 2, 3, 4, 5], algorithm="brute force"), (1, 1))

    def test_mid(self):  # угадать число по середине
        self.assertEqual(guess_number(3, [1, 2, 3, 4, 5], algorithm="brute force"), (3, 3))

    def test_end(self):  # угадать последнее число
        self.assertEqual(guess_number(5, [1, 2, 3, 4, 5], algorithm="brute force"), (5, 5))

    def test_unsorted(self):  # неотсортированный список
        self.assertIsInstance(guess_number(3, [5, 1, 3, 4, 2], algorithm="binary"), Tuple)

    def test_empty(self):  # пустой список
        with self.assertRaises(ValueError) as cm:
            guess_number(1, [], algorithm="brute force")
        self.assertEqual(str(cm.exception), "Число не найдено")

    def test_single(self):  # единственное значение
        self.assertEqual(guess_number(1, [1], algorithm="brute force"), (1, 1))

    def test_not_found(self):  # число отсутствует в списке
        with self.assertRaises(ValueError):
            guess_number(2, [1], algorithm="brute force")

    def test_duplicat(self):  # повторяющиеся числа
        self.assertEqual(guess_number(3, [1, 2, 3, 3, 3], algorithm="brute force"), (3, 3))


if __name__ == '__main__':
    unittest.main()
