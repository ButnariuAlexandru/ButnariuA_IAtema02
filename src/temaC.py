import seaborn as sns
import matplotlib.pyplot as plt


def main():
    tips = sns.load_dataset("tips")

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("Dashboard Vizualizare Dataset Tips", fontsize=16)

    culori = {"Male": "blue", "Female": "red"}

    for sex, culoare in culori.items():
        subset = tips[tips["sex"] == sex]
        axes[0, 0].scatter(subset["total_bill"], subset["tip"],
                           label=sex, color=culoare, alpha=0.7)

    axes[0, 0].set_title("Total Bill vs Tip")
    axes[0, 0].set_xlabel("Total Bill ($)")
    axes[0, 0].set_ylabel("Tip ($)")
    axes[0, 0].legend()

    sns.boxplot(data=tips,
                x="day",
                y="total_bill",
                order=["Thur", "Fri", "Sat", "Sun"],
                ax=axes[0, 1])

    axes[0, 1].set_title("Distribuția total_bill per zi")
    axes[0, 1].set_xlabel("Zi")
    axes[0, 1].set_ylabel("Total Bill ($)")

    sns.histplot(data=tips,
                 x="tip",
                 hue="time",
                 kde=True,
                 ax=axes[1, 0])

    axes[1, 0].set_title("Distribuția bacșișurilor")
    axes[1, 0].set_xlabel("Tip ($)")
    axes[1, 0].set_ylabel("Frecvență")

    sns.barplot(data=tips,
                x="day",
                y="tip",
                order=["Thur", "Fri", "Sat", "Sun"],
                errorbar="ci",
                ax=axes[1, 1])

    axes[1, 1].set_title("Bacșiș mediu per zi")
    axes[1, 1].set_xlabel("Zi")
    axes[1, 1].set_ylabel("Tip mediu ($)")

    plt.tight_layout()
    plt.savefig("dashboard_tips.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    main()