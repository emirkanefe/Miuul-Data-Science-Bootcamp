# Hafta 3: FLO - CRM Analitiği (Customer Relationship Management)

Bu klasör, omni-channel (hem online hem offline) satış stratejisi izleyen FLO ayakkabı şirketinin 20.000 müşterisine ait veri seti üzerinde gerçekleştirilen veri odaklı müşteri ilişkileri yönetimi süreçlerini içermektedir. Proje, kural tabanlı segmentasyon (RFM) ve olasılıksal gelecek değer tahmini (CLTV Prediction) olmak üzere iki ana vaka çalışmasından oluşmaktadır.

## Klasör Yapısı ve Teknik Detaylar

### 1. RFM Analizi ile Müşteri Segmentasyonu (`flo_rfm_analysis.py`)
Müşterilerin geçmiş satın alma davranışlarına göre kural tabanlı kümeleme ve hedef kitle tespiti çalışmasıdır.
* **Veri Hazırlama:** Online ve offline platformlardaki toplam sipariş (`total_order`) ve toplam harcama (`total_price`) miktarları birleştirilmiş, tarih içeren değişkenler zaman serisi formatına dönüştürülmüştür.
* **Metrik Hesaplama:** Analiz tarihi olarak belirlenen `2021-06-01` baz alınarak her müşteri için Recency (Yenilik), Frequency (Sıklık) ve Monetary (Parasal Değer) metrikleri hesaplanmıştır.
* **Skorlama:** Metrikler, `pd.qcut` yöntemiyle 1-5 arası standart skorlara dönüştürülmüş ve RF skoru elde edilmiştir.
* **Segmentasyon:** Düzenli ifadeler (regex) yardımıyla RF skorları endüstri standardı olan 10 farklı müşteri segmentine (`champions`, `loyal_customers`, `cant_loose` vb.) atanmıştır.
* **Hedef Kitle Çıktısı (Aksiyon Planı):** * Kadın kategorisine ilgi duyan sadık müşterilerin (`champions` ve `loyal_customers`) ID bilgileri `case_study_1_a.csv` olarak dışa aktarılmıştır.
  * Erkek ve çocuk kategorilerine ilgi duyan, kaybedilmemesi gereken veya yeni gelen müşterilerin ID bilgileri `case_study_1_b.csv` olarak raporlanmıştır.

### 2. Olasılıksal Modeller ile CLTV Tahmini (`flo_cltv_prediction.py`)
Müşterilerin gelecekte şirkete kazandıracağı potansiyel değerin ileri seviye istatistiksel modellerle tahmin edilmesi simülasyonudur.
* **Aykırı Değer Yönetimi:** Çok yüksek harcama veya sipariş sayısına sahip kullanıcıların veri setini manipüle etmesini önlemek amacıyla, `%1` ve `%99` çeyreklikler baz alınarak `outlier_thresholds` ve `replace_with_thresholds` fonksiyonları ile baskılama işlemi uygulanmıştır.
* **Veri Yapısının Kurulması:** BG-NBD modelinin gereksinim duyduğu haftalık recency (`recency_cltv_weekly`), haftalık müşteri yaşı (`T_weekly`), sıklık (`frequency`) ve ortalama işlem değeri (`monetary_cltv_avg`) hesaplanarak `cltv_df` oluşturulmuştur.
* **BG-NBD Modeli:** Olasılıksal model eğitilerek müşterilerin 3 aylık ve 6 aylık periyotlarda gerçekleştireceği beklenen satın alma sayıları (`exp_sales_3_month`, `exp_sales_6_month`) tahmin edilmiştir. `plot_period_transactions` fonksiyonu ile model doğrulaması yapılmıştır.
* **Gamma-Gamma Modeli:** Müşterilerin bırakacağı beklenen ortalama kar (`exp_average_value`) modellenmiş ve gerçekleşen değerler ile model tahminleri saçılım grafiği (`scatterplot`) üzerinde doğrulanmıştır.
* **Gelecek Değer Tahmini (6 Aylık CLTV):** İki istatistiksel model birleştirilerek her müşterinin 6 aylık yaşam boyu değeri hesaplanmış ve kullanıcılar çeyreklik bazda (A, B, C, D) segmentlere ayrılmıştır.

## Kullanılan Teknolojiler ve Kütüphaneler
* Python 3.10+
* Pandas, NumPy
* Lifetimes (BetaGeoFitter, GammaGammaFitter)
* Matplotlib, Seaborn

## Çalıştırma Talimatı
Analizlerin yerel ortamınızda simüle edilmesi ve metrik çıktıların üretilmesi için terminal üzerinden şu komutları yürütebilirsiniz:
```bash
python flo_rfm_analysis.py
python flo_cltv_prediction.py