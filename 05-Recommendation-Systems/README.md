# Hafta 5: Tavsiye Sistemleri (Recommendation Systems)

Bu klasör, kullanıcı deneyimini optimize etmek ve kişiselleştirilmiş hizmet/ürün sunmak amacıyla geliştirilen modern tavsiye sistemi algoritmalarını ve vaka çalışmalarını içermektedir.

## Klasör Yapısı ve Teknik Detaylar

### 1. Teorik ve Temel Algoritma Çalışmaları
* **`arl.py`:** Birliktelik Kuralı Analizi (Association Rule Learning) metodolojisinin temel pratikleri.
* **`content_based.py` / `item_based.py` / `user_based.py`:** İçerik tabanlı ve işbirlikçi filtreleme tekniklerinin temel DataFrame pratikleri.
* **`model_based.py`:** Matris Matrisleştirme (SVD) yöntemiyle makine öğrenmesi tabanlı öneri sistemi pratikleri.

### 2. Vaka Çalışmaları (Case Studies)

#### 🛠️ Birliktelik Kuralı Analizi ile Hizmet Öneri Sistemi (`armut_arl_recommender.py`)
Türkiye'nin en büyük online hizmet platformu olan Armut'un kullanıcı alışkanlıkları üzerinden Apriori algoritması kullanılarak bir servis tavsiye motoru kurulmuştur:
* **Veri Hazırlama ve Sepet Tanımı:** `ServiceId` ve `CategoryId` değişkenleri string operasyonları ile birleştirilerek benzersiz hizmet tanımları (`hizmetler`) türetilmiştir. Veride doğrudan bir fatura/sepet tanımı bulunmadığı için, her kullanıcının aylık bazda aldığı hizmetler `UserId_Year-Month` formatında birleştirilerek benzersiz sepet ID'leri (`ID`) oluşturulmuştur.
* **Matris Dönüşümü:** Veri seti, satırlarda sepetlerin, sütunlarda hizmetlerin yer aldığı ve hücrelerde hizmet frekanslarının bulunduğu bir `Invoice-Product` pivot matrisine dönüştürülmüştür.
* **Apriori ve Kuralların Üretilmesi:** `mlxtend` kütüphanesi kullanılarak minimum support değeri `%1` baz alınarak olası tüm ürün birliktelikleri (`frequent_itemsets`) hesaplanmış, ardından Lift metriğine göre sıralı birliktelik kuralları (`rules`) çıkarılmıştır.
* **Öneri Algoritması:** `arl_recommender` fonksiyonu ile en son `2_0` hizmetini alan bir kullanıcıya, kurallardaki Lift skorları baz alınarak en yüksek korelasyona sahip tamamlayıcı hizmet dinamik olarak önerilmektedir.

#### 🎬 Film Verisi Üzerinden Hibrit Öneri Sistemi (`movie_hybrid_recommender.py`)
Aynı kullanıcı için hem Kullanıcı Tabanlı (User-Based) hem de Ürün Tabanlı (Item-Based) işbirlikçi filtreleme yöntemlerini entegre eden hibrit bir öneri motoru geliştirilmiştir:
* **Veri Ön İşleme:** `movie` ve `rating` veri setleri birleştirilmiş, sistem istatistiklerini manipüle etmemesi adına toplam oy sayısı 1000'in altında kalan filmler filtrelenerek temiz bir `user_movie_df` pivot tablosu oluşturulmuştur.
* **User-Based Bölümü:** * Rastgele seçilen bir hedef kullanıcının izlediği filmler tespit edilmiş ve bu filmlerin en az `%60`'ını izleyen diğer benzer kullanıcılar izole edilmiştir.
  * Bu kullanıcılar ile hedef kullanıcı arasındaki Pearson Korelasyon matrisi hesaplanarak, $r \ge 0.40$ şartını sağlayan en yakın profiller (`top_users`) listelenmiştir.
  * Benzer kullanıcıların verdiği puanlar, korelasyon katsayıları ile çarpılarak ağırlıklı puan (`weighted_rating`) haline getirilmiş ve hedef kullanıcıya özel en yüksek skora sahip ilk 5 film önerisi üretilmiştir.
* **Item-Based Bölümü:** Target kullanıcının geçmişte 5 tam puan verdiği en güncel film (`timestamp` bazlı) tespit edilmiş, bu filmin tüm veri setindeki diğer filmlerle olan korelasyon dağılımı (`corrwith`) hesaplanarak en benzer ilk 5 tamamlayıcı film belirlenmiştir.
* **Sonuç:** Kullanıcıya 5'i User-Based, 5'i Item-Based olmak üzere toplam 10 adet analitik film tavsiyesi sunulmuştur.

## Kullanılan Teknolojiler
* Python 3.10+
* Pandas, NumPy, SciPy
* MLxtend (Apriori & Association Rules)

## Çalıştırma Talimatı
Projeleri çalıştırmak ve çıktı listelerini incelemek için terminal üzerinden şu komutları yürütebilirsiniz:
```bash
python armut_arl_recommender.py
python movie_hybrid_recommender.py