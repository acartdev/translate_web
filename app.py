from flask import Flask, render_template, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

language_codes = list(LANGUAGES.keys())
language_names = list(LANGUAGES.values())

@app.route('/')
def index():
    return render_template('index.html', source_languages=zip(language_codes, language_names), target_languages=zip(language_codes, language_names))

@app.route('/translate', methods=['POST'])
def translate_text():
    text_to_translate = request.form.get('text')
    source_language = request.form.get('source_language')
    target_language = request.form.get('target_language')

    if not text_to_translate or not source_language or not target_language:
        return jsonify({'translation': 'Please provide valid input.'})

    translator = Translator()
    try:
        translation = translator.translate(text_to_translate, src=source_language, dest=target_language).text
    except Exception as e:
        print(f"Translation error: {e}")
        translation = "Translation failed. Please try again later."

    return jsonify({'translation': translation})

@app.route('/pronounce', methods=['POST'])
def pronounce_text():
    text = request.json.get('text')
    if text:
        return jsonify({'message': 'Text pronounced successfully!'})
    else:
        return jsonify({'message': 'Text not provided for pronunciation.'})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
    