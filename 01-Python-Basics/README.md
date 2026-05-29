# Hafta 1: Python Alıştırmaları (Python Basics)

Bu klasör, veri bilimi süreçlerinde sıkça kullanılan temel Python konseptlerine ve veri yapılarına odaklanan teknik alıştırmaları içermektedir.

## İçerik ve Çözülen Görevler
* **Veri Yapıları:** Temel veri tiplerinin (`int`, `float`, `list`, `dict`, `set`, `tuple`) incelenmesi.
* **String & Liste Manipülasyonu:** Metin temizleme, dilimleme (`slicing`) ve yerleşik liste metotlarının kullanımı.
* **Sözlük İşlemleri:** Key-value manipülasyonu, dinamik güncel değer atamaları ve veri silme süreçleri.
* **Fonksiyon Yapıları:** Tek ve çift sayıları ayıran, geriye çoklu değer döndüren fonksiyon tasarımı.
* **Döngü Yapıları:** `enumerate()` ile indeks takibi ve `zip()` ile eş zamanlı veri eşleştirme pratikleri.
* **Küme Teorisi:** Kapsama, kesişim ve fark metotlarının küme analizi üzerinde kullanımı.

## Çalıştırma Talimatı
Egzersizleri yerel ortamınızda test etmek için:
```bash
python python_exercises.py
```
# Hafta 1: List Comprehensions Pratikleri

Bu klasör, Python'da veri manipülasyonu süreçlerini hızlandıran ve kod okunabilirliğini artıran List Comprehensions yapılarının `car_crashes` veri seti üzerinde uygulanmasını içermektedir.

## İçerik ve Çözülen Görevler
* **Görev 1:** Veri setindeki numerik değişkenlerin isimlerini dinamik olarak seçip, başlarına "NUM_" ön ekini ekleyerek kalıcı/geçici değişiklik yapılması.
* **Görev 2:** Değişken isimlerinde belirli bir kelimeyi ("no") barındırmayan kolonların sonuna dinamik olarak "_FLAG" ekinin getirilmesi.
* **Görev 3:** Belirlenen bir listenin dışındaki tüm kolon isimlerinin filtrelenerek veri setinden sadece bu hedef değişkenlerin seçilmesi.

## Kullanılan Veri Seti
* Seaborn kütüphanesi içerisinde yer alan yerleşik **`car_crashes`** veri seti.

## Çalıştırma Talimatı
Scripti yerel ortamınızda test etmek için:
```bash
python list_comprehensions.py