# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pandas as pd
pd.set_option('display.max_columns', None, 'display.max_rows', None)
import yahooquery as yq

# To find out where a particular item is, use https://yahooquery.dpguthrie.com/guide/ticker/modules/

costco = yq.Ticker("COST")

costco.summary_detail

costco.asset_profile

costco.summary_detail['COST'].keys()

costco.summary_detail['COST']['marketCap']/1e9

costco.balance_sheet()

costco.income_statement(frequency='q')

mask = costco.income_statement(frequency='q')['periodType'] == '3M'
costco.income_statement(frequency='q')[mask]

brka = yq.Ticker('BRK-A')
brkb = yq.Ticker('BRK-B')

brkb.balance_sheet(frequency='q').columns

brkb.income_statement(frequency='q')

mask = brkb.income_statement(frequency='q')['periodType'] == '3M'
brkb.income_statement(frequency='q')[mask]

brkb.cash_flow(frequency='q').columns

brkb.cash_flow(frequency='q')

import os
os.getcwd()


