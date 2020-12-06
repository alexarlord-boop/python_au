import unittest
from hexadecimal.hex import Node, HexNumber, Solution


class TestHexNumber(unittest.TestCase):
    def test_str(self):
        test_num = HexNumber("1FF")
        self.assertEqual(str(test_num), "1FF")

        test_num = HexNumber("1")
        self.assertEqual(str(test_num), "1")

        test_num = HexNumber("")
        self.assertEqual(str(test_num), "")

        test_num = HexNumber("AFF")
        self.assertEqual(str(test_num), "AFF")

        test_num = HexNumber("123")
        self.assertEqual(str(test_num), "123")

        with self.assertRaises(ValueError):
            test_num = HexNumber("fd")

        with self.assertRaises(ValueError):
            test_num = HexNumber("12f")

        with self.assertRaises(ValueError):
            test_num = HexNumber("Fad")
