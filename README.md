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
##  3. Eğitim
Her iki model de 10 epoch boyunca eğitilmiştir ve aşağıdaki sonuçlar elde edilmiştir:

####  CNN Modeli Sonuçları:
Model, her biri 9 farklı balık sınıfını temsil eden 7200 görüntü üzerinde eğitildi. Eğitim sırasında model parametreleri güncellenerek, sınıflar arasında en yüksek doğruluk oranına ulaşılması hedeflendi. Aşağıdaki adımlar kullanılarak eğitim süreci yapılandırılmıştır:

####  1. **Veri Önişleme ve Artırma**:
    - Rescale: Görseller `1./255` ile normalize edildi.
    - Veri artırma işlemleri:
        - Döndürme (`rotation_range=20`)
        - Genişlik ve yükseklik kaydırmaları (`width_shift_range=0.2`, `height_shift_range=0.2`)
        - Kesme (`shear_range=0.2`)
        - Yakınlaştırma (`zoom_range=0.2`)
        - Yatay çevirme (`horizontal_flip=True`)

####  2. **Eğitim Parametreleri**:
    - Epoch sayısı: 10
    - Batch boyutu: 32
    - Optimizasyon: `Adam` optimizer, varsayılan ayarlarla.
    - Kayıp Fonksiyonu: `Categorical Crossentropy`
    - Sınıf modu: Kategorik (`categorical`) olarak tanımlandı.

### Model Eğitimi

Model, eğitimin her epoch'unda belirli bir doğruluk ve kayıp değerine ulaşmıştır. Epoch sonuçlarına göre doğruluk oranında belirli bir artış gözlenmiş, ancak doğrulama kaybı bazı epoch'larda yüksek kalmıştır

### Model Doğrulama Sonuçları

Eğitim sonrasında, model doğrulama veri seti üzerinde test edilmiştir. Doğrulama sonuçları şu şekildedir:
- **Doğrulama Kaybı**: 15.7350
- **Doğrulama Doğruluğu**: %41.78

### Değerlendirme ve İyileştirme Önerileri

Modelin doğrulama doğruluğu (%41.78) ve doğrulama kaybı değerleri, modelin daha iyi bir performansa ulaşabilmesi için iyileştirilmesi gerektiğini göstermektedir. Önerilen bazı geliştirmeler şunlardır:
- **Model Mimarisi**: Ekstra Conv2D katmanları veya Dropout katmanları ekleyerek aşırı uyum önlenebilir.
- **Hiperparametre Ayarları**: Epoch sayısını artırmak ve `learning_rate` ayarları ile oynayarak daha iyi sonuçlar elde edilebilir.
- **Veri Artırma**: Görseller üzerindeki veri artırma parametreleri üzerinde daha fazla çalışarak veri çeşitliliği artırılabilir.

Bu eğitim ve doğrulama süreçleri, modelin hangi alanlarda iyileştirilmeye açık olduğunu ortaya koymaktadır.
