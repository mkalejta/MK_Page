import unittest
from test_function import get_formatted_name


class MyTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('mikolaj', 'kalejta')
        self.assertEqual(formatted_name, 'Mikolaj Kalejta')


if __name__ == '__main__':
    unittest.main()
