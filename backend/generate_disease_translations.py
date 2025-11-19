import csv
import json
from pathlib import Path

# 1) Girdi CSV dosyan (sende dia_3.csv)
CSV_PATH = Path("dataset/dia_3.csv")

# 2) Çıktı JSON dosyası (frontend tarafındaki sözlük)
JSON_PATH = Path("../frontend/src/diseaseTranslations.json")

def main():
    # 3) Var olan çevirileri koru (varsayılan: boş)
    if JSON_PATH.exists():
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            try:
                translations = json.load(f)
            except json.JSONDecodeError:
                print("Mevcut JSON bozuk, sıfırdan başlıyoruz.")
                translations = {}
    else:
        translations = {}

    # 4) CSV'den diagnose kolonunu oku
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            diag = (row.get("diagnose") or "").strip()
            if not diag:
                continue

            # Eğer zaten JSON'da varsa, aynen bırak (senin TR çevirilerin korunur)
            if diag in translations:
                continue

            # Yeni bir giriş oluştur: en ve tr aynı
            translations[diag] = {
                "en": diag,
                "tr": diag  # ŞİMDİLİK aynı; istersen sonra Türkçeye çevirirsin
            }

    # 5) JSON'a yaz
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)

    print(f"Toplam {len(translations)} hastalık JSON'a yazıldı:", JSON_PATH)

if __name__ == "__main__":
    main()
