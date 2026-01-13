import matplotlib.pyplot as plt
import numpy as np

# Data outputed in the results_table.txt file 
cpi_values = {
    'lbm': {
        'IVa': 1.989308,
        'IVb': 2.576600,
        'IVc': 2.576597,
        'IVd': 1.989308,
        'IVe': 1.989308,
    },
    'sjeng': {
        'IVa': 5.171443,
        'IVb': 6.795891,
        'IVc': 6.795093,
        'IVd': 5.171385,
        'IVe': 5.171287,
    },
    'bzip': {
        'IVa': 1.601742,
        'IVb': 1.624832,
        'IVc': 1.608267,
        'IVd': 1.600096,
        'IVe': 1.631287,
    },
    'mcf': {
        'IVa': 1.169147,
        'IVb': 1.123369,
        'IVc': 1.122884,
        'IVd': 1.107630,
        'IVe': 1.108791,
    },
    'hmmer': {
        'IVa': 1.177702,
        'IVb': 1.181154,
        'IVc': 1.179780,
        'IVd': 1.177320,
        'IVe': 1.178316,
    },
}

parameters = {
    'IVa': {
        'Size_L1': 160,
        'Size_L2': 4000,
        'Assoc_L1': 4,
        'Assoc_L2': 8,
        'Cache_Line_Size': 256,
    },
    'IVb': {
        'Size_L1': 128,
        'Size_L2': 4000,
        'Assoc_L1': 8,
        'Assoc_L2': 16,
        'Cache_Line_Size': 128,
    },
    'IVc': {
        'Size_L1': 160,
        'Size_L2': 4000,
        'Assoc_L1': 4,
        'Assoc_L2': 16,
        'Cache_Line_Size': 128,
    },
    'IVd': {
        'Size_L1': 160,
        'Size_L2': 4000,
        'Assoc_L1': 4,
        'Assoc_L2': 16,
        'Cache_Line_Size': 256,
    },
    'IVe': {
        'Size_L1': 128,
        'Size_L2': 4000,
        'Assoc_L1': 8,
        'Assoc_L2': 16,
        'Cache_Line_Size': 256,
    },
}


def cost(parameters, cpi):
    a=0.4
    b=0.1
    c=0.2
    d=0.3
    e=512
    f=2
    norm = 100 # so that cost isn't unnecessarily large
    return (a * parameters['Size_L1'] +
                   b * parameters['Size_L2'] +
                   c * parameters['Assoc_L1']**2 +
                   d * parameters['Assoc_L2'] +
                   e / parameters['Cache_Line_Size']) * (cpi)**f / norm

# Calculate average CPI across all benchmarks for each test
average_cpi = {}
for test in parameters.keys():
    total_cpi = 0
    for benchmark in cpi_values.keys():
        total_cpi += cpi_values[benchmark][test]
    average_cpi[test] = total_cpi / len(cpi_values)

# Calculate cost of each test
test_costs = {}
for test, params in parameters.items():
    test_costs[test] = cost(params, average_cpi[test])

# Print costs
for test, cost_value in test_costs.items():
    print(f"Test {test} - Cost: {cost_value:.2f}")

print(f"Most successful design: {min(test_costs, key=test_costs.get)}")
