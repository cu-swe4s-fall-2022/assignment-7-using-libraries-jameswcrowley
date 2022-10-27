# Your code to create majestic plots goes in here!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def make_plots(file_name):
    # figure 1: iris boxplot:
    iris_df = pd.read_csv(file_name,
                          header=None)
    iris_labels = ['sepal width',
                   'sepal_length',
                   'petal_width',
                   'petal_length',
                   'species']
    iris_df.columns = iris_labels


    measurement_labels = ['sepal width',
                          'sepal_length',
                          'petal_width',
                          'petal_length']
    plt.figure(figsize=[10, 8])
    plt.boxplot(iris_df[measurement_labels],
                labels=measurement_labels)
    plt.ylabel('cm')

    plt.savefig('./plots/iris_boxplot.png')

    # figure 2: scatter plot:

    plt.figure(figsize=[10, 8])
    # need to create separate groups for each species.
    for species_i in set(iris_df['species']):
        species_subset = iris_df[iris_df['species'] == species_i]
        plt.scatter(species_subset['petal_width'],
                    species_subset['petal_length'],
                    label=species_i)
    plt.legend()
    plt.xlabel('petal_width')
    plt.ylabel('petal_length')

    plt.savefig('./plots/petal_width_v_length_scatter.png')

    # figure 3: multi-plot figure:
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(12, 8)

    axes[0].boxplot(iris_df[measurement_labels], labels=measurement_labels)
    axes[0].set_ylabel('cm')

    for species_i in set(iris_df['species']):
        species_subset = iris_df[iris_df['species'] == species_i]
        axes[1].scatter(species_subset['petal_width'],
                           species_subset['petal_length'],
                           label=species_i)
    plt.legend()
    axes[1].set_xlabel('petal_width')
    axes[1].set_ylabel('petal_length')


    # removing the top right border of each plot:
    for i in range(2):
        axes[i].spines['top'].set_visible(False)
        axes[i].spines['right'].set_visible(False)


    plt.savefig('./plots/multi_panel_figure.png')


