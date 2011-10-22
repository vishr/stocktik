"""
Created on Oct 22, 2011

@author: Vishal Rana
"""

from stocktik import overlays as o
import unittest

class OverlaysTest(unittest.TestCase):
    def setUp(self):
        self.close = [
            22.27,
            22.19,
            22.08,
            22.17,
            22.18,
            22.13,
            22.23,
            22.43,
            22.24,
            22.29,
            22.15,
            22.39,
            22.38,
            22.61,
            23.36,
            24.05,
            23.75,
            23.83,
            23.95,
            23.63
        ]

    def test_sma(self):
        expected = [
            22.22,
            22.21,
            22.23,
            22.26,
            22.3,
            22.42,
            22.61,
            22.76,
            22.9,
            23.08,
            23.21
        ]
        self.assertEqual(expected, [round(i, 2) for i in o.sma(self.close, 10)])
        
    def test_ema(self):
        expected = [
            22.21,
            22.2,
            22.24,
            22.26,
            22.33,
            22.51,
            22.79,
            22.97,
            23.12,
            23.27,
            23.34
        ]
        self.assertEqual(expected, [round(i, 2) for i in o.ema(self.close, 10)])
