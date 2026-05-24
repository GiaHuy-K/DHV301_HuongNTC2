# Decision Log - Dự án Phân tích Khảo sát Lương

Dưới đây là các quyết định quan trọng trong quá trình xử lý dữ liệu (Data Cleaning) để đảm bảo tính chính xác và chiều sâu cho các phân tích tiếp theo.

---

## 1. Quyết định xử lý: Cột 'annual_salary' — Missing 14%

**Quan sát**: 391 hàng bị thiếu (NaN). Dữ liệu lương thường không phân phối chuẩn mà bị lệch phải (Right-skewed) do một số ít người có thu nhập rất cao.

**Giả thuyết về nguyên nhân**: 
- Khả năng **MNAR (Missing Not At Random)** cao: Những người có thu nhập ở mức cực thấp hoặc cực cao thường có xu hướng giữ bí mật thông tin tài chính.

**Phương án đã xem xét**:
1. **Fillna(mean)**: Bị loại bỏ vì giá trị trung bình sẽ bị kéo cao bởi các outliers, làm sai lệch mức lương thực tế của đa số.
2. **Fillna(global_median)**: Đơn giản nhưng bỏ qua ngữ cảnh ngành nghề (ví dụ: lương ngành Tech khác ngành Giáo dục).

**Quyết định**: **Phương án 3 - Fillna bằng Median theo từng ngành (Industry)**.
**Lý do**: Mức lương phụ thuộc chặt chẽ vào lĩnh vực làm việc. Dùng trung vị ngành giúp bảo toàn tính đặc trưng của dữ liệu và hạn chế ảnh hưởng của giá trị ngoại lai.

---

## 2. Quyết định xử lý: Cột 'country' — Missing 4.1%

**Quan sát**: Nhiều hàng thiếu quốc gia nhưng lại có thông tin ở cột `us_state`.

**Giả thuyết về nguyên nhân**:
- Người dùng mặc định rằng khi đã chọn Bang (State) của Mỹ thì không cần điền lại quốc gia "United States".

**Phương án đã xem xét**:
1. **Drop hàng null**: Làm mất đi 4.1% dữ liệu về lương và kinh nghiệm quý giá.
2. **Fillna(mode)**: Có rủi ro sai lệch cho các mẫu ngoài nước Mỹ (UK, Canada...).

**Quyết định**: **Xử lý bắc cầu (Logic-based Imputation)**. 
- Nếu `us_state` không trống -> Điền `country` là "United States".
- Các trường hợp còn lại mới điền theo giá trị xuất hiện nhiều nhất (mode).

**Lý do**: Sử dụng mối tương quan giữa các cột để khôi phục dữ liệu một cách chính xác và khoa học nhất thay vì chỉ dựa vào xác suất thống kê.

---

## 3. Quyết định xử lý: Cột 'additional_monetary_comp' — Missing 55.1%

**Quan sát**: Hơn một nửa dataset không có thông tin thu nhập thêm.

**Giả thuyết về nguyên nhân**: 
- Khả năng **MAR (Missing At Random)**: Trong khảo sát, nếu không có thưởng/hoa hồng, người dùng thường để trống thay vì nhập số 0.

**Phương án đã xem xét**:
1. **Drop hàng null**: Loại bỏ hơn 50% dữ liệu -> Không thể thực hiện.
2. **Fillna(median)**: Sai lệch bản chất vì thực tế đa số người tham gia chỉ nhận lương cứng.

**Quyết định**: **Chuyển về dạng số (Numeric) và điền các giá trị trống bằng 0**.
**Lý do**: Để phản ánh đúng bản chất kinh tế. Việc điền số 0 giúp tính toán "Tổng thu nhập" (Lương + Thưởng) cho toàn bộ dataset được chính xác.
