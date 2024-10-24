# Deep_Learning_Project_Buket_Kalfa
Bu proje, bir balık veri seti üzerinde yapay sinir ağları (ANN) ve evrişimli sinir ağları (CNN) kullanarak balık türlerini sınıflandırmayı amaçlamaktadır. Proje kapsamında kullanılan veri seti, farklı balık türlerine ait görüntülerden oluşmaktadır. Model, bu görüntülerden yola çıkarak balık türlerini sınıflandırmayı öğrenir.
[Kaggle Notebook "A_Large_Scale_Fish_Dataset_Buket_Kalfa_" linki]https://www.kaggle.com/code/buketkalfa/a-large-scale-fish-dataset-buket-kalfa/
# Veri Seti
Bu projede kullanılan veri seti, Kaggle üzerinde bulunan geniş ölçekli bir balık veri setidir. Veri seti, 9 farklı balık türüne ait toplamda 18.000 görüntü içermektedir.

##  Balık türleri şunlardır:

####  Hourse Mackerel
####  Black Sea Sprat
####  Sea Bass
####  Red Mullet
####  Trout
####  Striped Red Mullet
####  Shrimp
####  Gilt-Head Bream
####  Red Sea Bream
# Proje Aşamaları
##  1. Veri Hazırlama
Görüntüler, TensorFlow'un ImageDataGenerator sınıfı kullanılarak yüklenmiş ve eğitim/ doğrulama olarak %80 eğitim ve %20 doğrulama verisi şeklinde ayrılmıştır. Ayrıca, görüntülerin her biri 224x224 boyutlarına küçültülmüş ve normalizasyon işlemi yapılmıştır.

##  2. CNN Modeli
CNN modeli, görsel verileri işleyip sınıflandırma yapabilen güçlü bir modeldir. Bu model şu katmanlardan oluşur:

###  Giriş Katmanı: (224x224x3)
3 adet Evrişim Katmanı (Conv2D) ve Max Pooling katmanları
###  Flatten katmanı
128 nöronlu tam bağlantılı (Dense) katman
###  Çıkış katmanı: Softmax ile 9 sınıfı sınıflandırır.
##  3. ANN Modeli
ANN modeli ise daha basit bir sinir ağı yapısıdır ve görüntü verilerini tek boyutlu vektörlere dönüştürerek işlem yapar. Bu model şu katmanlardan oluşur:

Giriş Katmanı: (224x224x3) görüntüyü düzleştiren (Flatten) bir katman
3 adet Tam Bağlantılı (Dense) katman
Çıkış katmanı: Softmax ile 9 sınıfı sınıflandırır.
##  4. Eğitim
Her iki model de 10 epoch boyunca eğitilmiştir ve aşağıdaki sonuçlar elde edilmiştir:

####  CNN Modeli Sonuçları:
Eğitim Doğruluğu: %99
Doğrulama Doğruluğu: %84.5
Eğitim Kaybı: 0.0261
Doğrulama Kaybı: 0.6626
ANN Modeli Sonuçları:
Eğitim Doğruluğu: %83
Doğrulama Doğruluğu: %59.5
Eğitim Kaybı: 0.4674
Doğrulama Kaybı: 1.3899
##  5. Sonuç
CNN modeli, ANN modeline kıyasla daha iyi sonuçlar vermiştir ve doğrulama verisinde %84.5 oranında doğruluk elde etmiştir. ANN modeli ise %59.5 doğruluk ile CNN modelinin gerisinde kalmıştır.

Kullanılan Teknolojiler
Python 3
TensorFlow / Keras
Pandas
NumPy
Matplotlib (veri görselleştirme)
