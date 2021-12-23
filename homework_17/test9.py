import unittest
from arithmetic import arithmetic
import os
import logger


class HomeWorkTest(unittest.TestCase):

    def test_plus(self):
        "test plus"
        number = arithmetic(7, 10, "+")
        logger.log.debug("check start")
        self.assertEqual(number, 7+10)

    def test_minus(self):
        "test minus"
        number = arithmetic(7, 10, "-")
        logger.log.info("check log info")
        self.assertEqual(number, 7-10)

    def test_divide(self):
        "test divide"
        number = arithmetic(7, 10, "/")
        logger.log.warning("check warning")
        self.assertEqual(number, 7/10)

    def test_multiply(self):
        "test multiply"
        number = arithmetic(7, 10, "*")
        logger.log.error("check error")
        self.assertEqual(number, 7*10)

    @unittest.skip
    def test_divide_copy(self):
        "skip test divide"
        number = arithmetic(7, 10, "/")
        self.assertEqual(number, 7/10)

    @unittest.skipIf(os.name != "linux", "test for Linux")
    def test_multiply_copy(self):
        "skipif test multiply"
        number = arithmetic(7, 10, "*")
        self.assertEqual(number, 7*10)

    @unittest.expectedFailure
    def test_divide_zero(self):
        "test zero devide"
        number = arithmetic(7, 0, "/")
        self.assertEqual(number, 7/0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
