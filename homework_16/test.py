import unittest
import hw5


class HomeWorkTest5(unittest.TestCase):

    def test_1(self):
        """test is title"""
        out = hw5.homework_1("hello my name is")
        exp = "Hello My Name Is"
        self.assertEqual(out, exp)

    def test_2(self):
        """is this dict or no"""
        out = hw5.homework_2("name=Amanda=sssss&age=32&&salary=1500&currency=quro")
        self.assertIsInstance(out, dict)

    def test_3(self):
        """test len"""
        out = hw5.homework_2("name=Amanda=sssss&age=32&&salary=1500&currency=quro")
        self.assertEqual(len(out), 4)

    def test_4(self):
        """low case check"""
        out = hw5.homework_3("TEST")
        self.assertEqual(out, out.lower())


if __name__ == "__main__":
    unittest.main()

