import unittest
from porcodio.porcodio import get_porcodio

class TestGetPorcodio(unittest.TestCase):
    def test_get_porcodio(self):
        print(get_porcodio())

if __name__ == '__main__':
    unittest.main()