import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
)

sns.set_theme(style="whitegrid")


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load cleaned dataset.
    """
    return pd.read_csv(file_path)


def prepare_features(df: pd.DataFrame):
    """
    Prepare features and target variable.
    """
    features = [
        "gdp_per_capita",
        "social_support",
        "healthy_life_expectancy",
        "freedom",
        "generosity",
        "corruption",
    ]

    X = df[features]
    y = df["score"]

    return X, y, features


def train_model(X, y):
    """
    Train Linear Regression model.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    return model, X_train, X_test, y_train, y_test, predictions


def evaluate_model(model, X, y, y_test, predictions):
    """
    Evaluate model performance.
    """
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, predictions)

    cv_scores = cross_val_score(
        model,
        X,
        y,
        cv=5,
        scoring="r2"
    )

    print("\n" + "=" * 60)
    print("MODEL EVALUATION")
    print("=" * 60)
    print(f"MAE:             {mae:.4f}")
    print(f"MSE:             {mse:.4f}")
    print(f"RMSE:            {rmse:.4f}")
    print(f"R² Score:        {r2:.4f}")
    print(f"CV Mean R²:      {cv_scores.mean():.4f}")
    print(f"CV Std Dev:      {cv_scores.std():.4f}")


def display_feature_importance(model, features):
    """
    Display feature importance.
    """
    importance = pd.DataFrame({
        "Feature": features,
        "Coefficient": model.coef_
    }).sort_values(
        by="Coefficient",
        ascending=False
    )

    print("\n" + "=" * 60)
    print("FEATURE IMPORTANCE")
    print("=" * 60)
    print(importance.to_string(index=False))


def plot_predictions(y_test, predictions):
    """
    Plot actual vs predicted values.
    """
    os.makedirs("images", exist_ok=True)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x=y_test,
        y=predictions
    )

    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        linestyle="--"
    )

    plt.xlabel("Actual Happiness Score")
    plt.ylabel("Predicted Happiness Score")
    plt.title("Actual vs Predicted Happiness Scores")
    plt.tight_layout()
    plt.savefig("images/model_predictions.png")
    plt.close()

    print("\nPrediction plot saved to images/model_predictions.png")


def save_model(model):
    """
    Save trained model.
    """
    joblib.dump(model, "happiness_model.pkl")
    print("Model saved as 'happiness_model.pkl'")


def main():
    file_path = "data/processed/world_happiness_cleaned.csv"

    print("Loading data...")
    df = load_data(file_path)

    X, y, features = prepare_features(df)

    print("Training model...")
    (
        model,
        X_train,
        X_test,
        y_train,
        y_test,
        predictions,
    ) = train_model(X, y)

    evaluate_model(
        model,
        X,
        y,
        y_test,
        predictions,
    )

    display_feature_importance(
        model,
        features,
    )

    plot_predictions(
        y_test,
        predictions,
    )

    save_model(model)


if __name__ == "__main__":
    main()