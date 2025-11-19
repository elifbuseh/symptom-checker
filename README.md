# 🩺 AI-Powered Symptom Checker (English Version)

> **⚠️ Disclaimer:** This project is for educational and informational purposes only. It does not replace professional medical diagnosis. Please consult a healthcare professional for health concerns.

**Machine Learning-Based Symptom Analysis Web Application**  
**GitHub Repository:** https://github.com/elifbuseh/symptom-checker  
**Branch:** main

---

## 📖 About the Project

Symptom Checker is a machine-learning-powered web application that allows users to select symptoms and receive predictions about possible diseases. The modern UI enables easy filtering, searching, and selection of symptoms.

A Python Flask backend processes input and uses a trained ML model to generate predictions.

---

## ✨ Features

- 🔍 **Smart Symptom Search:** Filter symptoms by their first letters  
- 🛒 **Dynamic Symptom Panel:** View and remove selected symptoms easily  
- 🎨 **Modern UI:** Built with React, animated, responsive  
- 🤖 **ML-Powered Prediction:** Uses a trained Scikit-learn model  
- 📱 **Overlay Result Screen:** Displays predictions without page reload  

---

## 🛠️ Technologies Used

### Frontend
- React.js  
- CSS3  

### Backend
- Python & Flask  
- Pandas & NumPy  
- Scikit-learn  
- Git LFS (large model files)  

---

## 🚀 Installation & Setup

### ⚙️ Prerequisites
- Node.js  
- Python  
- Git LFS  

---

### 1. Clone the Repository

```bash
git clone https://github.com/elifbuseh/symptom-checker.git
cd symptom-checker
```

---

### 2. Backend Setup

```bash
cd backend
```

Create virtual environment:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
python app.py
```

👉 Backend runs at: **http://localhost:5000**

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

👉 Frontend runs at: **http://localhost:3000**

---

## 📂 Project Structure

```text
symptom-checker/
├── backend/
│   ├── app.py              # Flask API
│   ├── model.pkl           # ML Model
│   ├── dataset/            # Data Files
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
└── README.md
```

---

## 🤝 Contributors

Thanks to the amazing contributors of this project:

- **Elif Buse Holozlu**  
- **Sude Güngör**  
- **Giray Bosna** 

---

## ⭐ Support

If you like this project, please ⭐ the repository!

---

# 🩺 AI Destekli Semptom Kontrol Uygulaması (Türkçe Sürüm)

> **⚠️ Uyarı:** Bu proje yalnızca eğitim amaçlıdır. Tıbbi teşhis yerine geçmez. Sağlık sorunlarınız için doktora danışınız.

**Makine Öğrenmesi Tabanlı Semptom Analizi Web Uygulaması**  
**GitHub Deposu:** https://github.com/elifbuseh/symptom-checker  
**Branch:** main

---

## 📖 Proje Hakkında

Symptom Checker, kullanıcıların seçtiği semptomlara göre olası hastalık tahminleri sunan makine öğrenmesi destekli bir web uygulamasıdır. Modern ve kullanıcı dostu arayüzü sayesinde semptomlar hızlıca aranabilir, filtrelenebilir ve seçilebilir.

Flask tabanlı backend, kullanıcıdan gelen verileri işleyerek eğitilmiş bir ML modeli ile tahmin üretir.

---

## ✨ Özellikler

- 🔍 **Akıllı Semptom Arama**  
- 🛒 **Dinamik Seçili Semptom Paneli**  
- 🎨 **Modern & Responsive Arayüz**  
- 🤖 **Makine Öğrenmesi ile Tahmin**  
- 📱 **Overlay Sonuç Gösterimi**  

---

## 🛠️ Kullanılan Teknolojiler

### Frontend
- React.js  
- CSS3  

### Backend
- Python & Flask  
- Pandas & NumPy  
- Scikit-learn  
- Git LFS  

---

## 🚀 Kurulum ve Çalıştırma

### ⚙️ Gereksinimler
- Node.js  
- Python  
- Git LFS  

---

### 1. Projeyi Klonlayın

```bash
git clone https://github.com/elifbuseh/symptom-checker.git
cd symptom-checker
```

---

### 2. Backend Kurulumu

```bash
cd backend
```

Sanal ortam:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Kurulum:

```bash
pip install -r requirements.txt
python app.py
```

👉 Backend adresi: **http://localhost:5000**

---

### 3. Frontend Kurulumu

```bash
cd frontend
npm install
npm start
```

👉 Frontend adresi: **http://localhost:3000**

---

## 📂 Proje Yapısı

```text
symptom-checker/
├── backend/
│   ├── app.py
│   ├── model.pkl
│   ├── dataset/
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
└── README.md
```

---

## 🤝 Katkıda Bulunanlar

Projeye katkı sağlayan ekip:

- **Elif Buse Holozlu**  
- **Sude Güngör**  
- **Giray Bosna**  

---

## ⭐ Destek

Projeyi beğendiysen yıldız bırakabilirsin ⭐

