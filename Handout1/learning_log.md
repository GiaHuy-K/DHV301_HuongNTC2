# Các lỗi gặp phải
1. ModuleNotFound của Parquet: 
* Mô tả lỗi :Khi chạy thử dữ liệu thì không tìm thấy các module như pyarrow,...
* Nơi tìm giải pháp: Gemini + google
* Kết quả : đã fix được
* lý do : khi pip install các module đã quên active môi trường ảo nên chỉ là tải về python global.
Đó chính là lý do jupyter notebook không tìm được

# Điều học được ngoài bài: Setup môi trường phải thật cẩn thận, nếu không bạn sẽ mất mấy tiếng với đống lỗi từ .venv.

1. Điều khó nhất khi học python và pandas hiện nay chính là hàm setup môi trường.
2. Điều thú vị nhất chính là các hàm xử lí của python quá nhiều để tìm hiểu, cần thời gian rất nhiều.
3. Câu hỏi về titanic khoang ở mũi tàu của tôi vẫn chưa có câu trả lời.