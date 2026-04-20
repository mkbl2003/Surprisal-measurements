from surprisal_adjuster import *
import glob
from matplotlib import pyplot as plt
def boxplot_generator(name):
    filenames = glob.glob('david_temp_2_surprisal_values.txt')
    preliminary_results = []
    # results = []
    for filename in filenames:
        preliminary_results.append(main(filename))
    
    results = [[value for inner in group for _, value in inner] for group in preliminary_results]
    fig, ax = plt.subplots(figsize=(10, 7))

    # Create boxplot
    ax.boxplot(results)

    # Set y-axis ticks
    ax.set_yticks([0, 10, 20, 30, 40])

    # Create x-axis labels (cleaner names)
    labels = [f.replace('_surprisal_values.txt', '') for f in filenames]

    # Set x-axis ticks and labels
    ax.set_xticks(range(1, len(labels) + 1))
    ax.set_xticklabels(labels, rotation=30, ha='right')

    ax.set_xlabel("Files")
    ax.set_ylabel("Surprisal values")
    ax.set_title(name)

    plt.tight_layout()
    plt.savefig(name)
