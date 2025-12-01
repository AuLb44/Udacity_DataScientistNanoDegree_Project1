"""
Unit tests for the src/utils.py module.

Tests the utility functions used in the economic data analysis project.
"""

import numpy as np
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import (
    calculate_model_metrics,
    clean_dataframe,
    generate_synthetic_economic_data,
    predict_gdp_growth
)


class TestCalculateModelMetrics:
    """Tests for calculate_model_metrics function."""

    def test_perfect_predictions(self):
        """Test metrics with perfect predictions."""
        y_true = [1.0, 2.0, 3.0, 4.0]
        y_pred = [1.0, 2.0, 3.0, 4.0]
        metrics = calculate_model_metrics(y_true, y_pred)
        
        assert metrics['r2'] == pytest.approx(1.0)
        assert metrics['rmse'] == pytest.approx(0.0)

    def test_returns_dict_with_required_keys(self):
        """Test that function returns dictionary with r2 and rmse keys."""
        y_true = [1.0, 2.0, 3.0]
        y_pred = [1.1, 2.2, 2.9]
        metrics = calculate_model_metrics(y_true, y_pred)
        
        assert 'r2' in metrics
        assert 'rmse' in metrics

    def test_rmse_calculation(self):
        """Test RMSE calculation with known values."""
        y_true = [3.0, -0.5, 2.0, 7.0]
        y_pred = [2.5, 0.0, 2.0, 8.0]
        metrics = calculate_model_metrics(y_true, y_pred)
        
        # Expected RMSE: sqrt(mean([0.25, 0.25, 0, 1])) = sqrt(0.375) ≈ 0.612
        assert metrics['rmse'] == pytest.approx(0.6124, rel=0.01)


class TestCleanDataframe:
    """Tests for clean_dataframe function."""

    def test_drops_na_by_default(self):
        """Test that NaN values are dropped by default."""
        df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
        cleaned = clean_dataframe(df)
        
        assert len(cleaned) == 1
        assert cleaned['A'].iloc[0] == 1
        assert cleaned['B'].iloc[0] == 4

    def test_keeps_na_when_drop_false(self):
        """Test that NaN values are kept when drop_na=False."""
        df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
        cleaned = clean_dataframe(df, drop_na=False)
        
        assert len(cleaned) == 3

    def test_returns_dataframe(self):
        """Test that function returns a DataFrame."""
        df = pd.DataFrame({'A': [1, 2, 3]})
        result = clean_dataframe(df)
        
        assert isinstance(result, pd.DataFrame)


class TestGenerateSyntheticEconomicData:
    """Tests for generate_synthetic_economic_data function."""

    def test_returns_correct_shape(self):
        """Test that function returns DataFrame with correct shape."""
        data = generate_synthetic_economic_data(n_samples=10)
        
        assert data.shape == (10, 5)

    def test_has_required_columns(self):
        """Test that DataFrame has all required columns."""
        data = generate_synthetic_economic_data(n_samples=5)
        expected_columns = ['Country', 'Credit_to_private_sector', 'Inflation', 
                          'Unemployment', 'GDP_growth']
        
        assert list(data.columns) == expected_columns

    def test_reproducibility_with_seed(self):
        """Test that same seed produces same data."""
        data1 = generate_synthetic_economic_data(n_samples=10, random_seed=42)
        data2 = generate_synthetic_economic_data(n_samples=10, random_seed=42)
        
        pd.testing.assert_frame_equal(data1, data2)

    def test_values_in_expected_ranges(self):
        """Test that generated values are within expected ranges."""
        data = generate_synthetic_economic_data(n_samples=100)
        
        assert data['Credit_to_private_sector'].min() >= 10
        assert data['Credit_to_private_sector'].max() <= 150
        assert data['Inflation'].min() >= 0
        assert data['Inflation'].max() <= 15
        assert data['Unemployment'].min() >= 2
        assert data['Unemployment'].max() <= 20
        assert data['GDP_growth'].min() >= -5
        assert data['GDP_growth'].max() <= 10


class TestPredictGdpGrowth:
    """Tests for predict_gdp_growth function."""

    def test_returns_float(self):
        """Test that function returns a float value."""
        # Create a simple model
        X = np.array([[50, 3, 5], [60, 4, 6], [70, 5, 7]])
        y = np.array([2.0, 2.5, 3.0])
        model = LinearRegression()
        model.fit(X, y)
        
        result = predict_gdp_growth(model, credit=55, inflation=3.5, unemployment=5.5)
        
        assert isinstance(result, (float, np.floating))

    def test_prediction_consistency(self):
        """Test that same inputs produce same prediction."""
        X = np.array([[50, 3, 5], [60, 4, 6], [70, 5, 7]])
        y = np.array([2.0, 2.5, 3.0])
        model = LinearRegression()
        model.fit(X, y)
        
        result1 = predict_gdp_growth(model, credit=50, inflation=3, unemployment=5)
        result2 = predict_gdp_growth(model, credit=50, inflation=3, unemployment=5)
        
        assert result1 == pytest.approx(result2)
