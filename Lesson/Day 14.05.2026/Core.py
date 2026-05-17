import pandas as pd
import seaborn as sns
import os

df = pd.read_csv("dataset/salary_survey_raw.csv")

# --- CÂU 1: Load dataset và in 5 dòng đầu ---
print("--- Câu 1 ---")
print(df.head())
print(f"Tổng cộng có {len(df)} người.")
print(df.shape)
print(df.describe())
# --- CÂU 2: Kiểm tra kiểu dữ liệu và giá trị NULL ---
print("\n--- Câu 2 ---")
print("Kiểm tra giá trị null")
miss = df.isnull().sum()
pct  = (miss / len(df) * 100).round(1)
report = pd.DataFrame({'count': miss, 'pct_%': pct})
report = report[report['count'] > 0].sort_values('pct_%', ascending=False)
print(report)
# --- CÂU 3: Thống kê mô tả ---
# Chạy vòng lặp kiểm tra từng cột
