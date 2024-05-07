import matplotlib.pyplot as plt
import numpy as np

# Random data for the histograms
data = np.random.normal(0, 1, 1000)

# List of 15 different pink-related colors
pink_shades = [
    'pink', 'lightpink', 'hotpink', 'deeppink', 'palevioletred', 'mediumvioletred',
    'fuchsia', 'magenta', 'orchid', 'thistle', 'lightcoral', 'violet', 'crimson',
    'rosybrown', 'salmon'
]
# Plot histograms for each shade of pink
for color in pink_shades:
    plt.hist(data, bins=30, color=color)
    plt.title(f"Histogram with {color.capitalize()}")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()
