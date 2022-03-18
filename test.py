import unittest
from simulate_leveraged_etf import simulate_leveraged_etf


class FirstTests(unittest.TestCase):

    def test_runs(self):
        obj = simulate_leveraged_etf("QQQ", "TQQQ")
        assert obj.etf_ticker == "QQQ"
        assert obj.leverage_ticker == "TQQQ"
        obj.build()


if __name__ == '__main__':
    unittest.main()
