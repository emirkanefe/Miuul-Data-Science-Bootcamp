# Hafta 4: Ölçümleme Problemleri ve A/B Testi (Measurement Problems & A/B Testing)

Bu klasör, e-ticaret platformlarında ürün puanlarının manipülasyondan uzak, doğru hesaplanması ve kullanıcı yorumlarının yanıltıcı olmayacak şekilde sıralanması (sorting) süreçlerine ait matematiksel ve istatistiksel çözümleri içermektedir.

## Klasör Yapısı ve Teknik Detaylar

### 1. Teorik ve Pratik Çalışma Scriptleri
* **`rating.py` / `sorting_by_rating.py`:** Ürün puanlama ve derecelendirme metodolojilerinin temel pratikleri.
* **`sorting_reviews.py`:** Yorum sıralama algoritmalarının test süreçleri.
* **`ab_testing.py`:** Hipotez testleri ve varyasyon analizleri.

### 2. Vaka Çalışması: Amazon Ürün Puanlama ve Yorum Sıralama (`amazon_rating_sorting.py`)
Amazon Elektronik kategorisindeki en fazla yorum alan ürünün kullanıcı değerlendirmeleri üzerinden iki temel problem çözülmüştür:

#### A. Zamana Göre Ağırlıklı Puan Hesaplama (Time-Based Weighted Average)
Ürünün ham puan ortalamasının (`overall.mean()`), eski yorumlar ile güncel trendler arasındaki farkı yansıtamaması problemi giderilmiştir.
* Kullanıcıların yorum yaptığı tarihten itibaren geçen gün sayısı (`day_diff`) analiz edilerek veri seti çeyreklik bazda (`quantile`) dönemlere ayrılmıştır.
* Güncel yorumların ürün trendini daha iyi yansıtması amacıyla yakın tarihteki puanlara daha yüksek ağırlık verilerek (`%28`, `%26`, `%24`, `%22`) ağırlıklı ürün puanı hesaplanmıştır.

#### B. Wilson Lower Bound (WLB) ile Güvenilir Yorum Sıralaması
Kullanıcıların yorumlara verdiği faydalı/faydasız (up/down) oylarının sıralanmasında salt fark (`up - down`) veya oran (`up / total`) yöntemlerinin yarattığı dezavantajlar (örn: 1 up / 0 down alan bir yorumun, 100 up / 1 down alan yorumun önüne geçmesi gibi) engellenmiştir.
* Veri setinde bulunmayan faydasız oy sayısı (`helpful_no`), toplam oy sayısından faydalı oy sayısı çıkarılarak (`total_vote - helpful_yes`) türetilmiştir.
* **Score Positive-Negative Difference**, **Score Average Rating** ve **Wilson Lower Bound** skorları her satır için hesaplanmıştır.
* **Wilson Lower Bound Skoru:** Bernoulli parametresi $p$ için hesaplanan güven aralığının alt sınırı baz alınarak olasılıksal bir sıralama yapılmış, ürün detay sayfasında sergilenecek en güvenilir 20 yorum belirlenmiştir.

## Kullanılan Teknolojiler ve Metotlar
* Python 3.10+
* Pandas, SciPy (`scipy.stats`)
* Wilson Lower Bound Skoru hesaplama algoritması

## Çalıştırma Talimatı
Analiz süreçlerini çalıştırmak ve sıralama çıktılarını incelemek için terminal üzerinden şu komutu yürütmeniz yeterlidir:
```bash
python amazon_rating_sorting.py