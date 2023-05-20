import unittest

from flask_rabotaem5_task3.py import BlockErrors


class BlockErrorsTestCase(unittest.TestCase):
    def test_ignore_error(self):
        with BlockErrors({ZeroDivisionError}):
            a = 1 / 0
        self.assertTrue(True)

    def test_propagate_error(self):
        with self.assertRaises(TypeError):
            with BlockErrors({ZeroDivisionError}):
                a = 1 / '0'

    def test_ignore_inner_error(self):
        with BlockErrors({TypeError}):
            with BlockErrors({ZeroDivisionError}):
                a = 1 / '0'
            self.assertTrue(True)

    def test_ignore_child_errors(self):
        with BlockErrors({Exception}):
            a = 1 / '0'
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()