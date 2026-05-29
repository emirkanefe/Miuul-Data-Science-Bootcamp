# Hafta 2: Python ile Keşifçi Veri Analizi (EDA)

Bu klasör, Python kütüphanelerini (`NumPy`, `Pandas`, `Matplotlib`, `Seaborn`) kullanarak veri manipülasyonu, gelişmiş veri analizi pratikleri ve kural tabanlı müşteri segmentasyonu vaka çalışmalarını içermektedir.

## Klasör Yapısı ve İçerik

### 1. Temel ve İleri Seviye EDA Pratikleri
* **`numpy_ders.py` / `pandas_101.py`:** Temel kütüphane pratikleri ve veri manipülasyon temelleri.
* **`degiskenlerin_yakalanması.py`:** Büyük veri setlerinde nümerik, kategorik ve kardinal değişkenlerin otomatik fonksiyonlarla ayırt edilmesi.
* **`korelasyon.py` / `veri_gorsellestirme.py`:** Değişkenler arası ilişkilerin matrisler ve Seaborn grafik araçları ile analizi.

### 2. Vaka Çalışmaları (Case Studies)

#### Pandas ve Keşifçi Veri Analizi (`pandas_and_eda_exercises.py`)
`Titanic` ve `Tips` veri setleri üzerinden gerçek gerçekleştirilen kapsamlı EDA çalışması:
* Kayıp gözlemlerin (`missing values`) saptanması, mod ve medyan yöntemleri ile doldurulması.
* Koşullu seçim (`loc` ve mantıksal operatörler) pratikleri.
* Verilerin `groupby` ve `agg` fonksiyonları kullanılarak çoklu kırılımlarda (`survived`, `time`, `day`) özet istatistiklerinin çıkarılması.
* Fonksiyonel programlama, `apply` ve `lambda` yapıları ile yeni özellik türetimi (`feature engineering`).

#### Kural Tabanlı Sınıflandırma ile Potansiyel Gelir Hesaplama (`lead_scoring_persona.py`)
Bir oyun şirketinin kullanıcı verilerini (`persona.csv`) kullanarak seviye tabanlı yeni müşteri tanımları (persona) oluşturma ve gelir tahmini simülasyonu:
* Verinin ülkelere, cihazlara (`SOURCE`), yaşa ve cinsiyete göre kırılıp ortalama kazanç yapısının çıkarılması.
* Sürekli veri türündeki yaş (`AGE`) değişkeninin `pd.cut` kullanılarak kategorik bir yapıya (`AGE_CAT`) dönüştürülmesi.
* Müşteri özelliklerine göre seviye tabanlı dinamik string birleştirme ile `customers_level_based` (Persona) değişkeninin oluşturulması.
* Personaların `pd.qcut` ile 4 farklı çeyreğe bölünerek gelir segmentlerine (`SEGMENT`) ayrılması.
* Yeni bir kullanıcı sisteme dahil olduğunda getirebileceği ortalama geliri ve segmenti döndüren fonksiyonel tahmin (`predict`) algoritmasının kurulması.

## Kullanılan Teknolojiler
* Python 3.10+
* Pandas, NumPy, Seaborn, Matplotlib

## Çalıştırma Talimatı
Projeleri yerel ortamınızda test etmek için terminalden şu komutları yürütebilirsiniz:
```bash
python pandas_and_eda_exercises.py
python lead_scoring_persona.py