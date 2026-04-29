import pandas as pd
from pathlib import Path

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
    )

    df = df.drop_duplicates()
    
    df = df.dropna()
    
    df = df.reset_index(drop=True)

    return df


def save_data(df: pd.DataFrame, output_path: str) -> None:
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def main() -> None:
    input_file = "data/raw/world_happiness_2026.csv"
    output_file = "data/processed/world_happiness_cleaned.csv"

    print("Loading dataset...")
    df = load_data(input_file)

    print(f"Original shape: {df.shape}")

    cleaned_df = clean_data(df)

    print(f"Cleaned shape: {cleaned_df.shape}")

    save_data(cleaned_df, output_file)

    print(f"Cleaned dataset saved to: {output_file}")

if __name__ == "__main__":
    main()