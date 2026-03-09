import seaborn as sns
import matplotlib.pyplot as plt


def main():
    tips = sns.load_dataset("tips")

    dimensiune = tips.shape
    print(f"Dimensiunea datasetului: {dimensiune}")

    tip_date = tips.dtypes
    print("\nTipurile de date pentru fiecare coloana:")
    print(tip_date)

    statistici = tips.describe()
    print("\nStatistici descriptive pentru coloanele numerice:")
    print(statistici)

    bacsis_mediu = tips.groupby(["day", "sex"]).mean(numeric_only=True)
    print("\n=== Bacșiș mediu per zi și per sex ===")
    print(bacsis_mediu["tip"])

    tips_extins = tips.copy()
    tips_extins["procent_bacsis"] = tips_extins["tip"] / tips_extins["total_bill"] * 100

    print("\n=== Primele 5 valori procent_bacsis ===")
    print(tips_extins[["total_bill", "tip", "procent_bacsis"]].head())

    top5 = tips_extins.sort_values(by="procent_bacsis", ascending=False).head(5)
    print("\n=== Top 5 cele mai generoase mese ===")
    print(top5[["total_bill", "tip", "procent_bacsis", "day", "sex"]])

    mese = tips.groupby(["day", "smoker"]).size()
    print("\n=== Număr mese per zi și fumători ===")
    print(mese)


if __name__ == "__main__":
    main()