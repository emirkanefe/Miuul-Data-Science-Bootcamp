# Hafta 7: Özellik Mühendisliği (Feature Engineering)

Bu klasör, ham veri setlerini makine öğrenmesi modellerine hazır hale getirmek, model performansını optimize etmek ve veri içerisindeki gizli kalıpları ortaya çıkarmak amacıyla gerçekleştirilen ileri seviye **Özellik Mühendisliği (Feature Engineering)** ve **Veri Ön İşleme (Data Preprocessing)** çalışmalarını içermektedir.

## Klasör Yapısı ve Teknik Detaylar

### 1. Temel Pratikler
* **`feature_engineering.py`:** Aykırı değer yönetimi, eksik gözlem analizi, veri ölçeklendirme ve encoding tekniklerinin temel fonksiyonel pratikleri.

### 2. Vaka Çalışmaları (Case Studies)

#### Diyabet Veri Seti Özellik Mühendisliği (`diabetes_feature_engineering.py`)
Pima Indians Diabetes veri seti üzerinde uçtan uca veri ön işleme ve yeni özellik türetme çalışması:
* **Keşifçi Veri Analizi:** Nümerik ve kategorik değişkenlerin analizi, hedef değişken (`Outcome`) ile olan ilişkilerinin incelenmesi.
* **Eksik Değer Analizi:** Veri setinde `0` olarak girilen ancak biyolojik olarak `0` olamayacak değişkenlerin (`Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`) tespit edilerek `NaN` değerine dönüştürülmesi ve medyan/ortalama yöntemleri ile doldurulması.
* **Aykırı Değer Yönetimi:** Belirlenen eşik değerlere göre aykırı gözlemlerin baskılanması (`reaping`).
* **Özellik Türetimi (Feature Extraction):** Yaş, BMI ve Glikoz gibi kritik değişkenlerin bir araya getirilmesiyle yeni kombinasyon değişkenler (Örn: `NEW_AGE_BMI_NOM`, `NEW_GLUCOSE_INSULIN_RATIO`) oluşturulması.
* **Encoding & Scaling:** Kategorik değişkenlerin `One-Hot Encoding` işlemine tabi tutulması ve nümerik değişkenlerin standartlaştırılması (`RobustScaler` / `StandardScaler`).

####  Ev Fiyatları Veri Seti Özellik Mühendisliği (`house_price_feature_engineering.py`)
Ames, Iowa'daki konutların özelliklerini içeren veri seti üzerinde gelişmiş veri ön işleme süreci:
* **Yapısal Analiz:** Nümerik görünümlü kategorik değişkenlerin (Örn: `MSSubClass`) tespiti ve kardinalitesi yüksek olan sütunların analizi.
* **Eksik ve Aykırı Değer Çözümü:** Ev fiyatını doğrudan etkileyebilecek eksik verilerin (`GarageYrBlt`, `MasVnrArea` vb.) yapısal özelliklerine göre (0 veya None ile) doldurulması ve aykırı değerlerin temizlenmesi.
* **Gelişmiş Özellik Türetimi:** * Evin toplam yaşam alanını gösteren (`NEW_TotalFlrSF`), toplam banyo sayısını veren (`NEW_TotalBath`) dinamik değişkenlerin oluşturulması.
  * Yapım yılı ve yenilenme yılı üzerinden evin güncel yaşının (`NEW_HouseAge`) hesaplanması.
* **Rare Encoding:** Veri setinde frekansı çok düşük olan kategorik sınıfların bir araya getirilerek `Rare` olarak etiketlenmesi ve modelin aşırı öğrenmesinin (`overfitting`) engellenmesi.
* **Model Hazırlığı:** Tüm kategorik değişkenlerin encoder süreçlerinden geçirilerek matris yapısına hazırlanması.

## Kullanılan Teknolojiler
* Python 3.10+
* Pandas, NumPy, Scikit-learn

## Çalıştırma Talimatı
Analiz ve ön işleme scriptlerini test etmek için terminal üzerinden şu komutları kullanabilirsiniz:
```bash
python diabetes_feature_engineering.py
python house_price_feature_engineering.py