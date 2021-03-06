"""
Copyright (c) 2014 Marshall Farrier
license http://opensource.org/licenses/MIT

@author: Arka Dasgupta
@contact: arkadasgupta@gmail.com
@since: 2016-01-17
@summary: Integration Test for data retrieval from yahoo
"""

import unittest
import pandas as pd
import pynance as pn


class TestData(unittest.TestCase):
    def setUp(self):
        self.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
        self.index = pd.date_range('2014-03-03', periods=5)

        # Adjusted close values can change. So ignore them for tests
        self.test_data_aapl = pd.DataFrame([[5.23419991e+02, 5.30650009e+02, 5.22809990e+02, 5.27760010e+02,
                                             5.96953000e+07, 0],
                                            [5.30999977e+02, 5.32640015e+02, 5.27769997e+02, 5.31239983e+02,
                                             6.47850000e+07, 0],
                                            [5.30919975e+02, 5.34750023e+02, 5.29129974e+02, 5.32360008e+02,
                                             5.00157000e+07, 0],
                                            [5.32789978e+02, 5.34440002e+02, 5.28099991e+02, 5.30749985e+02,
                                             4.63722000e+07, 0],
                                            [5.31090019e+02, 5.31980026e+02, 5.26050011e+02, 5.30440018e+02,
                                             5.51824000e+07, 0]], self.index, self.columns)

    def test_pynance_data_get(self):
        pynance_data = pn.data.get('AAPL', '2014-03-03', '2014-03-07')
        self.assertEqual(pynance_data.shape, self.test_data_aapl.shape)
        for session, test_session in zip(pynance_data.values, self.test_data_aapl.values):
            # ignore adjusted close column in pandas data
            for value, test_value in zip(session[:-1], test_session):
                self.assertAlmostEqual(value, test_value)


if __name__ == '__main__':
    unittest.main()
