import unittest

class testStringSame(unittest.TestCase):

    def test_equal(self):
        word = 'hello'
        self.assertEqual(word, 'hello')


if __name__ == '__main__':
    unittest.main()