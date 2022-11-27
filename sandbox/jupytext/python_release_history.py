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

# Use this file for experimentation. For integrating it into an applicaiton, checkout rutils/python3/src/release_history.py -> python_release_history()

url = 'https://www.python.org/doc/versions/'

# +
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import pandas as pd

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)


# +
# We want to parse lines such as
# <div class="section" id="python-documentation-by-version">
# ...
# <li><a class="reference external" href="https://docs.python.org/release/3.11.0/">Python 3.11.0</a>, documentation released on 24 October 2022.</li>
# ...
# </div>
div = soup.find('div', attrs={'id': "python-documentation-by-version"})
# print(div)
release_data = []
for link in div.findAll('li'):
    # Sample output:
    # link = '<li><a class="reference external" href="https://docs.python.org/release/3.11.0/">Python 3.11.0</a>, documentation released on 24 October 2022.</li>'
    # x.contents = ['Python 3.11.0']
    # release_tag = '3.11.0'
    # y = ', documentation released on 24 October 2022.'
    # s = '24 October 2022'
    # release_date = '2022-10-24'
    
    # print(link)
    x = link.find('a', attrs={'href': re.compile('^https*://')})
    # print(x.contents)
    matches = re.search('Python (.*)$', x.contents[0])
    release_tag = matches.group(1)
    # print(release_tag)
    y = link.contents[1].replace('\n', ' ')
    # print(y)
    matches = re.search(', documentation released on (\d* .* \d*)\.?$', y)
    s = matches.group(1)
    release_date = datetime.strptime(s, '%d %B %Y').date()
    release_data.append((release_date, release_tag))
    
# print(release_data)
# -

releases = pd.DataFrame(release_data, columns=['release_date', 'release_tag'])
releases


