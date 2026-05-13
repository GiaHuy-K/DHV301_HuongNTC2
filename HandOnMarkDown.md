# Hướng Dẫn Sử Dụng Markdown Cơ Bản

Markdown là một ngôn ngữ đánh dấu nhẹ giúp bạn định dạng văn bản một cách nhanh chóng và chuyên nghiệp. Dưới đây là các cú pháp phổ biến nhất:

## 1. Tiêu đề (Headings)
Sử dụng ký tự `#` ở đầu dòng. Số lượng dấu `#` tương ứng với cấp độ tiêu đề.
# Tiêu đề H1
## Tiêu đề H2
### Tiêu đề H3
#### Tiêu đề H4

---

## 2. Định dạng văn bản (Text Formatting)
- **Chữ đậm**: Bao quanh văn bản bằng `**`. Ví dụ: **Đây là chữ đậm**.
- *Chữ nghiêng*: Bao quanh văn bản bằng `*`. Ví dụ: *Đây là chữ nghiêng*.
- ***Đậm và nghiêng***: Sử dụng `***`.

---

## 3. Danh sách (Lists)

### Danh sách không thứ tự
Sử dụng dấu `-`, `*` hoặc `+`:
- Mục thứ nhất
- Mục thứ hai
  - Mục con 2a

### Danh sách có thứ tự
Sử dụng số kèm dấu chấm:
1. Bước một
2. Bước hai
3. Bước ba

---

## 4. Chèn Code (Code Blocks)

### Code Inline
Dùng dấu ` để đánh dấu một đoạn code nhỏ trong câu. 
Ví dụ: `print("Hello World")`

### Khối Code (Code Block)
Dùng ba dấu backtick (```) để bao quanh nhiều dòng code:

```python
import pandas as pd
df = pd.read_csv("titanic.csv")
print(df.head())