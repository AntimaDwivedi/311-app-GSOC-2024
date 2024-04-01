from flask import Flask ,request ,jsonify

from huggingface import translate, translate_portuguese

app = Flask(__name__)

@app.route('/translation/ar' ,methods=['GET'])
def arabic_translator():
    data = request.get_data()
    input_text = str(data, 'UTF-8')
    target_language = 'ar'
    translated_text = translate(input_text, target_language)
    return jsonify("Language - arabic  " + translated_text)

@app.route('/translation/fr' ,methods=['GET'])
def french_translator():
    data = request.get_data()
    input_text = str(data, 'UTF-8')
    target_language = 'fr'
    translated_text = translate(input_text, target_language)
    return jsonify("Language - french  " + translated_text)

@app.route('/translation/ru' ,methods=['GET'])
def russian_translator():
    data = request.get_data()
    input_text = str(data, 'UTF-8')
    target_language = 'ru'
    translated_text = translate(input_text, target_language)
    return jsonify("Language - russian  " + translated_text)

@app.route('/translation/pt' ,methods=['GET'])
def portuguese_translator():
    data = request.get_data()
    input_text = str(data, 'UTF-8')
    target_language = 'pt'
    translated_text = translate_portuguese(input_text)
    return jsonify("Language - portugueses  " + translated_text)

app.run(debug = True)