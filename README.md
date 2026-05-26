# DHV301
## 1. Danh sách các thư viện 

| Nhóm chức năng | Các thư viện sử dụng |
| :--- | :--- |
| **Data Processing** | `numpy`, `pandas` |
| **Visualization** | `matplotlib` |
| **Machine Learning** | `scikit-learn`, `statsmodels`, `prophet`, `surprise` |
| **Deep Learning** | `torch`, `torchvision`, `torchmetrics` |
| **Web API & Deployment** | `flask`, `fastapi`, `uvicorn` |
| **MLOps & Testing** | `mlflow`, `evidently`, `pytest` |
| **Utilities** | `joblib`, `pathlib`, `gensim` |

---
## 2 Cài đặt & Chạy dự án
### Yêu cầu hệ thống
- Python 3.9+ (Khuyên dùng 3.10)
- Trình quản lý gói `pip`

### Thiết lập môi trường 

1. Bước 1: Tạo môi trường ảo
Mở Terminal tại thư mục dự án và chạy:
```bash
python -m venv .venv
```
2. Bước 2: Kích hoạt môi trường
- **Windows (PowerShell):**
```
.\.venv\Scripts\Activate
```
- **Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```  
- **Mac/Linux::**
 ```cmd
 source .venv/bin/activate 
```

3. Bước 3: Cài đặt các thư viện cần thiết
Cài đặt toàn bộ danh sách thư viện từ file `requirements.txt`:
```bash
pip install -r requirements.txt
```