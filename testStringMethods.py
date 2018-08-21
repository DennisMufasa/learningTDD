# import unittest
import unittest


# create a testcase by making a class that subclasses unittest.TestCase
class TestStringMethods(unittest.TestCase):
    # making individual tests whose names must start with test for unit test to know they are tests
    def test_upper(self):
        # testing if upper returns an uppercase string
        self.assertEqual('foo'.upper(), 'FOO') # accepts 2 arguments. the two are checked for equality


    # another test for isUpper()
    def test_isUpper(self):
        # checks whether isUpper returns true for uppercase string
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    # another test for split
    def test_split(self):
        s = 'dennis mufasa'
        self.assertEqual(s.split(), ['dennis', 'mufasa'])
#         to make sure that the test fails if the s.split() seperator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()




