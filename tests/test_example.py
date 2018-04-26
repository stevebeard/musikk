import unittest

class TestStringMethods(unittest.TestCase):
    
    def testUpper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def testIsUpper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()