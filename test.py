import unittest


class FirstTests(unittest.TestCase):

    def test_runs(self):
        assert 1 == 1

if __name__ == '__main__':
    unittest.main()