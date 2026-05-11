import pandas as pd
import seaborn as sns
import os

df = sns.load_dataset('titanic')

# --- CÂU 1: Load dataset và in 5 dòng đầu ---
print("--- Câu 1 ---")
print(df.head())
print(f"Tổng cộng có {len(df)} hành khách.")
print(df.shape)

# --- CÂU 2: Kiểm tra kiểu dữ liệu và giá trị NULL ---
print("\n--- Câu 2 ---")
df.info()
null_counts = df.isnull().sum()
print("\nSố lượng giá trị null ở mỗi cột:")
print(null_counts[null_counts > 0])
max_null_col = null_counts.idxmax()
print(f"Cột có nhiều giá trị null nhất là: {max_null_col} ({null_counts.max()} giá trị)")

# --- CÂU 3: Thống kê mô tả ---
print("\n--- Câu 3 ---")
description = df.describe()
print(description)
mean_age = df['age'].mean()
max_fare = df['fare'].max()
print(f"Tuổi trung bình: {mean_age:.2f} tuổi.")
print(f"Giá vé cao nhất: {max_fare:.2f}")

# --- CÂU 4: Đếm số lượng nam/nữ ---
print("\n--- Câu 4 ---")
gender_counts = df['sex'].value_counts()
print("Số lượng hành khách theo giới tính:")
print(gender_counts)

# --- CÂU 5: Thống kê hạng vé (pclass) ---
print("\n--- Câu 5 ---")
pclass_counts = df['pclass'].value_counts()
pclass_percent = df['pclass'].value_counts(normalize=True) * 100

print("Số lượng mỗi hạng vé:")
print(pclass_counts)
print("\nTỉ lệ phần trăm mỗi hạng vé:")
print(pclass_percent.map('{:.2f}%'.format))
print(f"Hành khách đi hạng {pclass_counts.idxmax()} là nhiều nhất.")

# --- CÂU 6: Lọc hành khách nữ và tính tỉ lệ % ---
print("\n--- Câu 6 ---")
# Lọc ra danh sách hành khách nữ
female_df = df[df['sex'] == 'female']
num_female = len(female_df)

percent_female = (num_female / len(df)) * 100

print(f"Số lượng hành khách nữ: {num_female}")
print(f"Tỉ lệ hành khách nữ chiếm: {percent_female:.2f}%")


# --- CÂU 7: Lọc hạng 1 và tính giá vé trung bình ---
print("\n--- Câu 7 ---")
# Lọc hành khách đi hạng 1 (pclass = 1)
first_class_df = df[df['pclass'] == 1]
avg_fare_class1 = first_class_df['fare'].mean()

print(f"Số lượng hành khách hạng 1: {len(first_class_df)}")
print(f"Giá vé trung bình của hạng 1: {avg_fare_class1:.2f} USD")


# --- CÂU 8: Thống kê theo độ tuổi ---
print("\n--- Câu 8 ---")
# Lọc hành khách dưới 18 tuổi
under_18 = df[df['age'] < 18]
# Lọc hành khách trên 60 tuổi
over_60 = df[df['age'] > 60]

print(f"Số hành khách dưới 18 tuổi (Trẻ em): {len(under_18)}")
print(f"Số hành khách trên 60 tuổi (Người già): {len(over_60)}")