import pandas as pd
import numpy as np

# 1. Load data
df = pd.read_csv("LAB03_retail_quality_issues_raw.csv")

# 2. Xử lý trùng lặp
df = df.drop_duplicates()

# 3. Chuẩn hóa Categorical
df['gender'] = df['gender'].astype(str).str.lower().map({
    'male': 'male', 'm': 'male', 'female': 'female', 'f': 'female'
})
df['region'] = df['region'].astype(str).str.strip().str.title()
df['status'] = df['status'].astype(str).str.strip().str.capitalize()

# 4. Xử lý Numeric & Dates
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df.loc[(df['customer_age'] < 0) | (df['customer_age'] > 120), 'customer_age'] = np.nan
df.loc[df['unit_price'] <= 0, 'unit_price'] = df['unit_price'].median()
df.loc[df['discount'] > 1, 'discount'] = np.nan # Hoặc set về 0 tùy nghiệp vụ

# 5. Tạo Derived Fields (Yêu cầu quan trọng)
df['revenue'] = df['quantity'] * df['unit_price'] * (1 - df['discount'].fillna(0))

def categorize_age(age):
    if pd.isna(age): return "Unknown"
    if age <= 25: return "18-25"
    if age <= 35: return "26-35"
    if age <= 50: return "36-50"
    return ">50"

df['age_group'] = df['customer_age'].apply(categorize_age)

# 6. Save file
df.to_csv("LAB04_cleaned_retail.csv", index=False)
print("Đã tạo file LAB04_cleaned_retail.csv thành công!")