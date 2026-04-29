import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load cleaned dataset.
    """
    return pd.read_csv(file_path)


def basic_info(df: pd.DataFrame) -> None:
    """
    Display general information about the dataset.
    """
    print("\n" + "=" * 50)
    print("DATASET INFORMATION")
    print("=" * 50)
    print(df.info())


def descriptive_statistics(df: pd.DataFrame) -> None:
    """
    Display descriptive statistics.
    """
    print("\n" + "=" * 50)
    print("DESCRIPTIVE STATISTICS")
    print("=" * 50)
    print(df.describe(include="all"))


def missing_values(df: pd.DataFrame) -> None:
    """
    Check missing values.
    """
    print("\n" + "=" * 50)
    print("MISSING VALUES")
    print("=" * 50)
    print(df.isnull().sum())


def correlation_analysis(df: pd.DataFrame) -> None:
    """
    Display correlation matrix.
    """
    print("\n" + "=" * 50)
    print("CORRELATION MATRIX")
    print("=" * 50)

    numeric_df = df.select_dtypes(include=["number"])
    print(numeric_df.corr())


def top_happiest_countries(df: pd.DataFrame, n: int = 10) -> None:
    """
    Display top happiest countries.
    """
    score_col = "score"

    if score_col in df.columns:
        print("\n" + "=" * 50)
        print(f"TOP {n} HAPPIEST COUNTRIES")
        print("=" * 50)

        print(
            df.nlargest(n, score_col)[
                ["country", score_col]
            ].to_string(index=False)
        )


def main() -> None:
    file_path = "data/processed/world_happiness_cleaned.csv"

    df = load_data(file_path)

    basic_info(df)
    descriptive_statistics(df)
    missing_values(df)
    correlation_analysis(df)
    top_happiest_countries(df)


if __name__ == "__main__":
    main()