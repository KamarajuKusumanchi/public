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

import pandas as pd
df_things = pd.DataFrame({
    'A': ['al1', 'al1', 'al1', 'al2', 'al3', 'al1', 'al3'],
    'B': ['bal1', 'bal1', 'bal2', 'bal2', 'bal3', 'bal2', 'bal3'],
    'C': ['cal1', 'cal1', 'cal2', 'cal2', 'cal3', 'cal3', 'cal3'],
    'CLASS': ['Ship', 'Ship', 'Ship', 'Cow', 'Car', 'Car', 'Car']
})
print(df_things)

df_B = df_things.groupby('CLASS').B.value_counts()
print(df_B)

df_reduced = df_things.groupby(['CLASS']).filter(lambda grp: grp['B'].nunique() > 1)
print(df_reduced)

df_reduced.groupby(['CLASS'])['B'].value_counts()


