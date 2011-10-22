"""
Created on Sep 21, 2011

@author: Vishal Rana
"""

from overlays import sma, ema
import logging
import numpy as np

logger = logging.getLogger(__name__)

def macd(close, nsignal=9):
    emaf = ema(close, 12)
    emas = ema(close, 26)
    macd = emaf[-emas.size:] - emas
    signal = ema(macd, nsignal)
    histogram = macd[-signal.size:] - signal
    return macd, signal, histogram

def rsi(close, n=14):
    """
    Cutler's relative strength index
    """
    diff = close[1:] - close[:-1]
    # up trend close
    uclose = diff.copy()
    uclose[uclose <= 0] = 0
    # down trend close
    dclose = diff
    dclose[dclose >= 0] = 0
    dclose = np.abs(dclose)
    rsi = 100 * sma(uclose, n) / (sma(uclose, n) + sma(dclose, n))
    # replace NaN
    rsi[np.isnan(rsi)] = 100
    return rsi

def cci(high, low, close, n=20):
    tp = (high + low + close) / 3.
    sma_tp = sma(tp, n)
    size = sma_tp.size
    # stride array
    tp_strided = np.zeros(shape=(size, n))
    for i in range(n):
        tp_strided[:, i] = tp[i:size + i]
    md = np.abs(tp_strided - sma_tp[:, None]).sum(axis=1) / n
    return (tp[-sma_tp.size:] - sma_tp) / (.015 * md)

def stochastic(high, low, close, x=14, y=3):
    size = high.size - x + 1
    # stride arrays
    high_strided = np.zeros(shape=(size, x))
    low_strided = np.zeros(shape=(size, x))
    close_strided = np.zeros(shape=(size, x))
    for i in range(x):
        high_strided[:, i] = high[i:size + i]
        low_strided[:, i] = low[i:size + i]
        close_strided[:, i] = close[i:size + i]
    lmin = low_strided.min(axis=1)
    hmax = high_strided.max(axis=1)
    kfast = 100 * (close_strided[:, -1] - lmin) / (hmax - lmin)
    dfast = sma(kfast, y);
    kslow = dfast;
    dslow = sma(kslow, y)
    return kfast, dfast, kslow, dslow
