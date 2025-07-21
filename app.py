# Import thư viện
from flask import Flask, render_template, request, jsonify
from chat import get_response
# Khởi tạo flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
# Xử lí tin nhắn ngườii dùng
@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.form.get("msg")
    response = get_response(user_message)
    return jsonify(response)
# Chạy ứng dụng flask
if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 8080)
