import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("customers.csv")

print("---- RAW DATA ----")
print(df)

# 1. Fix incorrect data types
df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# 2. Handle missing values
df['name'] = df['name'].fillna("Unknown")
df['city'] = df['city'].fillna("Not Provided")
df['purchase_amount'] = df['purchase_amount'].fillna(df['purchase_amount'].mean())

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Fix negative and unrealistic values
df.loc[df['purchase_amount'] < 0, 'purchase_amount'] = 0
df.loc[df['age'] < 0, 'age'] = np.nan

# 5. Handle outliers (remove ages > 100)
df = df[df['age'] <= 100]

# 6. Create new useful columns
df['signup_year'] = df['signup_date'].dt.year
df['is_high_purchase'] = df['purchase_amount'].apply(lambda x: x > 250)

# 7. Rename columns for clarity
df = df.rename(columns={
    'purchase_amount': 'amount_spent'
})

print("\n---- CLEANED DATA ----")
print(df)

# Save cleaned data
df.to_csv("customers_cleaned.csv", index=False)
