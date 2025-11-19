// frontend/src/App.js
import React, { useState, useEffect, useMemo } from 'react';
import './App.css';
import symptomTranslations from './symptomTranslations.json';   // Semptom sözlüğü
import diseaseTranslationsRaw from './diseaseTranslations.json';   // Hastalık sözlüğü (ham)

// ✅ 1) HASTALIK SÖZLÜĞÜNÜ NORMALİZE ET
// Tüm key'leri: lowercase + '_'→' ' + birden fazla boşluk→tek boşluk + trim
const buildDiseaseMap = (raw) => {
  const map = {};
  Object.entries(raw).forEach(([key, value]) => {
    const normKey = key
      .toString()
      .toLowerCase()
      .replace(/_/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();

    map[normKey] = value;
  });
  return map;
};

const diseaseTranslations = buildDiseaseMap(diseaseTranslationsRaw);

/* ================== 1) DİL METİNLERİ ================== */
const texts = {
  en: {
    title: 'Symptom Checker',
    subtitle: 'Please select the symptoms you are experiencing:',
    selectedPlaceholder: 'Selected symptoms will appear here...',
    lettersAll: 'All',
    predictButton: 'Predict Condition',
    predicting: 'Predicting...',
    loadingSymptoms: 'Loading symptoms... (Is the backend running?)',
    resultTitle: 'Prediction Results',
    resultPossible: 'Possible Condition:',
    disclaimerTitle: 'Disclaimer:',
    disclaimerText:
      'This is not a medical diagnosis. The information provided is a prediction based on a machine learning model. Always consult a healthcare professional for an accurate diagnosis and treatment.',
    noResultWithSymptoms:
      "Select symptoms and click 'Predict' to see possible conditions.",
    noSymptomsSelected:
      'No symptoms selected yet. Please select at least one symptom.',
    analyzing: 'Analyzing your symptoms...',
    langLabel: 'Language',
    themeLabel: 'Theme',
    themeLight: 'Light',
    themeDark: 'Dark',
    showResults: 'Show results',
    hideResults: 'Hide results',
  },
  tr: {
    title: 'Semptom Kontrolü',
    subtitle: 'Lütfen yaşadığın semptomları seç:',
    selectedPlaceholder: 'Seçtiğin semptomlar burada görünecek...',
    lettersAll: 'Tümü',
    predictButton: 'Olası Hastalığı Tahmin Et',
    predicting: 'Tahmin ediliyor...',
    loadingSymptoms: 'Semptomlar yükleniyor... (Backend çalışıyor mu?)',
    resultTitle: 'Tahmin Sonuçları',
    resultPossible: 'Olası Durum / Hastalık:',
    disclaimerTitle: 'Uyarı:',
    disclaimerText:
      'Bu bir tıbbi tanı değildir. Gösterilen bilgi, makine öğrenmesi modeline dayalı bir tahmindir. Doğru tanı ve tedavi için mutlaka bir sağlık profesyoneline başvurun.',
    noResultWithSymptoms:
      "Semptomları seçip 'Olası Hastalığı Tahmin Et' tuşuna basarak sonucu görebilirsin.",
    noSymptomsSelected: 'Henüz semptom seçmedin. Lütfen en az bir semptom seç.',
    analyzing: 'Semptomların analiz ediliyor...',
    langLabel: 'Dil',
    themeLabel: 'Tema',
    themeLight: 'Açık',
    themeDark: 'Koyu',
    showResults: 'Sonuçları göster',
    hideResults: 'Sonuçları gizle',
  },
};

/* ================== 2) SEMPTOM ADINI DİLE GÖRE SEÇEN FONKSİYON ================== */
const getSymptomLabel = (symptom, language) => {
  const entryExact = symptomTranslations[symptom];
  const entryLower = symptomTranslations[symptom.toLowerCase()];
  const entry = entryExact || entryLower;

  const base = symptom.replace(/_/g, ' ');
  if (!entry) return base;

  const langKey = language === 'tr' ? 'tr' : 'en';
  return entry[langKey] || base;
};

/* ================== 2.5) HASTALIK ADINI DİLE GÖRE SEÇEN FONKSİYON ================== */
/* ================== 2.5) HASTALIK ADINI DİLE GÖRE SEÇEN FONKSİYON ================== */
const getDiseaseLabel = (disease, language) => {
  if (!disease || typeof disease !== 'string') return '';

  // normalize: tüm stringleri aynı forma sok
  const normalize = (str) =>
    str
      .toString()
      .replace(/\v/g, '')      // gizli dikey boşlukları sil
      .replace(/_/g, ' ')      // alt çizgi -> boşluk
      .replace(/\s+/g, ' ')    // birden fazla boşluk -> tek boşluk
      .toLowerCase()
      .trim();

  const normDisease = normalize(disease);

  // buildDiseaseMap sayesinde diseaseTranslations'ın key'leri zaten normalize edilmiş durumda
  const foundEntry = diseaseTranslations[normDisease];

  const base = disease.replace(/_/g, ' ');

  // DEBUG için: çeviri yoksa console'a yaz
  if (!foundEntry) {
    console.log('Çeviri bulunamadı:', normDisease);
    return base;
  }

  const langKey = language === 'tr' ? 'tr' : 'en';
  return foundEntry[langKey] || base;
};


/* ================== 3) ANA KOMPONENT ================== */
function App() {
  const [allSymptoms, setAllSymptoms] = useState([]);
  const [selectedSymptoms, setSelectedSymptoms] = useState(new Set());
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const [isResultClosed, setIsResultClosed] = useState(true);
  const [activeFilter, setActiveFilter] = useState('All');

  const [language, setLanguage] = useState('en'); // 'en' veya 'tr'
  const [theme, setTheme] = useState('light');    // 'light' veya 'dark'

  const t = texts[language];

  // Alfabeler
  const alphabetEn = ['All', ...'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')];
  const alphabetTr = [
    'All',
    'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H',
    'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P',
    'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z',
  ];
  const alphabet = language === 'tr' ? alphabetTr : alphabetEn;

  // Semptomları backend'den çek
  useEffect(() => {
    fetch('http://localhost:5000/getsymptoms')
      .then((res) => res.json())
      .then((data) => {
        setAllSymptoms(data.sort());
      })
      .catch((err) => {
        console.error('API bağlantı hatası veya semptomlar yüklenemedi:', err);
      });
  }, []);

  // Semptoma tıklama
  const handleSymptomClick = (symptom) => {
    const newSelection = new Set(selectedSymptoms);
    if (newSelection.has(symptom)) {
      newSelection.delete(symptom);
    } else {
      newSelection.add(symptom);
    }
    setSelectedSymptoms(newSelection);
  };

  // Tahmin isteği
  const handlePredict = async () => {
    setLoading(true);
    setResult(null);
    setIsResultClosed(false);

    const symptomsArray = Array.from(selectedSymptoms);

    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ symptoms: symptomsArray }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const cleanDisease = data.disease.replace(/\v/g, '');
      setResult(cleanDisease);
    } catch (error) {
      console.error('Tahmin alınırken hata oluştu:', error);
      setResult('Error occurred during prediction. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // A–Z filtre (görünen dile göre filtreliyoruz)
  const filteredSymptoms = useMemo(() => {
    if (activeFilter === 'All') {
      return allSymptoms;
    }
    const letter = activeFilter.toLowerCase();
    return allSymptoms.filter((symptom) => {
      const label = getSymptomLabel(symptom, language).toLowerCase();
      return label.startsWith(letter);
    });
  }, [allSymptoms, activeFilter, language]);

  return (
    <div
      className={`app-main-container ${isResultClosed ? 'results-closed' : ''} ${theme}`}
    >
      {/* Sonuç panelini açma butonu */}
      <button
        className="open-results-button"
        onClick={() => setIsResultClosed(false)}
        aria-label={t.showResults}
      >
        ❮
      </button>

      {/* SOL: Semptom alanı */}
      <div className="symptom-section">
        {/* Üstte dil ve tema kontrolleri */}
        <div className="top-controls">
          <div className="control-group">
            <span>{t.langLabel}:</span>
            <button
              className={`small-toggle-btn ${language === 'tr' ? 'active' : ''}`}
              onClick={() => setLanguage('tr')}
            >
              TR
            </button>
            <button
              className={`small-toggle-btn ${language === 'en' ? 'active' : ''}`}
              onClick={() => setLanguage('en')}
            >
              EN
            </button>
          </div>

          <div className="control-group">
            <span>{t.themeLabel}:</span>
            <button
              className={`small-toggle-btn ${theme === 'light' ? 'active' : ''}`}
              onClick={() => setTheme('light')}
            >
              {t.themeLight}
            </button>
            <button
              className={`small-toggle-btn ${theme === 'dark' ? 'active' : ''}`}
              onClick={() => setTheme('dark')}
            >
              {t.themeDark}
            </button>
          </div>
        </div>

        <h1>{t.title}</h1>
        <p>{t.subtitle}</p>

        {/* Seçili semptomlar alanı */}
        <div className="selected-symptoms-container">
          {selectedSymptoms.size === 0 ? (
            <span className="selected-symptoms-placeholder">
              {t.selectedPlaceholder}
            </span>
          ) : (
            Array.from(selectedSymptoms).map((symptom) => (
              <div key={symptom} className="selected-symptom-tag">
                {getSymptomLabel(symptom, language)}
                <button
                  className="remove-symptom-btn"
                  onClick={() => handleSymptomClick(symptom)}
                >
                  &times;
                </button>
              </div>
            ))
          )}
        </div>

        {/* A–Z filtre butonları */}
        <div className="letter-filter">
          {alphabet.map((letter) => (
            <button
              key={letter}
              className={activeFilter === letter ? 'active' : ''}
              onClick={() => setActiveFilter(letter)}
            >
              {letter === 'All' ? t.lettersAll : letter}
            </button>
          ))}
        </div>

        {/* Semptom listesi */}
        <div className="symptom-grid">
          {allSymptoms.length === 0 && !loading ? (
            <p className="loading-message">{t.loadingSymptoms}</p>
          ) : (
            filteredSymptoms.map((symptom) => (
              <button
                key={symptom}
                className={`symptom-tag ${
                  selectedSymptoms.has(symptom) ? 'selected' : ''
                }`}
                onClick={() => handleSymptomClick(symptom)}
              >
                {getSymptomLabel(symptom, language)}
              </button>
            ))
          )}
        </div>

        {/* Tahmin butonu */}
        <button
          onClick={handlePredict}
          disabled={selectedSymptoms.size === 0 || loading}
          className="predict-button"
        >
          {loading ? t.predicting : t.predictButton}
        </button>
      </div>

      {/* SAĞ: Sonuç paneli */}
      <div className="result-section">
        <button
          className="result-toggle-button close-btn"
          onClick={() => setIsResultClosed(true)}
          aria-label={t.hideResults}
        >
          &times;
        </button>

        <div className="result-content-wrapper">
          <h2>{t.resultTitle}</h2>
          {loading && (
            <div className="loading-spinner">
              <p>{t.analyzing}</p>
            </div>
          )}

          {!loading && result && (
            <div className="result-content">
              <h3>{t.resultPossible}</h3>
              <h2 className="disease-name">
                {getDiseaseLabel(result, language)}
              </h2>
              <p className="warning-message">
                <b>{t.disclaimerTitle}</b> {t.disclaimerText}
              </p>
            </div>
          )}

          {!loading && !result && selectedSymptoms.size > 0 && (
            <p>{t.noResultWithSymptoms}</p>
          )}
          {!loading && !result && selectedSymptoms.size === 0 && (
            <p>{t.noSymptomsSelected}</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
