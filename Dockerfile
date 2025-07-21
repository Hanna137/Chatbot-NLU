# Sử dụng image Python 3.9 thay vì 3.13 để tăng tính tương thích
FROM python:3.9-slim-buster 

# Đặt thư mục làm việc
WORKDIR /chatbot-app

# Sao chép file requirements.txt
COPY requirements.txt .

# Cài đặt dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép tất cả file source code vào container
COPY . .

# Chạy ứng dụng
CMD ["python", "app.py"]
