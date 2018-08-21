# import the unittest module and file to test
import unittest
import inc_dec


# create unittests by creating a class that subclasses unittest.TestCase\
class TestIncrementDecrement(unittest.TestCase):
    # individual test for increment
    def test_inc(self):
        self.assertEqual(inc_dec.increment(2), 3)

    # another individual test for decrement
    def test_dec(self):
        self.assertEqual(inc_dec.decrement(3), 2)


if __name__ == '__main__':
    unittest.main()

