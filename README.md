# Titanic-Lifetime-Value-Prediction-Customer-Analytics-ML-Modeling
📊 Titanic Lifetime Value Prediction – ML &amp; Analytics  A machine learning pipeline to analyze and predict **Customer Lifetime Value (CLV)** using **XGBoost** Regression. Includes data cleaning, feature engineering, EDA, and segmentation to uncover key customer insights.  

🚀 Tech: **Pandas, Seaborn, XGBoost, Sklearn**

**Project Overview:**
I built a data-driven **machine learning pipeline** to analyze and predict **Customer Lifetime Value (CLV)** using structured customer data. This project involved data cleaning, feature engineering, exploratory **data analysis (EDA)**, and predictive modeling to identify key factors influencing CLV.

To enhance data quality, I removed missing values, duplicates, and outliers while transforming categorical variables for analysis. Using **seaborn** and **matplotlib**, I visualized the relationships between age, income, education, marital status, and CLV to uncover insights into customer behavior. Additionally, I engineered new features such as age and income buckets, education indicators, and customer segments to enhance predictive accuracy.

Finally, I trained an **XGBoost** regression model to predict CLV, evaluated its performance using RMSE, and **optimized** it for better accuracy. This project provides valuable **insights** into customer spending patterns and retention strategies, enabling data-driven business decisions.

**Project Synopsis:**
I developed a** machine learning pipeline** to predict Customer Lifetime Value (CLV) using data preprocessing, visualization, feature engineering, and model training. The project focuses on identifying key drivers of customer value and leveraging predictive analytics to enhance business insights.

Key steps include:

✅ **Data Cleaning & Outlier Handling** – Ensured data integrity and consistency

✅ **EDA & Visualization** – Explored customer behavior patterns

✅ **Feature Engineering** – Created new features for better model accuracy

✅ **Customer Segmentation** – Grouped customers based on demographics & spending

✅ **Predictive Modeling** – Used XGBoost Regression to forecast CLV

✅ **Model Evaluation** – Assessed performance using RMSE

This project helps me understand customer profitability, optimize marketing efforts, and improve retention strategies using machine learning and advanced analytics.

**Results of Analysis: Titanic Lifetime Value Prediction – ML & Analytics**

After conducting data cleaning, exploratory analysis, feature engineering, and predictive modeling, I derived key insights related to customer lifetime value (LTV) prediction based on various demographic factors, using the Titanic dataset as a proxy.

1️⃣ Key Drivers of Lifetime Value

📊 Age and Income were strong predictors of lifetime value (LTV), with younger customers and those in the higher-income bracket showing higher predicted values.

📊 Education and marital status were also significant contributors, where customers with higher education (e.g., Bachelors, Masters) and those who are married tended to have higher LTVs.

📊 Gender showed minor influence, with female customers marginally showing higher average LTVs compared to males.

2️⃣ Data Cleaning & Feature Engineering Insights

🔧 After addressing missing values, duplicates, and outliers, I engineered new features that improved the model's predictive accuracy:

Age buckets: Categorizing age into 18-35, 36-50, 51-65, 66+ allowed for a more granular analysis.

Income brackets: Dividing income into <50k, 50-100k, 100-150k, >150k revealed income distribution's strong correlation with LTV.

Has a college degree: This binary feature significantly impacted LTV predictions, as more educated individuals had higher spending behavior.

3️⃣ Predictive Modeling Results

🤖 XGBoost Regressor proved to be the most accurate model, with low RMSE and strong R² performance on the validation set. It captured non-linear relationships between features and lifetime value effectively.

📉 Linear Regression did not perform as well due to its assumption of linear relationships, which did not align well with the complex interactions in the data.

🌲 Decision Trees showed decent performance but suffered from overfitting issues, especially with high variance in LTV predictions.

📊 Model Evaluation Metrics:

XGBoost RMSE: Lower root mean squared error (RMSE) than linear regression and decision trees, indicating better prediction accuracy.
R² Value: The model achieved a high R² value, showing that a significant proportion of LTV variance could be explained by the features.

4️⃣ Customer Segmentation & Insights

🔍 By combining age, income, gender, and education into custom segments (e.g., “High income-College educated-Young”), we could identify customer segments with the highest predicted LTVs, enabling businesses to target high-value customers.

📊 Customer segments such as young, highly-educated individuals in the top income brackets exhibited consistently high LTV predictions, suggesting they are prime targets for marketing and retention efforts.

5️⃣ Strategic Recommendations

✅ Targeted Marketing: Businesses should focus on young, high-income customers with higher education for high LTV potential.

✅ Retention Strategies: Customers with higher education levels and those in the age bracket 18-35 should receive tailored offers to maximize their lifetime value.

✅ Investment in Data: More detailed demographic and behavioral data could further refine predictions, especially in terms of customized offers for higher LTV segments.

