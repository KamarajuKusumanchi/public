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

# +
# From https://www.berkshirehathaway.com/news/aug0622.pdf
# -

def eps_by_class(a_shares, b_shares, operating_earnings, net_earnings):
    result = {}
    result['net_eps_class_A'] = net_earnings / a_shares
    result['net_eps_class_B'] = net_earnings / b_shares
    result['operating_eps_class_A'] = operating_earnings / a_shares
    result['operating_eps_class_B'] = operating_earnings / b_shares
    return result


# for H1 2022
data = {'a_shares': 1472628, 'b_shares': 2208942539,
        'operating_earnings': 16323 * 1e6, 'net_earnings': -38295 * 1e6}
eps_h1_2022 = eps_by_class(data['a_shares'], data['b_shares'], data['operating_earnings'], data['net_earnings'])
print(result)

# for Q2 2022
data = {'a_shares': 1470577, 'b_shares': 2205865262,
        'operating_earnings': 9283 * 1e6, 'net_earnings': -43755 * 1e6}
eps_q2_2022 = eps_by_class(data['a_shares'], data['b_shares'], data['operating_earnings'], data['net_earnings'])
print(result)

last_price = 267.80  # asof 2022-10-10
pe = last_price / eps_q2_2022['operating_eps_class_B']
print(pe)


