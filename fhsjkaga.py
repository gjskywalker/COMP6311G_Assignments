import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# 1. Data Preparation
# Note: Values are taken directly from your provided logs.
data = {
    'Structure': [
        'QuadTree', 'QuadTree', 'QuadTree', 'QuadTree', 'QuadTree',
        'R-Tree', 'R-Tree', 'R-Tree', 'R-Tree', 'R-Tree',
        'Z-Order', 'Packed R-Tree', 'Packed R-Tree', 'Packed R-Tree', 'Packed R-Tree',
        'R*-Tree', 'R*-Tree', 'R*-Tree', 'R*-Tree', 'R*-Tree',
        'GeoPandas', 'GeoPandas', 'GeoPandas', 'GeoPandas', 'GeoPandas'
    ],
    'Metric': [
        'Build Time (s)', 'Memory (MB)', 'Q1: Point (s)', 'Q2: Poly (s)', 'Q3: k-NN (s)',
        'Build Time (s)', 'Memory (MB)', 'Q1: Point (s)', 'Q2: Poly (s)', 'Q3: k-NN (s)',
        'Build Time (s)', 'Memory (MB)', 'Q1: Point (s)', 'Q2: Poly (s)', 'Q3: k-NN (s)',
        'Build Time (s)', 'Memory (MB)', 'Q1: Point (s)', 'Q2: Poly (s)', 'Q3: k-NN (s)',
        'Build Time (s)', 'Memory (MB)', 'Q1: Point (s)', 'Q2: Poly (s)', 'Q3: k-NN (s)'
    ],
    'Value': [
        # QuadTree
        121.6920, 406.28, 0.0044, 0.2838, 125.8443,
        # R-Tree
        80.9119, 451.88, 0.0063, 0.1568, 123.7106,
        # Packed R-Tree
        59.1574, 423.79, 0.0051, 0.1636, 124.0229,
        # R*-Tree
        122.8220, 448.12, 0.0056, 0.1664, 123.1764,
        # GeoPandas
        0.0014, 358.21, 0.0294, 0.0191, 24.4057
    ]
}

df = pd.DataFrame(data)

# 2. Plotting Configuration
# Adjusted figsize to 15:3 ratio (Width 15, Height 3)
plt.figure(figsize=(17, 6))
sns.set_theme(style="whitegrid")

# Custom color palette
palette = {
    'QuadTree': '#409cd8',      # Blue
    'R-Tree': '#ffbd00',        # Yellow
    'Packed R-Tree': '#bbe7bb', # Light Green
    'R*-Tree': '#ffeab0',       # Light Pink
    'GeoPandas': '#e86252'      # Red
}

# Define explicit hue order to ensure we can target GeoPandas correctly
hue_order = ['QuadTree', 'R-Tree', 'Packed R-Tree', 'R*-Tree', 'GeoPandas']

# Create Bar Plot
chart = sns.barplot(
    data=df,
    x='Metric',
    y='Value',
    hue='Structure',
    hue_order=hue_order,
    palette=palette,
    edgecolor='black',
    linewidth=1
)

# Apply hatching to GeoPandas bars
# GeoPandas is the last item in hue_order, so it corresponds to the last container
# Note: chart.containers contains patches for each hue level
geopandas_container = chart.containers[4] 
for bar in geopandas_container:
    bar.set_hatch('///')

# 3. Formatting
# Logarithmic scale is crucial due to the mix of MB (300+) and fast queries (0.001s)
plt.yscale('log')
plt.ylim(0.001, 100000)

# Labels and Titles
plt.title('Comprehensive Performance Comparison: Custom Indices vs. GeoPandas', fontsize=20, fontweight='bold', pad=20)
plt.ylabel('Value (Log Scale)\n[Seconds for Time / MB for Memory]', fontsize=18)
plt.xlabel('Evaluation Metrics', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.grid(axis='y', linestyle='--', color='black', alpha=1.0, zorder=0)

# Legend placement
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1), ncol=5, frameon=False, fontsize=16)

plt.tight_layout()

# Save or Show
plt.savefig('performance_comparison.pdf', dpi=300, bbox_inches='tight')
plt.show()