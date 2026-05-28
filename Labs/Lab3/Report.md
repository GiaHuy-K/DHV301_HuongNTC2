### 1. Data Quality Report
| Metric | Value |
| :--- | :--- |
| **Total Rows** | 13 |
| **Total Columns** | 12 |
| **Data Health Status** | **Poor** |

### 2. Data Issue Log
| issue_id | field | issue type | example | count | percentage | impact level | suggested treatment |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ISS01 | quantity | Missing value | blank | 1 | 7.69% | Medium | Impute median |
| ISS02 | customer_age | Missing value | blank | 2 | 15.38% | Medium | Impute median |
| ISS03 | status | Missing value | blank | 1 | 7.69% | Medium | Gán "Unknown" |
| ISS04 | All | Duplicate rows | O009 | 1 | 7.69% | High | drop_duplicates() |
| ISS05 | gender | Inconsistent | M, Male | 6 | - | Low | Mapping chuẩn |
| ISS06 | region | Inconsistent | north, North | 4 | - | Low | str.title() |
| ISS07 | order_date | Invalid date | not_a_date | 2 | 15.38% | High | to_datetime |
| ISS08 | customer_age | Invalid value | -5, 150 | 2 | 15.38% | High | Range [18-90] |
| ISS09 | unit_price | Invalid value | 0.0 | 1 | 7.69% | High | Verify price |
| ISS10 | discount | Out-of-range | 1.2 | 1 | 7.69% | High | Cap at 1.0 |

### 3. Top 3 Issues
| Priority | Issue | Reason |
| :--- | :--- | :--- |
| 1 | Duplicates | Tránh sai lệch doanh thu |
| 2 | Invalid Numbers | Đảm bảo tính toán đúng |
| 3 | Invalid Dates | Phân tích xu hướng thời gian |