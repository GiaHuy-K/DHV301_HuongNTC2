import pandas as pd
import numpy as np

# 1. Load the provided raw dataset [cite: 33]
df = pd.read_csv("LAB03_retail_quality_issues_raw.csv")

# 2. Check shape, head, dtypes, and describe(include='all') 
print("--- 2. Tổng quan dữ liệu ---")
print(f"Shape: {df.shape}") 
print(df.info())
print(df.describe(include='all')) 

# 3. Calculate missing value count and missing percentage for every column
print("\n--- 3. Kiểm tra giá trị thiếu ---")
missing_count = df.isna().sum() 
missing_pct = (df.isna().mean() * 100).round(2) 
missing_df = pd.DataFrame({"missing_count": missing_count, "missing_pct": missing_pct})
print(missing_df)

# 4. Check duplicate rows and possible duplicate logical keys (order_id)
print("\n--- 4. Kiểm tra trùng lặp ---")
print(f"Số dòng trùng lặp hoàn toàn: {df.duplicated().sum()}") 
print(f"Số order_id bị trùng: {df['order_id'].duplicated().sum()}")

# 5. Inspect unique values for categorical fields
print("\n--- 5. Kiểm tra tính nhất quán nhãn (Categorical) ---")
for col in ['gender', 'region', 'status']:
    print(f"\nGiá trị duy nhất trong {col}:")
    print(df[col].unique())
    print(df[col].value_counts(dropna=False)) 

# 6. Inspect min, max, and invalid ranges for numeric fields 
print("\n--- 6. Kiểm tra giá trị số không hợp lệ ---")
numeric_cols = ['customer_age', 'quantity', 'unit_price', 'discount']

print("Các dòng có giá trị số bất thường:")
invalid_numeric = df[
    (df['customer_age'] < 0) | (df['customer_age'] > 120) | 
    (df['unit_price'] <= 0) | 
    (df['discount'] > 1.0)
]
print(invalid_numeric[['order_id', 'customer_age', 'unit_price', 'discount']])

# Gợi ý xử lý ngày tháng để phát hiện lỗi 
df['order_date_dt'] = pd.to_datetime(df['order_date'], errors='coerce')
print("\nCác dòng có ngày tháng không hợp lệ (NaT):")
print(df[df['order_date_dt'].isna()][['order_id', 'order_date']])