# backend/train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import json
import os

print("Script başladı...")

# 1. Dosya Yollarını Tanımla
DATA_PATH = 'dataset'
# Ana ham veri (ilişki dosyası)
TRAIN_DATA_FILE = os.path.join(DATA_PATH, 'diffsydiw.csv') 

# --- Tüm Sözlük Dosyalarını Tanımla ---
DISEASE_DICT_1 = os.path.join(DATA_PATH, 'dia_t.csv')
DISEASE_DICT_2 = os.path.join(DATA_PATH, 'dia_3.csv')
DISEASE_DICT_3 = os.path.join(DATA_PATH, 'diagn_title.csv')

SYMPTOM_DICT_1 = os.path.join(DATA_PATH, 'symptoms2.csv')
SYMPTOM_DICT_2 = os.path.join(DATA_PATH, 'sym_t.csv')
SYMPTOM_DICT_3 = os.path.join(DATA_PATH, 'sym_3.csv')
# ----------------------------------------------------

try:
    # 2. Semptom Sözlüklerini ve İsim Listesini Oluştur
    symptom_id_to_name_map = {} 
    print("Ana Semptom Sözlüğü oluşturuluyor...")
    
    # Sütun adları, en son 'check_columns.py' çıktınıza GÖRE TAHMİN EDİLMİŞTİR
    # (symptoms2.csv -> chief_complaint_id, name)
    try:
        df_dict_1 = pd.read_csv(SYMPTOM_DICT_1)
        for _, row in df_dict_1.iterrows():
            if pd.notna(row['name']) and pd.notna(row['chief_complaint_id']):
                symptom_id_to_name_map[int(row['chief_complaint_id'])] = row['name'].strip()
    except Exception: pass # Bir dosya başarısız olursa devam et
    
    # (sym_t.csv -> syd, symptom)
    try:
        df_dict_2 = pd.read_csv(SYMPTOM_DICT_2)
        for _, row in df_dict_2.iterrows():
            if pd.notna(row['symptom']) and pd.notna(row['syd']):
                symptom_id_to_name_map[int(row['syd'])] = row['symptom'].strip()
    except Exception: pass
    
    # (sym_3.csv -> _id, symptom)
    try:
        df_dict_3 = pd.read_csv(SYMPTOM_DICT_3)
        for _, row in df_dict_3.iterrows():
            if pd.notna(row['symptom']) and pd.notna(row['_id']):
                symptom_id_to_name_map[int(row['_id'])] = row['symptom'].strip()
    except Exception: pass
    
    print(f"Toplam {len(symptom_id_to_name_map)} ID-İsim eşleşmesi (Semptom) bulundu.")

    # 3. Hastalık İsimleri Sözlüğünü Oluştur
    disease_id_to_name_map = {}
    print("Ana Hastalık Sözlüğü oluşturuluyor...")
    
    # (dia_t.csv -> did, diagnose)
    try:
        df_dis_1 = pd.read_csv(DISEASE_DICT_1)
        for _, row in df_dis_1.iterrows():
            if pd.notna(row['diagnose']) and pd.notna(row['did']):
                disease_id_to_name_map[int(row['did'])] = row['diagnose'].strip()
    except Exception: pass
    
    # (dia_3.csv -> _id, diagnose)
    try:
        df_dis_2 = pd.read_csv(DISEASE_DICT_2)
        for _, row in df_dis_2.iterrows():
            if pd.notna(row['diagnose']) and pd.notna(row['_id']):
                disease_id_to_name_map[int(row['_id'])] = row['diagnose'].strip()
    except Exception: pass
    
    # (diagn_title.csv -> id, title)
    try:
        df_dis_3 = pd.read_csv(DISEASE_DICT_3)
        for _, row in df_dis_3.iterrows():
            if pd.notna(row['title']) and pd.notna(row['id']):
                disease_id_to_name_map[int(row['id'])] = row['title'].strip()
    except Exception: pass
        
    print(f"Ana Hastalık Sözlüğü {len(disease_id_to_name_map)} benzersiz isimle dolduruldu.")
    if len(disease_id_to_name_map) == 0:
        print("HATA: Hiç hastalık sözlüğü okunamadı. Lütfen 'dia_t.csv' vb. dosyalardaki sütun adlarını kontrol edin.")
        exit()

    # 4. Ana Ham Veriyi Oku ('diffsydiw.csv')
    df_train_raw = pd.read_csv(TRAIN_DATA_FILE)
    print(f"'{TRAIN_DATA_FILE}' (ham veri) başarıyla okundu.")
    
    # 5. Veriyi Geniş Formata (Matrix) Çevir
    print("Ham veri matrise dönüştürülüyor (pivot)... Bu işlem biraz sürebilir.")
    
    # 'did' ve 'syd' sütunlarındaki ID'leri İSİMLERE dönüştür
    df_train_raw['disease_name'] = df_train_raw['did'].map(disease_id_to_name_map)
    df_train_raw['symptom_name'] = df_train_raw['syd'].map(symptom_id_to_name_map)
    
    # İsimlendiremediğimiz (sözlükte olmayan) verileri at
    df_train_raw = df_train_raw.dropna(subset=['disease_name', 'symptom_name'])
    
    # Pivot Table oluştur: Satırlar hastalık, sütunlar semptom, değerler ağırlık (wei)
    # aggfunc='max' ekleyerek, aynı hastalık-semptom çifti varsa en yüksek ağırlığı al
    matrix = pd.pivot_table(
        df_train_raw,
        values='wei',
        index='disease_name',
        columns='symptom_name',
        fill_value=0, # Eksik ilişkiler 0 olsun
        aggfunc='max' 
    )
    print("Veri matrisi (pivot table) başarıyla oluşturuldu.")

    # 6. Veriyi X (Semptomlar) ve y (Hastalık İSİMLERİ) olarak hazırla
    y = matrix.index  # Satır başlıkları (Hastalık İsimleri)
    X = matrix.values # Matrisin içindeki değerler (0'lar ve ağırlıklar)
    
    # Semptom listesini (X'in sütunları) al
    symptom_list = list(matrix.columns)
    
    # '[null]' gibi istenmeyen bir semptom varsa temizle
    if '[null]' in symptom_list:
        symptom_list.remove('[null]')
        X = matrix.drop(columns=['[null]']).values # X'ten de çıkar
        
    print(f"Model için X ({len(symptom_list)} semptom) ve y ({len(y)} hastalık) oluşturuldu.")
    
    # 7. Modeli Eğit
    model = RandomForestClassifier()
    model.fit(X, y)
    print("Model eğitildi.")

    # 8. Modeli Kaydet
    joblib.dump(model, 'model.pkl')
    print("'model.pkl' dosyası kaydedildi.")

    # 9. 'symptoms.json' dosyasını oluştur
    # Bu 'symptom_list', X matrisinin sütunlarıyla %100 aynı
    with open('symptoms.json', 'w') as f:
        json.dump(symptom_list, f)
    
    print(f"'symptoms.json' dosyası {len(symptom_list)} gerçek semptom ismiyle güncellendi.")
    print("--- Eğitim Başarıyla Tamamlandı! ---")

except FileNotFoundError as e:
    print(f"HATA: Dosya bulunamadı. '{e.filename}'")
    print("Lütfen tüm CSV dosyalarının 'backend/dataset/' klasöründe olduğundan emin olun.")
except KeyError as e:
    print(f"HATA: Bir CSV dosyasında beklenen sütun bulunamadı: {e}")
    print("Lütfen koddaki sütun adlarını (örn: 'did', 'diagnose', 'syd', 'symptom') CSV dosyalarınızla karşılaştırın.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")