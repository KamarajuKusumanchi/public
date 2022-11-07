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

# From https://www.berkshirehathaway.com/news/nov0522.pdf

def eps_by_class(a_shares, b_shares, operating_earnings, net_earnings):
    result = {}
    result['net_eps_class_A'] = net_earnings / a_shares
    result['net_eps_class_B'] = net_earnings / b_shares
    result['operating_eps_class_A'] = operating_earnings / a_shares
    result['operating_eps_class_B'] = operating_earnings / b_shares
    return result


# for first nine months of 2022
data = {'a_shares': 1470714, 'b_shares': 2206070294,
        'operating_earnings': 24084 * 1e6, 'net_earnings': -40983 * 1e6}
eps_first_9_months_2022 = eps_by_class(data['a_shares'], data['b_shares'], data['operating_earnings'], data['net_earnings'])
print(eps_first_9_months_2022)

# for Q3 2022
data = {'a_shares': 1466946, 'b_shares': 2200419462,
        'operating_earnings': 7761 * 1e6, 'net_earnings': -2688 * 1e6}
eps_q3_2022 = eps_by_class(data['a_shares'], data['b_shares'], data['operating_earnings'], data['net_earnings'])
print(eps_q3_2022)

last_price = 287.47  # asof 2022-11-04
pe_est1 = last_price / (4 * eps_q3_2022['operating_eps_class_B'])
print(pe_est1)
pe_est2 = last_price / ((4/3) * eps_first_9_months_2022['operating_eps_class_B'])
print(pe_est2)


