# Hafta 8: Makine Öğrenmesine Giriş (Introduction to Machine Learning)

Bu klasör, veri bilimi süreçlerinde tahminsel modelleme ve veri kümeleme amacıyla kullanılan temel Makine Öğrenmesi (Machine Learning) algoritmalarını, model kurma süreçlerini ve başarı değerlendirme metriklerini içermektedir. Çalışmalar hem Gözetimli (Supervised Learning) hem de Gözetimsiz (Unsupervised Learning) öğrenme modellerini kapsamaktadır.

## Klasör Yapısı ve Teknik Detaylar

### 1. Gözetimli Öğrenme Modelleri (Supervised Learning)
* **`ml_linear_reg.py` (Doğrusal Regresyon):** Sürekli hedef değişkenleri tahmin etmek amacıyla kurulan regresyon modelleri. Hata terimlerinin analizi ve katsayıların yorumlanması süreçleri.
* **`ml_logistic_reg.py` (Lojistik Regresyon):** İkili (binary) sınıflandırma problemleri için olasılıksal modelleme. Sınıflandırma eşik değerlerinin (threshold) analizi.
* **`ml_knn.py` (K-Nearest Neighbors):** Mesafe tabanlı sınıflandırma algoritması pratikleri. En yakın komşu sayısı ($K$) hiperparametresinin model başarısına etkisinin incelenmesi.
* **`ml_modeling.ipynb` (Uçtan Uca Modelleme Hattı):** Veri setlerinin eğitim (train) ve test (test) olarak bölünmesi, çapraz doğrulama (Cross-Validation) teknikleri ve Confusion Matrix (Karmaşıklık Matrisi) analizi üzerinden Accuracy, Precision, Recall ve F1-Score metriklerinin hesaplanması.

### 2. Gözetimsiz Öğrenme Modelleri (Unsupervised Learning)
* **`ml_kmeans.ipynb` (K-Means Kümeleme):** Etiketsiz verilerin benzerliklerine göre gruplandırılması süreçleri. Optimum küme sayısının belirlenmesi için Elbow (Dirsek) yöntemi ve Silhouette analizi uygulamaları.

## Kullanılan Teknolojiler ve Kütüphaneler
* Python 3.10+
* Pandas, NumPy
* Scikit-learn (`sklearn.linear_model`, `sklearn.neighbors`, `sklearn.cluster`, `sklearn.metrics`)
* Matplotlib, Seaborn (Model başarı grafiklerinin ve kümeleme sonuçlarının görselleştirilmesi için)

## Çalıştırma Talimatı
Script dosyalarını çalıştırmak veya not defterlerini incelemek için ilgili dizinde şu komutları yürütebilirsiniz:
```bash
python ml_linear_reg.py
jupyter notebook ml_modeling.ipynb