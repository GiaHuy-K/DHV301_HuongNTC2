import pandas as pd
import os

# --- 1. LOAD DATA ---
# Sử dụng os.path để tránh lỗi FileNotFoundError bất kể bạn chạy code từ đâu
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "dataset", "salary_survey_raw.csv")

df = pd.read_csv(file_path)

# --- 2. XỬ LÝ DTYPE (Ép kiểu) ---
# Xử lý các cột tiền tệ: đảm bảo chuyển về string trước khi replace để tránh lỗi với NaN
cols_money = ['annual_salary', 'additional_monetary_comp']
for col in cols_money:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(r'[^\d.]', '', regex=True), errors='coerce')

# --- 3. XỬ LÝ MISSING VALUE ---

# 3.1 Lương: Median theo ngành (Tối ưu: Nếu ngành đó null hết, thì lấy median tổng)
industry_median = df.groupby('industry')['annual_salary'].transform('median')
global_median = df['annual_salary'].median()
df['annual_salary'] = df['annual_salary'].fillna(industry_median).fillna(global_median)

# 3.2 Thưởng: Những người để trống mặc định là không có (0)
df['additional_monetary_comp'] = df['additional_monetary_comp'].fillna(0)

# 3.3 Quốc gia & Bang: 
df['country'] = df['country'].str.strip().str.title()
# Logic bắc cầu: Nếu có bang Mỹ thì chắc chắn quốc gia là USA
df.loc[df['us_state'].notnull() & df['country'].isnull(), 'country'] = 'United States'
df['country'] = df['country'].fillna(df['country'].mode()[0])

# 3.4 Nhân khẩu học: Điền giá trị trung lập 
df['gender'] = df['gender'].fillna('Other')
df['race'] = df['race'].fillna('Prefer not to answer')

# 3.5 Các cột ngữ cảnh (Context): Điền nhãn để giữ lại dữ liệu hàng đó
context_cols = ['income_context', 'additional_context_on_job_title', 'city', 'us_state']
for col in context_cols:
    df[col] = df[col].fillna('Unknown/None')

# --- 4. XỬ LÝ DUPLICATE ---
df.drop_duplicates(inplace=True)

# --- 5. LƯU DATASET SAU XỬ LÝ ---
output_path = os.path.join(base_path, "dataset", "salary_survey_cleaned.csv")
df.to_csv(output_path, index=False)
print(f"--- Đã lưu dataset sau khi xử lí tại: {output_path} ---")

# --- 6. HÀM Missing Report ---
def missing_report(df):
    miss = df.isnull().sum()
    if miss.sum() == 0:
        return "\nKết quả: Dataset sạch, không còn giá trị null nào!"
    pct = (miss / len(df) * 100).round(1)
    report = pd.concat([miss, pct], axis=1, keys=['Missing Count', 'Percentage (%)'])
    return report[report['Missing Count'] > 0].sort_values('Percentage (%)', ascending=False)

print(missing_report(df))