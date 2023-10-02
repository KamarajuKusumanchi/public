# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pandas_datareader.data as web

# With pandas_datareader 0.10.0, I am getting
#   TypeError: string indices must be integers, not 'str'
# when running something like
#   data = web.get_data_yahoo('SPY', start='2023-09-02', end='2023-10-02')
# To work around this, "hijack" pandas_datareader.data.get_data_yahoo() method to use yfinance.
# This has two advantages:
#   1. It will return data in the same format as pandas_datareader's get_data_yahoo()
#   2. It is faster
# Ref:
#   * https://github.com/ranaroussi/yfinance

import yfinance as yf
yf.pdr_override()

data = web.get_data_yahoo('SPY', start='2023-09-02', end='2023-10-02')
# -
data



