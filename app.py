import requests
from flask import Flask, render_template, request, session
from secrets import token_hex

app = Flask(__name__)
# Cần có SECRET_KEY để sử dụng session
app.config['SECRET_KEY'] = token_hex(16)

# DÁN PRODUCTION URL CỦA BẠN VÀO ĐÂY
N8N_WEBHOOK_URL = "http://localhost:5678/webhook/6950c3ea-b460-418a-85cc-ac9ac69fa032" 

@app.route('/', methods=['GET'])
def index():
    # Xóa lịch sử chat cũ khi tải lại trang chủ
    session.pop('chat_history', None)
    # Khởi tạo lịch sử với tin nhắn chào mừng
    initial_message = {
        "type": "bot", 
        "text": "Xin chào! Tôi có thể giúp gì cho bạn về nhà hàng của chúng tôi?"
    }
    session['chat_history'] = [initial_message]
    return render_template('index.html', history=session.get('chat_history'))

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form.get('question')
    
    # Lấy lịch sử chat từ session
    chat_history = session.get('chat_history', [])
    
    # Thêm câu hỏi của người dùng vào lịch sử
    chat_history.append({"type": "user", "text": user_question})

    # Tạo một sessionId duy nhất cho mỗi phiên
    if 'sessionId' not in session:
        session['sessionId'] = 'flask_session_' + token_hex(8)

    bot_answer_text = "Xin lỗi, có lỗi xảy ra."

    if user_question:
        payload = {
            "question": user_question,
            "sessionId": session.get('sessionId')
        }
        
        try:
            # Gọi đến n8n webhook
            response = requests.post(N8N_WEBHOOK_URL, json=payload)
            response.raise_for_status() 
            data = response.json()
            bot_answer_text = data.get('answer', 'Không nhận được câu trả lời hợp lệ.')
        except requests.exceptions.RequestException as e:
            print(f"Error calling n8n: {e}")
            bot_answer_text = "Lỗi kết nối đến trợ lý ảo, vui lòng thử lại sau."

    # Thêm câu trả lời của bot vào lịch sử
    chat_history.append({"type": "bot", "text": bot_answer_text})
    
    # Lưu lại lịch sử vào session
    session['chat_history'] = chat_history
    
    return render_template('index.html', history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)