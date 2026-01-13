"""
This script plots bar graphs for CPI values as outputed by tests IV(a) trough IV(e) in Part 2, Step 2.
"""

import matplotlib.pyplot as plt
import numpy as np

# Data outputed in the results_table.txt file 
data = {
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

# Color map so that tests are color coded
color_map = {
    'IVa': 'red', 
    'IVb': 'green', 
    'IVc': 'blue',
    'IVd': 'orange',
    'IVe': 'purple',
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
        Patch(facecolor='red', edgecolor='black', label='Test IV(a)'),
        Patch(facecolor='green', edgecolor='black', label='Test IV(b)'),
        Patch(facecolor='blue', edgecolor='black', label='Test IV(c)'),
        Patch(facecolor='orange', edgecolor='black', label='Test IV(d)'),
        Patch(facecolor='purple', edgecolor='black', label='Test IV(e)'),
    ]
    plt.legend(handles=legend_elements, loc='lower right', fontsize=10)
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.show()
