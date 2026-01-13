"""
This script plots bar graphs for execution time, CPI, and cache miss rates as outputed by the simulations in Part 2, Step 1. 
"""
import matplotlib.pyplot as plt
import numpy as np

benchmarks = ["bzip", "hmmer", "libm", "mcf", "sjeng"]
exec_time = [0.083982, 0.059396, 0.174671, 0.064955, 0.513528]
cpi = [1.679650, 1.187917, 3.493415, 1.299095, 10.270554]
l1d_miss = [0.014798, 0.001637, 0.060972, 0.002108, 0.121831]
l1i_miss = [0.000077, 0.000221, 0.000094, 0.023612, 0.000020]
l2_miss = [0.282163, 0.077760, 0.999944, 0.055046, 0.999972]

# Bar graph for Execution Time and CPI
def bar_graph(values, title, ylabel, color, rotation=0):
    plt.figure(figsize=(7, 4))
    bars = plt.bar(benchmarks, values, color=color,edgecolor='black', linewidth=1.2)
    height = plt.ylim(0, max(values) * 1.1) # y-axis height just higher than max y value

    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom', fontsize=9)
        
    plt.title(title, fontweight='bold')
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()

# Bar graph for Miss Rates
def miss_graph(l1d_miss, l1i_miss, l2_miss):
    plt.figure(figsize=(10, 5))
    x = np.arange(len(benchmarks))
    width = 0.25

    bars_l1d = plt.bar(x - width, l1d_miss, width, label='L1D', color='red', edgecolor='black', linewidth=1.2)
    bars_l1i = plt.bar(x, l1i_miss, width, label='L1I', color='green', edgecolor='black', linewidth=1.2)
    bars_l2 = plt.bar(x + width, l2_miss, width, label='L2', color='blue', edgecolor='black', linewidth=1.2)
    height = plt.ylim(0, max(max(l1d_miss), max(l1i_miss), max(l2_miss)) * 1.1) # y-axis height just higher than max y value

    bars = [bars_l1d, bars_l1i, bars_l2]

    # Add value labels on top of bars
    for bar_group in bars:
        for bar in bar_group:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom', fontsize=9)
        
    plt.xlabel('Benchmark')
    plt.ylabel('Miss Rate')
    plt.title('Cache Miss Rates', fontweight='bold')
    plt.xticks(x, benchmarks)
    plt.legend()
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()

    plt.show()


# Execution Time
bar_graph(exec_time, "Execution Time", "Seconds", 'orange')

# CPI
bar_graph(cpi, "CPI", "Cycles per Instruction", 'purple')

# Miss Rates - grouped bar chart
miss_graph(l1d_miss, l1i_miss, l2_miss)