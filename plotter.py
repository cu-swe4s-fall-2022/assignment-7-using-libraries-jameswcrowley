# Your code to create majestic plots goes in here!
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def make_plots(file_name):
    # figure 1: iris boxplot:
    iris_df = pd.read_csv(file_name,
                          sep=',',
                          header=None)
    iris_labels = ['sepal width',
                   'sepal_length',
                   'petal_width',
                   'petal_length',
                   'species']
    iris_df.columns = iris_labels
    plt.figure(figsize=[12, 10])
    plt.boxplot(iris_df[iris_labels], labels=iris_labels)
    plt.ylabel('cm')

    plt.savefig('./plots/iris_boxplot.png')

    # figure 2: scatter plot:

    plt.figure(figsize=[12, 10])
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
    plt.figure(figsize=[20, 10])

    plt.subplot(1, 2, 1)  # 2 subplots, first is boxplot.
    iris_df = pd.read_csv(file_name,
                          sep=',',
                          header=None)
    iris_labels = ['sepal width',
                   'sepal_length',
                   'petal_width',
                   'petal_length',
                   'species']
    iris_df.columns = iris_labels
    plt.figure(figsize=[12, 10])
    plt.boxplot(iris_df[iris_labels], labels=iris_labels)
    plt.ylabel('cm')

    plt.subplot(1, 2, 2)
    for species_i in set(iris_df['species']):
        species_subset = iris_df[iris_df['species'] == species_i]
        plt.scatter(species_subset['petal_width'],
                    species_subset['petal_length'],
                    label=species_i)
    plt.legend()
    plt.xlabel('petal_width')
    plt.ylabel('petal_length')

    plt.savefig('./plots/multi_panel_figure.png')


