How Credit Shapes Economic Growth: Insights from World Bank Data
https://unsplash.com/photos/world-map
(Placeholder: Use a royalty-free image from Unsplash or Pexels)

Introduction
Economic growth is a complex phenomenon influenced by multiple factors, including credit availability, inflation, and unemployment. Using World Bank economic indicators, this analysis explores these relationships and builds a predictive model for GDP growth.

Business Questions

Which countries have the highest GDP growth?
How does credit availability correlate with GDP growth?
What is the relationship between inflation and unemployment?
Can we predict GDP growth based on credit and economic indicators?


Exploratory Data Analysis
Before modeling, we examined the data to understand its structure and relationships.
GDP Growth Distribution
images/gdp_growth_distribution.png
Observation: GDP growth varies widely across countries, with most values clustering between -2% and 6%.

Correlation Heatmap
images/correlation_heatmap.png
Observation: Credit availability shows a moderate positive correlation with GDP growth, while inflation and unemployment have weaker relationships.

Additional Visuals
Credit vs GDP Growth
https://placeholder.com/credit-vs-gdp
Insight: Countries with higher credit availability tend to have slightly higher GDP growth, but the relationship is not strong.
Inflation vs Unemployment
https://placeholder.com/inflation-vs-unemployment
Insight: The classic Phillips curve relationship is weak in this dataset, suggesting other factors dominate.

Modeling
We trained a Linear Regression model to predict GDP growth using:

Credit to private sector (% of GDP)
Inflation (%)
Unemployment (%)

Model Performance:

R² Score: ~0.02
RMSE: ~4.5

(Low predictive power due to synthetic data; real-world data would likely yield better results.)

Scenario Prediction
Imagine a country with:

Credit to private sector: 50%
Inflation: 3%
Unemployment: 5%

Predicted GDP Growth: ~2.3%

Key Takeaways

Credit availability plays a role in economic growth, but it’s not the sole driver.
Inflation and unemployment have weaker correlations in this dataset.
Predictive modeling can provide insights, but real-world complexity requires more robust data and models.


Conclusion
Policymakers should consider credit availability as part of a broader economic strategy. While credit can stimulate growth, other factors like governance, trade, and innovation are equally critical.

Resources

https://databank.worldbank.org/
https://unsplash.com/
https://github.com/
