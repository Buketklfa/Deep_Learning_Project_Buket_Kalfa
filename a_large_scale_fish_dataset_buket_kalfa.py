# -*- coding: utf-8 -*-
"""a-large-scale-fish-dataset-buket-kalfa.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yVzoNUQ98JOEdPlXmGFvJP3BHYXI3SZ8
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# Klasik kütüphaneler.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# TensorFlow
import tensorflow as tf
import os
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

fish_dir = '/kaggle/input/a-large-scale-fish-dataset/Fish_Dataset/Fish_Dataset'
classes = [i for i in os.listdir(fish_dir) if '.' not in i]
classes

"""**Veri Önişleme Süreci**"""

label = []
path = []

fish_dir = '/kaggle/input/a-large-scale-fish-dataset/Fish_Dataset/Fish_Dataset'

for dir_name, _,filenames in os.walk(fish_dir):
    for filename in filenames:
        if os.path.splitext(filename)[-1]=='.png':               # If filename contains .png
            if dir_name.split()[-1]!='GT':                       # If directory doesn't contain GT
                label.append(os.path.split(dir_name)[-1])         # Append the directory name to label
                path.append(os.path.join(dir_name,filename))     # Append all the png files to path of that directory

data = pd.DataFrame(columns=['path','label'])
data['path']=path
data['label']=label


    # İlk birkaç satırı inceleyelim
print(data.head())

"""veri setinin içeriği"""

data.head()

data.tail()

data['label'].value_counts()

batch_size = 32
img_height = 224
img_width = 224

# Print the number of samples
print(f"X_train: {len(X_train)}")
print(f"X_test: {len(X_test)}")

# Veri setinin sayısını kontrol et
print(data['label'].value_counts())

# Hiperparametreler
batch_size = 32
img_height = 224
img_width = 224
epochs = 20  # Epoch sayısını artırdık

# Veri artırma ve validation split ile veri jeneratörlerini ayarla
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.2  # %20 veriyi validasyon için ayır
)

train_generator = train_datagen.flow_from_dataframe(
    dataframe=data,
    x_col='path',
    y_col='label',
    target_size=(img_height, img_width),
    class_mode='categorical',
    batch_size=batch_size,
    subset='training'
)

validation_generator = train_datagen.flow_from_dataframe(
    dataframe=data,
    x_col='path',
    y_col='label',
    target_size=(img_height, img_width),
    class_mode='categorical',
    batch_size=batch_size,
    subset='validation'
)

"""**CNN**"""

# CNN Modelini oluştur
model_cnn = keras.Sequential([
    layers.InputLayer(input_shape=(img_height, img_width, 3)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(256, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dropout(0.5),  # Dropout katmanı ekle
    layers.Dense(128, activation='relu'),
    layers.Dense(len(train_generator.class_indices), activation='softmax')])

# Modeli derle
model_cnn.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

# Modeli eğit
with tf.device('/GPU:0'):
    # Öğrenme oranı ayarlayıcıyı ekle
    lr_reduction = keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, min_lr=1e-6)

    history = model_cnn.fit(
        train_generator,
        epochs=epochs,
        validation_data=validation_generator,
        callbacks=[lr_reduction]
    )

# Modeli değerlendir
loss, accuracy = model_cnn.evaluate(validation_generator)
print(f'Validation loss: {loss}')
print(f'Validation accuracy: {accuracy}')