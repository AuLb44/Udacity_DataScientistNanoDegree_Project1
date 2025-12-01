"""
Utility functions for the Udacity Data Scientist Nanodegree Project 1.

This module provides helper functions for data loading, preprocessing,
visualization, and model evaluation used in the economic data analysis.
"""

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score


def calculate_model_metrics(y_true, y_pred):
    """
    Calculate regression model performance metrics.

    Computes R-squared (coefficient of determination) and Root Mean Squared Error
    (RMSE) to evaluate how well predictions match actual values.

    Args:
        y_true (array-like): Ground truth (actual) target values.
        y_pred (array-like): Predicted target values from the model.

    Returns:
        dict: A dictionary containing:
            - 'r2': R-squared score (float), where 1.0 is perfect prediction.
            - 'rmse': Root Mean Squared Error (float), in the same units as target.

    Examples:
        >>> y_actual = [3.0, -0.5, 2.0, 7.0]
        >>> y_predicted = [2.5, 0.0, 2.0, 8.0]
        >>> metrics = calculate_model_metrics(y_actual, y_predicted)
        >>> print(f"R²: {metrics['r2']:.4f}, RMSE: {metrics['rmse']:.4f}")
        R²: 0.9486, RMSE: 0.6124
    """
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return {'r2': r2, 'rmse': rmse}


def clean_dataframe(df, drop_na=True):
    """
    Clean a pandas DataFrame by handling missing values.

    Performs basic data cleaning operations including identifying and
    optionally removing rows with missing values.

    Args:
        df (pd.DataFrame): Input DataFrame to clean.
        drop_na (bool, optional): Whether to drop rows with missing values.
            Defaults to True.

    Returns:
        pd.DataFrame: Cleaned DataFrame with missing values handled.

    Examples:
        >>> import pandas as pd
        >>> data = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
        >>> cleaned = clean_dataframe(data, drop_na=True)
        >>> len(cleaned)
        1
    """
    if drop_na:
        return df.dropna()
    return df


def generate_synthetic_economic_data(n_samples=200, random_seed=42):
    """
    Generate synthetic economic indicator data for demonstration purposes.

    Creates a DataFrame with simulated economic indicators including credit
    to private sector, inflation, unemployment, and GDP growth. This is useful
    for testing and demonstration when real World Bank data is not available.

    Args:
        n_samples (int, optional): Number of country samples to generate.
            Defaults to 200.
        random_seed (int, optional): Random seed for reproducibility.
            Defaults to 42.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - 'Country': Country identifier string
            - 'Credit_to_private_sector': Credit as % of GDP (10-150)
            - 'Inflation': Inflation rate % (0-15)
            - 'Unemployment': Unemployment rate % (2-20)
            - 'GDP_growth': GDP growth rate % (-5 to 10)

    Examples:
        >>> data = generate_synthetic_economic_data(n_samples=5, random_seed=42)
        >>> data.shape
        (5, 5)
        >>> list(data.columns)
        ['Country', 'Credit_to_private_sector', 'Inflation', 'Unemployment', 'GDP_growth']
    """
    np.random.seed(random_seed)
    
    data = pd.DataFrame({
        'Country': [f'Country_{i}' for i in range(n_samples)],
        'Credit_to_private_sector': np.random.uniform(10, 150, n_samples),
        'Inflation': np.random.uniform(0, 15, n_samples),
        'Unemployment': np.random.uniform(2, 20, n_samples),
        'GDP_growth': np.random.uniform(-5, 10, n_samples)
    })
    
    return data


def predict_gdp_growth(model, credit, inflation, unemployment):
    """
    Predict GDP growth given economic indicators using a trained model.

    Creates a scenario DataFrame and uses the provided model to predict
    the expected GDP growth rate.

    Args:
        model: A trained scikit-learn regression model with a predict method.
        credit (float): Credit to private sector as percentage of GDP.
        inflation (float): Inflation rate as a percentage.
        unemployment (float): Unemployment rate as a percentage.

    Returns:
        float: Predicted GDP growth rate as a percentage.

    Examples:
        >>> from sklearn.linear_model import LinearRegression
        >>> # Assuming model is trained
        >>> # predicted = predict_gdp_growth(model, credit=50, inflation=3, unemployment=5)
    """
    scenario = pd.DataFrame({
        'Credit_to_private_sector': [credit],
        'Inflation': [inflation],
        'Unemployment': [unemployment]
    })
    return model.predict(scenario)[0]
