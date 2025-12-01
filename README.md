# How Credit Shapes Economic Growth: Insights from World Bank Data

[![CI](https://github.com/AuLb44/Udacity_DataScientistNanoDegree_Project1/actions/workflows/ci.yml/badge.svg)](https://github.com/AuLb44/Udacity_DataScientistNanoDegree_Project1/actions/workflows/ci.yml)

## Project Overview

This project explores the relationship between credit availability and GDP growth using World Bank economic indicators. The analysis follows the **CRISP-DM** (Cross-Industry Standard Process for Data Mining) methodology: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment/Conclusions.

This project is part of the Udacity Data Scientist Nanodegree Program.

## Motivation

Economic growth is influenced by multiple factors, including credit availability, inflation, and unemployment. Understanding these relationships can help policymakers make informed decisions about economic policy. This analysis aims to provide data-driven insights into how credit availability correlates with GDP growth across countries.

## Business Questions

1. **Which countries have the highest GDP growth?** - Identifying top performers helps understand economic success patterns.
2. **How does credit availability correlate with GDP growth?** - Understanding if easier credit access stimulates economic growth.
3. **What is the relationship between inflation and unemployment?** - Exploring the Phillips curve relationship in the data.
4. **Can we predict GDP growth based on credit and economic indicators?** - Building a predictive model for economic forecasting.

## Dataset

**Source:** [World Bank Databank](https://databank.worldbank.org/)

**Indicators Used:**
- Credit to private sector (% of GDP)
- Inflation rate (annual %)
- Unemployment rate (% of labor force)
- GDP growth rate (annual %)

For demonstration purposes, the notebook can generate synthetic data. See `data/README.md` for instructions on obtaining real World Bank data.

## Project Structure

```
.
├── notebook.ipynb          # Main analysis notebook (CRISP-DM structured)
├── src/
│   ├── __init__.py
│   └── utils.py            # Utility functions with docstrings
├── tests/
│   ├── __init__.py
│   └── test_utils.py       # Unit tests for utility functions
├── data/
│   └── README.md           # Instructions for obtaining data
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI workflow
├── requirements.txt        # Python dependencies
├── blogpost.md             # Medium blog post draft
├── README.md               # This file
└── .gitignore              # Git ignore patterns
```

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AuLb44/Udacity_DataScientistNanoDegree_Project1.git
   cd Udacity_DataScientistNanoDegree_Project1
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Jupyter notebook:**
   ```bash
   jupyter notebook notebook.ipynb
   ```

5. **Run tests:**
   ```bash
   pytest tests/ -v
   ```

## Libraries Used

| Library | Purpose |
|---------|---------|
| pandas | Data manipulation and analysis |
| numpy | Numerical computations |
| matplotlib | Data visualization |
| seaborn | Statistical visualizations |
| scikit-learn | Machine learning models |
| jupyter | Interactive notebook environment |

## Results Summary

- **GDP Growth Distribution:** Most countries show GDP growth between -2% and 6%, with significant variation across the dataset.
- **Correlation Analysis:** Credit availability shows a moderate positive correlation with GDP growth.
- **Model Performance:** Linear Regression model achieved R² ≈ 0.02 and RMSE ≈ 4.5 on synthetic data.
- **Scenario Prediction:** The model can predict GDP growth for hypothetical economic conditions.

*Note: Results are based on synthetic data for demonstration. Real-world data would yield more meaningful insights.*

## Key Takeaways

1. Credit availability plays a role in economic growth, but it's not the sole driver.
2. Inflation and unemployment have weaker correlations with GDP growth in this dataset.
3. Predictive modeling can provide insights, but real-world complexity requires more robust data and models.

## Blog Post

A detailed write-up of this analysis is available in [blogpost.md](blogpost.md) and will be published on Medium.

## Acknowledgements

- Data sourced from [World Bank Databank](https://databank.worldbank.org/)
- Project completed as part of [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025)

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.
