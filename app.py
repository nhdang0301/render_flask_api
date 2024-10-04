import re
import numpy as np
from gensim import corpora
from gensim.models import LdaModel
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from flask import Flask, request, jsonify

# Tải các gói NLTK cần thiết
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

# Hàm tiền xử lý văn bản


def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)


# Tải mô hình LDA đã lưu
lda_gensim_model = LdaModel.load('model/lda_model.model')
print("Mô hình LDA đã được tải thành công!")

# Tải từ điển đã lưu
dictionary = corpora.Dictionary.load('model/dictionary.dict')

# Định nghĩa endpoint phân loại văn bản


@app.route('/classify', methods=['POST'])
def classify_text():
    data = request.json
    new_text = data.get('text', '')

    # Tiền xử lý văn bản mới
    processed_text = preprocess_text(new_text)

    # Chuyển đổi văn bản mới thành dạng bag-of-words dựa trên từ điển đã huấn luyện
    bow_vector = dictionary.doc2bow(processed_text.split())

    # Dự đoán chủ đề cho văn bản mới
    topics = lda_gensim_model.get_document_topics(bow_vector)

    # Tìm chủ đề có xác suất cao nhất
    max_topic = None
    max_prob = 0
    topic_details = []

    for topic_id, prob in topics:
        # Chuyển đổi thành float
        topic_details.append(
            {'topic': topic_id + 1, 'probability': float(prob)})
        if prob > max_prob:
            max_prob = prob
            max_topic = topic_id + 1

    # Tạo phản hồi JSON
    response = {
        'topics': topic_details,
        # Chuyển đổi thành float
        'conclusion': f'Văn bản thuộc về chủ đề {max_topic} với xác suất cao nhất là {float(max_prob)}.'
    }
    return jsonify(response)


# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
