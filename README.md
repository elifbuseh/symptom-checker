🩺 AI-Powered Symptom Checker
(English Version)

Machine Learning Based Symptom Analysis Web Application
GitHub Repository: https://github.com/elifbuseh/symptom-checker
 (branch: main)

⚠️ Disclaimer: This project is for educational and informational purposes only. It does not replace professional medical diagnosis. Please consult a healthcare professional for health concerns.



📖 About the Project

Symptom Checker is a machine learning powered web application that allows users to select symptoms and receive predictions about potential diseases.

With its modern and interactive UI, symptoms can be searched, filtered, selected, and viewed easily.
A Python Flask backend processes the input and interacts with a trained ML model to generate predictions.

✨ Features

🔍 Smart Symptom Search: Filter symptoms based on the first letters.

🛒 Dynamic Selected Symptoms Panel: View and remove selected symptoms instantly.

🎨 Modern UI: Clean, responsive, and animated interface built with React.

🤖 Machine Learning: Disease prediction via Scikit-learn model.

📱 Overlay Result Screen: Displays prediction results without refreshing the page.

🛠️ Technologies Used
Frontend

React.js

CSS3 (animations, transitions, responsive layout)

Backend

Python & Flask

Pandas & NumPy

Scikit-learn

Git LFS (for handling large model files)

🚀 Installation & Setup

⚙️ Prerequisites:

Node.js

Python

Git LFS

1. Clone the Project
git clone https://github.com/elifbuseh/symptom-checker.git
cd symptom-checker

2. Backend Setup
cd backend

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start server
python app.py


Backend runs at:
👉 http://localhost:5000

3. Frontend Setup

Open a new terminal:

cd frontend
npm install
npm start


Frontend runs at:
👉 http://localhost:3000

📂 Project Structure
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

🤝 Contributing

Fork the repository

Create a feature branch

git checkout -b new-feature


Commit changes

git commit -m "Added new feature"


Push your branch

git push origin new-feature


Create a Pull Request 🎉

⭐ Support

If you like this project, feel free to star the repo!

🩺 AI Destekli Semptom Kontrol Uygulaması
(Türkçe Sürüm)

Makine Öğrenmesi Tabanlı Semptom Analizi Web Uygulaması
GitHub Deposu: https://github.com/elifbuseh/symptom-checker
 (branch: main)

⚠️ Uyarı: Bu proje sadece eğitim ve bilgilendirme amaçlıdır. Tıbbi teşhis yerine geçmez. Sağlık sorunlarınız için bir uzmana başvurunuz.



📖 Proje Hakkında

Symptom Checker, kullanıcıların yaşadıkları semptomları seçerek olası hastalık tahminleri almasını sağlayan makine öğrenmesi tabanlı bir web uygulamasıdır.

Modern arayüzü sayesinde semptomlar hızlıca aranabilir, filtrelenebilir, seçilebilir ve yönetilebilir.
Arka plandaki Python Flask API, eğitilmiş makine öğrenmesi modeli ile tahminleri üretir.

✨ Özellikler

🔍 Akıllı Semptom Arama: Semptomları baş harfine göre filtreleme.

🛒 Dinamik Seçim Paneli: Seçilen semptomları tek tıkla görüntüleme ve kaldırma.

🎨 Modern UI: React ile geliştirilmiş, estetik ve mobil uyumlu tasarım.

🤖 Makine Öğrenmesi Entegrasyonu: Scikit-learn modeli ile tahmin işlemi.

📱 Overlay Sonuç Paneli: Sayfa yenilemeden modern sonuç gösterimi.

🛠️ Kullanılan Teknolojiler
Frontend

React.js

CSS3 (animasyon, geçişler, responsive yapı)

Backend

Python & Flask

Pandas & NumPy

Scikit-learn

Git LFS (büyük model dosyası için)

🚀 Kurulum ve Çalıştırma

⚙️ Gereksinimler:

Node.js

Python

Git LFS

1. Projeyi Klonlayın
git clone https://github.com/elifbuseh/symptom-checker.git
cd symptom-checker

2. Backend Kurulumu
cd backend

# Sanal ortam (opsiyonel fakat önerilir)
python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Bağımlılıkların yüklenmesi
pip install -r requirements.txt

# Sunucuyu başlatma
python app.py


Backend adresi:
👉 http://localhost:5000

3. Frontend Kurulumu

Yeni bir terminal açın:

cd frontend
npm install
npm start


Frontend adresi:
👉 http://localhost:3000

📂 Proje Yapısı
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

🤝 Katkıda Bulunma

Repoyu forklayın

Yeni bir branch oluşturun

git checkout -b yeni-ozellik


Değişiklikleri commit edin

git commit -m "Yeni özellik eklendi"


Branch'i pushlayın

git push origin yeni-ozellik


Pull Request açın 🎉

⭐ Destek

Projeyi beğendiysen yıldız verebilirsin ⭐
