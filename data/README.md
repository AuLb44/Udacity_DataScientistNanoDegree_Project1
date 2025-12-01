# Data Directory

This directory is intended for storing datasets used in the analysis.

## Dataset Source

The data used in this project comes from the [World Bank Databank](https://databank.worldbank.org/).

### Indicators Used

1. **Credit to private sector (% of GDP)** - Domestic credit to private sector as a percentage of GDP
2. **Inflation (%)** - Consumer price inflation, annual percentage
3. **Unemployment (%)** - Unemployment rate, total (% of total labor force)
4. **GDP growth (%)** - Annual percentage growth rate of GDP

## How to Obtain the Data

1. Visit [World Bank Databank](https://databank.worldbank.org/)
2. Select "World Development Indicators" database
3. Choose the indicators listed above
4. Select countries and time range of interest
5. Download in CSV format
6. Place the CSV file in this directory

## Note

For demonstration purposes, the notebook can generate synthetic data that mimics the structure of the World Bank data. This is useful for testing and educational purposes but should be replaced with real data for actual analysis.

Large data files are excluded from version control via `.gitignore`. Please download the data separately using the instructions above.
