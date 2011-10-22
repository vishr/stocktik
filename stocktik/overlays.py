"""
Created on Sep 22, 2011

@author: Vishal Rana
"""

import logging
import numpy as np

logger = logging.getLogger(__name__)

def sma(close, n):
    """
    Compute simple moving average for n period.
    """
    w = np.ones(n) / n
    return np.convolve(close, w, mode="valid")

def ema(close, n):
    """
    Compute exponential moving average for n period.
    """
    # set the (n-1)th ema to sma, after that use the formula
    ema = [close[:n - 1].sum() / (n - 1)]
    a = 2. / (n + 1)
    for i, c in enumerate(close[n:]):
        ema.append(((c - ema[i]) * a) + ema[i])
    return np.asarray(ema)
