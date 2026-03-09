import seaborn as sns
import matplotlib.pyplot as plt


def main():
    iris = sns.load_dataset("iris")

    pair = sns.pairplot(iris, hue="species", diag_kind="kde")
    plt.suptitle("Pairplot Dataset Iris", y=1.02)
    plt.savefig("pairplot_iris.png", dpi=150)
    plt.show()

    fig, axes = plt.subplots(1, 4, figsize=(18, 5))

    variabile = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]

    for i, var in enumerate(variabile):
        sns.violinplot(
            data=iris,
            x="species",
            y=var,
            hue="species",
            split=False,
            ax=axes[i],
            legend=False
        )
        axes[i].set_title(var)

    plt.suptitle("Distribuția variabilelor Iris per specie")
    plt.tight_layout()
    plt.savefig("violinplots_iris.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()