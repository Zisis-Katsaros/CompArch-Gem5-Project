"""
This script plots bar graphs for CPI values as outputed by tests I(a) trough III(b) in Part 2, Step 2.
"""

import matplotlib.pyplot as plt
import numpy as np

# Data outputed in the results_table.txt file 
data = {
    'lbm': {
        'Ia': 3.493415,
        'Ib': 3.493415,
        'Ic': 3.493415,
        'IIa': 3.493293,
        'IIb': 3.493293,
        'IIc': 3.493293,
        'IIIa': 2.581299,
        'IIIb': 1.990648,
    },
    'sjeng': {
        'Ia': 10.270554,
        'Ib': 10.270520,
        'Ic': 10.270520,
        'IIa': 10.270037,
        'IIb': 10.270894,
        'IIc': 10.270890,
        'IIIa': 6.799471,
        'IIIb': 5.175719,
    },
    'bzip': {
        'Ia': 1.679650,
        'Ib': 1.650416,
        'Ic': 1.650388,
        'IIa': 1.664058,
        'IIb': 1.657795,
        'IIc': 1.665368,
        'IIIa': 1.666573,
        'IIIb': 1.661958,
    },
    'mcf': {
        'Ia': 1.299095,
        'Ib': 1.298527,
        'Ic': 1.155171,
        'IIa': 1.155172,
        'IIb': 1.155067,
        'IIc': 1.155172,
        'IIIa': 1.330534,
        'IIIb': 1.298444,
    },
    'hmmer': {
        'Ia': 1.187917,
        'Ib': 1.186170,
        'Ic': 1.185839,
        'IIa': 1.187564,
        'IIb': 1.187566,
        'IIc': 1.187564,
        'IIIa': 1.181978,
        'IIIb': 1.179864,
    },
}

# Color map so that tests are color coded
color_map = {
    'Ia': 'red', 
    'Ib': 'red', 
    'Ic': 'red',
    'IIa': 'green', 
    'IIb': 'green', 
    'IIc': 'green',
    'IIIa': 'blue', 
    'IIIb': 'blue',
}

# Loop through each benchmark and create bar graph
for benchmark, tests in data.items():
    plt.figure(figsize=(10, 6))
    
    test_names = list(tests.keys()) # get test names
    cpi_values = list(tests.values()) # get CPI
    colors = [color_map[test] for test in test_names] 
    
    bars = plt.bar(test_names, cpi_values, color=colors, edgecolor='black', linewidth=1.2)
    
    plt.xlabel('Test', fontsize=12, fontweight='bold')
    plt.ylabel('CPI', fontsize=12, fontweight='bold')
    plt.title(f'{benchmark.upper()} - CPI by Test', fontsize=14, fontweight='bold')
    plt.ylim(0, max(cpi_values) * 1.1) # y-axis height just higher than max CPI
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom', fontsize=9)
    
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='red', edgecolor='black', label='Test I (L1 size)'),
        Patch(facecolor='green', edgecolor='black', label='Test II (Assoc.)'),
        Patch(facecolor='blue', edgecolor='black', label='Test III (Cache line size)'),
    ]
    plt.legend(handles=legend_elements, loc='lower right', fontsize=10)
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.show()

