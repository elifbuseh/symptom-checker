# backend/check_columns.py
import pandas as pd
import os

DATA_PATH = 'dataset'

# Kontrol etmek istediğimiz, hata veren dosyalar
files_to_check = {
    'diffsydiw.csv': "Ana Veri Dosyası",
    'dia_t.csv': "Hastalık Sözlüğü 1",
    'dia_3.csv': "Hastalık Sözlüğü 2",
    'diagn_title.csv': "Hastalık Sözlüğü 3"
}

print("--- CSV Sütun Kontrol Aracı Başlatıldı ---")
print("Aşağıdaki listede, dosyalarınızda bulunan GERÇEK SÜTUN ADLARI görünecektir:\n")

for file_name, description in files_to_check.items():
    try:
        file_path = os.path.join(DATA_PATH, file_name)
        # Dosyanın sadece ilk satırını (header/başlık) oku
        df_temp = pd.read_csv(file_path, nrows=0) 
        
        print(f"--- {description} ({file_name}) ---")
        # Bulunan sütun adlarını listele
        print(f"Sütunlar: {list(df_temp.columns)}\n")
    
    except FileNotFoundError:
        print(f"--- HATA: {file_name} ---")
        print(f"Dosya '{DATA_PATH}' klasöründe bulunamadı.\n")
    except Exception as e:
        print(f"--- HATA: {file_name} ---")
        print(f"Dosya okunamadı. Hata: {e}\n")

print("--- Kontrol Tamamlandı ---")
print("Lütfen bu çıktının tamamını (yukarıdan aşağıya) kopyalayıp bana gönderin.")