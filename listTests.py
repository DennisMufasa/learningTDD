# import unittest & arrays.py
import unittest
import arrays

#create testCases
class ListTests(unittest.TestCase):
    # test output type
    def test_outputType(self):
        paramType = arrays.reversal([1, 2, 3])
        self.assertTrue(isinstance(paramType, list))

    def test_output(self):
        call = arrays.reversal([1,2,3])
        self.assertEqual(call[0], 3)  #checks whether the first list item is 3 as it should be after reversal



if __name__ == '__main__':
    unittest.main()

