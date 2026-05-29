# Hafta 9: Gelişmiş Ağaç Tabanlı Modeller (Advanced Tree-Based Models)

Bu klasör, doğrusal olmayan karmaşık veri yapılarını modellemek amacıyla kullanılan doğrusal olmayan ağaç tabanlı makine öğrenmesi algoritmalarını, bagging (torbalama) yöntemlerini ve bu modellerin hiperparametre optimizasyonu süreçlerini içermektedir. Ayrıca gerçek dünya veri setleri üzerinde test edilmesi amacıyla bir Kaggle entegrasyon çalışması barındırmaktadır.

## Klasör Yapısı ve Teknik Detaylar

### 1. Ağaç Tabanlı Modelleme Scriptleri
* **`ml_cart.py` (Classification and Regression Trees):** Karar ağacı yapılarının kurulması, Gini ve Entropy safsızlık (impurity) kriterlerine göre dallanma süreçleri. Aşırı öğrenmeyi (`overfitting`) engellemek amacıyla budama (`pruning`) ve hiperparametre (Örn: `max_depth`, `min_samples_split`) optimizasyonları.
* **`ml_random_forest.py` (Random Forest):** Birden fazla karar ağacının rastgele alt veri grupları ve rastgele öznitelik setleri ile eğitilerek bir araya getirilmesi (`Ensemble Learning`). Modelin varyansını düşürme ve tahmin tutarlılığını artırma süreçleri ile özellik önem düzeylerinin (`Feature Importance`) analizi.

### 2. Kaggle Yarışma Pratikleri (`kaggle/`)
Gerçek zamanlı bir makine öğrenmesi mücadelesine ait model geliştirme hattı:
* **`train.csv` / `test.csv`:** Model eğitimi ve nihai tahmin testleri için kullanılan ham veri setleri.
* **`prediction.py`:** Eğitilen ağaç tabanlı modellerin test verisi üzerinde simüle edilmesi ve tahmin çıktılarının üretilmesi süreci.
* **`sample_submission.csv`:** Kaggle platformunun standartlarına uygun formatta hazırlanan nihai tahmin teslim dosyası.

## Kullanılan Teknolojiler ve Kütüphaneler
* Python 3.10+
* Pandas, NumPy
* Scikit-learn (`sklearn.tree`, `sklearn.ensemble`, `sklearn.model_selection`)
* Grid Search / Randomized Search (Hiperparametre optimizasyon süreçleri için)

## Çalıştırma Talimatı
Modelleri çalıştırmak ve parametre optimizasyon sonuçlarını incelemek için terminal üzerinden şu komutları kullanabilirsiniz:
```bash
python ml_cart.py
python ml_random_forest.py