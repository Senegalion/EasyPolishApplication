from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
generator = pipeline("text2text-generation", model="sdadas/byt5-text-correction")

@app.route('/correct', methods=['POST'])
def correct_text():
    if request.is_json:
        data = request.get_json()
        sentences = data.get("sentences", [])
        corrected_sentences = generator(sentences, max_length=512)
        corrected_texts = [s['generated_text'] for s in corrected_sentences]
        return jsonify({"correctedText": corrected_texts})
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)