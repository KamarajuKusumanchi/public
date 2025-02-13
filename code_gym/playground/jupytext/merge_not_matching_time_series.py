# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# reproduce https://towardsdatascience.com/how-to-merge-not-matching-time-series-with-pandas-7993fcbce063 - How to Merge “Not Matching” Time Series with Pandas

import pandas as pd

A = pd.DataFrame(
    {
        "time": [
            pd.Timestamp("2020-02-01 00:00:00"),
            pd.Timestamp("2020-02-01 00:00:03"),
            pd.Timestamp("2020-02-01 00:00:06"),
            pd.Timestamp("2020-02-01 00:00:09"),
            pd.Timestamp("2020-02-01 00:00:12"),
        ],
        "name": ["GGG", "GGG", "GGG", "FFF", "FFF"],
        "values_a": [1, 2, 5, 4, 9]
    }
)
A

B = pd.DataFrame(
    {
        "time": [
            pd.Timestamp("2020-02-01 00:00:00"),
            pd.Timestamp("2020-02-01 00:00:04"),
            pd.Timestamp("2020-02-01 00:00:08"),
            pd.Timestamp("2020-02-01 00:00:12"),
            pd.Timestamp("2020-02-01 00:00:16"),
        ],
        "name": ["GGG", "GGG", "GGG", "FFF", "FFF"],
        "values_b": [5, 8, 7, 2, 9]
    }
)
B

pd.merge_asof(A, B, on='time', by='name', tolerance=pd.Timedelta('2s'))

pd.merge_asof(A, B, on='time', by='name')

pd.merge_asof(A, B, on='time', by='name', allow_exact_matches=False)


