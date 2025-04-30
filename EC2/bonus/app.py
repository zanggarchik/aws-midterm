from flask import Flask, request, jsonify
from transformers import pipeline

# Инициализация Flask приложения
app = Flask(__name__)

# Загрузка модели для анализа настроений
sentiment_analyzer = pipeline("sentiment-analysis")

# Определение API endpoint
@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    # Получаем текст из запроса
    text = request.json.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Получаем результат анализа настроений
    result = sentiment_analyzer(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
