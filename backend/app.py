# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import json
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # React'in API'ye erişmesi için

# Model ve semptom listesini yükle
try:
    model = joblib.load('model.pkl')
    with open('symptoms.json', 'r') as f:
        raw_symptoms = json.load(f)

    # 🔥 ÖNEMLİ: String olmayanları temizle (replace hatasını çözmesi için)
    model_symptoms = [
        s for s in raw_symptoms
        if isinstance(s, str) and s.strip() != ""
    ]

    print("Model ve semptom listesi yüklendi (temizlendi).")

except FileNotFoundError:
    print("HATA: 'model.pkl' veya 'symptoms.json' bulunamadı.")
    exit()


# ✔ Endpoint 1: Temizlenmiş semptomları frontend'e gönder
@app.route('/getsymptoms', methods=['GET'])
def get_symptoms():
    return jsonify(model_symptoms)


# ✔ Endpoint 2: Tahmin işlemi
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Frontend'den gelen semptom listesi
    user_symptoms = data.get('symptoms', [])

    # 🔥 Güvenlik: String olmayan değerleri ayıkla
    user_symptoms = [
        s for s in user_symptoms
        if isinstance(s, str) and s.strip() != ""
    ]

    # Model için 0/1 vektörü oluştur
    input_vector = [0] * len(model_symptoms)

    for symptom in user_symptoms:
        if symptom in model_symptoms:
            idx = model_symptoms.index(symptom)
            input_vector[idx] = 1

    # Tahmin
    prediction = model.predict([input_vector])

    return jsonify({'disease': prediction[0]})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
