from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Charge le fichier HTML depuis le dossier templates

@app.route('/generate_password', methods=['POST'])
def generate_password():
    data = request.json
    length = data.get('length', 8)
    use_digits = data.get('digits', True)
    use_specials = data.get('specials', True)

    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)

