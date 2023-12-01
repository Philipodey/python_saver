import unittest


class MyTestCase(unittest.TestCase):
    def test_nokia_function(self):
        
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
