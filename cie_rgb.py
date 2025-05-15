import numpy as np
import matplotlib.pyplot as plt
from colour.plotting import plot_chromaticity_diagram_CIE1931
from matplotlib.lines import Line2D

# Updated xy coordinates
xy_coords = np.array([
    [0.2830, 0.2789],  # Light - A
    [0.3478, 0.3545],  # Dilution - B
    [0.3897, 0.3635]   # Milk - C
])

point_labels = ['Light - A', 'Dilution - B', 'Milk - C']
point_labels2= ['A', 'B', 'C']
colors = ['red', 'green', 'blue']

# Plot CIE 1931 diagram
plot_chromaticity_diagram_CIE1931(standalone=False)

# Plot each point with unique color and label (only point labels on plot)
for (x, y), label, color in zip(xy_coords, point_labels2, colors):
    plt.scatter(x, y, color=color, s=2)
    plt.text(x + 0.005, y, label, fontsize=9, fontweight='normal', color=color)
    plt.plot([x, x], [-0.1, y], color=color, linestyle='dashed', linewidth=0.4)
    plt.plot([-0.15, x], [y, y], color=color, linestyle='dashed', linewidth=0.4)

# Create legend labels with coordinates
legend_labels_with_coords = [
    f'{label} ({x:.4f}, {y:.4f})' for label, (x, y) in zip(point_labels, xy_coords)
]

# Create legend handles matching colors
legend_handles = [
    Line2D([0], [0], marker='o', color='w', label=lbl,
           markerfacecolor=color, markersize=10)
    for lbl, color in zip(legend_labels_with_coords, colors)
]

plt.legend(handles=legend_handles, title='Samples')

plt.title('CIE with Samples and Coordinates')

plt.show()

# Existing point plotting loop
for (x, y), label, color in zip(xy_coords, point_labels2, colors):
    plt.scatter(x, y, color=color, s=2)
    plt.text(x + 0.005, y, label, fontsize=9, fontweight='normal', color=color)
    plt.plot([x, x], [-0.1, y], color=color, linestyle='dashed', linewidth=0.4)
    plt.plot([-0.15, x], [y, y], color=color, linestyle='dashed', linewidth=0.4)

# Draw inverse line chart connecting A to B to C
# This will be a visible line through all reference points
plt.plot(
    xy_coords[:, 0],  # x values from A to C
    xy_coords[:, 1],  # y values from A to C
    color='black',
    linestyle='dashed',
    linewidth=1,
    label='A → C Path'
)
