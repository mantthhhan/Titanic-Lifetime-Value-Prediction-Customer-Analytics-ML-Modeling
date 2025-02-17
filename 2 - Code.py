# Import libraries
import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('customer_data.csv')

# Remove missing values and duplicates
data = data.dropna()
data = data.drop_duplicates()

# Handle outliers
data = data[(data['lifetime_value'] > 0) & (data['lifetime_value'] < 100000)]
data = data[(data['income'] > 0) & (data['income'] < 500000)]

# Convert data types
data['gender'] = data['gender'].astype('category')
data['state'] = data['state'].astype('category')
data['education'] = data['education'].astype('category')
data['marital_status'] = data['marital_status'].astype('category')

# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Analyze customer behavior and patterns
sns.histplot(data=data, x='age')
plt.show()

sns.histplot(data=data, x='income')
plt.show()

sns.countplot(data=data, x='gender')
plt.show()

# Analyze relationship between customer behavior and revenue
sns.scatterplot(data=data, x='age', y='lifetime_value')
plt.show()

sns.scatterplot(data=data, x='income', y='lifetime_value')
plt.show()

# Identify key drivers of customer lifetime value
sns.barplot(data=data, x='education', y='lifetime_value')
plt.show()

sns.barplot(data=data, x='marital_status', y='lifetime_value')
plt.show()

# Create new features to capture relevant customer behavior
data['age_bucket'] = pd.cut(data['age'], bins=[18, 35, 50, 65, 100], labels=['18-35', '36-50', '51-65', '66+'])
data['income_bucket'] = pd.cut(data['income'], bins=[0, 50000, 100000, 150000, 500000], labels=['<50k', '50-100k', '100-150k', '>150k'])
data['has_college_degree'] = np.where(data['education'].isin(['Bachelors', 'Masters', 'PhD']), 1, 0)

# Create customer segments based on behavior and demographics
data['customer_segment'] = data['age_bucket'].astype(str) + '-' + data['income_bucket'].astype(str) + '-' + data['gender'].astype(str)

# Splitting the data into train and validation sets
from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Fitting the model on the training data
from xgboost import XGBRegressor

model = XGBRegressor()
model.fit(X_train, y_train)

# Evaluating the model on the validation data
from sklearn.metrics import mean_squared_error

y_pred = model.predict(X_val)
mse = mean_squared_error(y_val, y_pred)
rmse = np.sqrt(mse)
print(f"Validation RMSE: {rmse}")
