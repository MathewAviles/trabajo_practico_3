import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Configuration
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 8)


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load cleaned dataset.
    """
    return pd.read_csv(file_path)


def create_output_directory() -> None:
    """
    Create images directory if it doesn't exist.
    """
    os.makedirs("images", exist_ok=True)


def plot_top_happiest_countries(df: pd.DataFrame) -> None:
    """
    Plot top 10 happiest countries.
    """
    top_10 = df.nlargest(10, "score")

    plt.figure()
    sns.barplot(
        data=top_10,
        x="score",
        y="country"
    )
    plt.title("Top 10 Happiest Countries (2026)")
    plt.xlabel("Happiness Score")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.savefig("images/top_10_happiest_countries.png")
    plt.close()


def plot_score_distribution(df: pd.DataFrame) -> None:
    """
    Plot happiness score distribution.
    """
    plt.figure()
    sns.histplot(df["score"], kde=True)
    plt.title("Distribution of Happiness Scores")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("images/score_distribution.png")
    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """
    Plot correlation heatmap.
    """
    numeric_df = df.select_dtypes(include=["number"])

    plt.figure(figsize=(12, 10))
    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("images/correlation_heatmap.png")
    plt.close()


def plot_gdp_vs_happiness(df: pd.DataFrame) -> None:
    """
    Plot GDP per capita vs happiness score.
    """
    plt.figure()
    sns.scatterplot(
        data=df,
        x="gdp_per_capita",
        y="score",
        hue="region"
    )
    plt.title("GDP per Capita vs Happiness Score")
    plt.xlabel("GDP per Capita")
    plt.ylabel("Happiness Score")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("images/gdp_vs_happiness.png")
    plt.close()


def plot_average_score_by_region(df: pd.DataFrame) -> None:
    """
    Plot average happiness score by region.
    """
    regional_scores = (
        df.groupby("region")["score"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    plt.figure(figsize=(14, 8))
    sns.barplot(
        data=regional_scores,
        x="score",
        y="region"
    )
    plt.title("Average Happiness Score by Region")
    plt.xlabel("Average Score")
    plt.ylabel("Region")
    plt.tight_layout()
    plt.savefig("images/average_score_by_region.png")
    plt.close()


def main() -> None:
    file_path = "data/processed/world_happiness_cleaned.csv"

    create_output_directory()

    df = load_data(file_path)

    print("Generating visualizations...")

    plot_top_happiest_countries(df)
    plot_score_distribution(df)
    plot_correlation_heatmap(df)
    plot_gdp_vs_happiness(df)
    plot_average_score_by_region(df)

    print("Visualizations saved successfully in the 'images/' folder.")


if __name__ == "__main__":
    main()