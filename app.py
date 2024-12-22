from flask import Flask, render_template, request, jsonify
import pandas as pd
from fraud_detection import detect_fraud
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Process the uploaded file
        data = pd.read_excel(filepath)  # Assuming uploaded file is Excel
        fraud_results = detect_fraud(data)

        return jsonify(fraud_results.to_dict(orient='records'))
    return jsonify({'error': 'Something went wrong'})

if __name__ == '__main__':
    app.run(debug=True)
