#!/usr/bin/env python
# coding: utf-8

# # MK Praktikum Unggulan Universitas Gunadarma
# # Mata Kuliah: Praktikum Komputasi Big Data (Tingkat 2)  
# ---
# # Praktikum V
# 
# 
# ![1_L0464qoX7pSkIQMBcF73Tg.png](attachment:1_L0464qoX7pSkIQMBcF73Tg.png)
# 
# Gambar diatas menunjukkan tahapan yang Anda perlu lakukan ketika ingin membangun sebuah model *artificial intelligence*. 
# Pada minggu ini Anda akan melakukan fase data cleansing atau pembersihan data. Tahapan ini biasanya dilakuakan sebelum anda melakukan tahapan EDA yang telah Anda pelajari sebelumnya. Tahapan ini perlu dilakukan jika data yang Anda miliki tidak 'bersih', sehingga perlu dilakukan pemrosesan terlebih dahulu (tahapan pre-processing) sebelum data tersebut masuk kedalam algoritma pembangunan model. 
# 
# Materi praktikum ini dibagi menjadi 2 bagian dengan menggunakan dua dataset yang berbeda. Adapun operasi akan Anda lakukan antara lain:
# * Melihat bentuk data (shape) dari data train dan data test set.
# * Cek data NaN, bila ada maka hapus/drop data NaN tersebut.
# * Cek outliers, bila ada maka hapus/drop outliers tersebut.
# * Melakukan konversi jenis kolom yang relevan.
# * Melakukan transformasi terhadap data yang bersifat kategori.
# 
# Operasi yang Anda lakukan pada tahapan pembersihan data sangat bergantung pada karakteristik permasalahan, karakter data, serta jenis data yang terdapat dalam dataset Anda. Sebagai referensi, berikut bagan dari berbagai macam tipe data yang mungkin Anda temui dalam sebuah dataset. 

# 
# ![8UUywzzaMhY2ZGHrWE7VkA_b.png](attachment:8UUywzzaMhY2ZGHrWE7VkA_b.png)

# In[ ]:


import numpy as np 
import pandas as pd 
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# ### Dataset 1
# 
# Dataset yang akan Anda gunakan pada praktikum kali ini adalah dataset transaksi taksi di kota New York. Dataset ini memiliki jumlah sebanyak 200.000 data dengan 8 fitur. 

# In[ ]:


# Load data train dan test ke dalam pandas dataframe
train = pd.read_csv("https://raw.githubusercontent.com/supasonicx/ATA-praktikum-01/main/Split-200000.csv")


# ## BAGIAN 1 : DATA CLEANSING PENGHILANGAN MISSING VALUE DAN DATA ANOMALI
# 
# Pada bagian ini, Anda akan mempraktikan cara untuk:
# * Melihat bentuk data (shape) dari data train dan data test set.
# * Cek data NaN, bila ada maka hapus/drop data NaN tersebut.
# * Cek outliers, bila ada maka hapus/drop outliers tersebut.
# * Melakukan konversi jenis kolom yang relevan.

# In[ ]:


# Menghasilkan jumlah baris dan jumlah kolom (bentuk data) pada data train dengan fungsi shape
train.shape


# In[ ]:


# Menampilkan 10 data teratas
train.head(10)


# In[ ]:


# Fungsi describe() untuk mengetahui statistika data untuk data numeric seperti count, mean, standard deviation, maximum, mininum, dan quartile
train.describe()


# In[ ]:


# Cek nilai yang hilang atau missing values di dalam data train
train.isnull().sum().sort_values(ascending=False)


# Missing values adalah nilai yang tidak terdefinisi di dataset. Bentuknya beragam, bisa berupa blank cell, ataupun simbol-simbol tertentu seperti NaN (Not a Number), NA (Not Available), ?, -, dan sebagainya. Missing values dapat menjadi masalah dalam analisis data serta tentunya dapat mempengaruhi hasil modelling machine learning. **Dari hasil diatas data train mengandung 1 data missing values pada kolom/field dropoff_latitude dan dropoff_longitude.**

# Dari hasil diatas data test ternyata tidak memiliki missing values.

# In[ ]:


# Drop atau hapus data missing values
train = train.drop(train[train.isnull().any(axis=1)].index, axis=0)


# In[ ]:


train.shape


# Diatas dapat terlihat hasil dimensi/shape data setelah drop/hapus missing values.

# **Melakukan pemeriksaan dan membersihkan data yang dinilai 'anomali' setiap kolom pada data train:**
# 1. fare_amount
# 2. passanger_count
# 3. pickup_longitude
# 4. pickup_latitude
# 5. dropoff_longitude 
# 6. dropoff_latitude

# In[ ]:


# Periksa kolom target yaitu kolom fare_amount
train['fare_amount'].describe()


# Data target adalah fitur dari dataset yang ingin Anda pahami lebih dalam.
# **Dari output diatas**, kolom target fare amount atau jumlah tarif memiliki nilai negatif, yang tidak masuk akal sehingga kita hapus kolom ini.

# In[ ]:


# Seleksi nilai negatif, dan menghasilkan 38 kolom fare_amount memiliki nilai negatif 
from collections import Counter
Counter(train['fare_amount']<0)


# In[ ]:


# Hapus nilai negatif kemudian cek dimensi data dengan fungsi shape
train = train.drop(train[train['fare_amount']<0].index, axis=0)
train.shape


# In[ ]:


# Terlihat pada output tidak ada lagi nilai negatif pada kolom fare_amount
train['fare_amount'].describe()


# In[ ]:


# Terlihat pada output jumlah tarif tertiggi adalah $500
train['fare_amount'].sort_values(ascending=False)


# **Selanjutnya: Periksa kolom passenger_count.**

# In[ ]:


train['passenger_count'].describe()


# In[ ]:


# Asumsinya, menurut aturan batas maksimum penumpang dalam sebuah taksi adalah 6 (enam).
# Ini PASTI outlier. Mari kita drop atau hapus.
train[train['passenger_count']>=6]


# In[ ]:


# Jauh lebih rapi sekarang! Jumlah penumpang maksimal adalah 6 (enam).
train['passenger_count'].describe()


# **Selanjutnya: Periksa kolom pickup_latitude dan pickup_longitudes.**

# In[ ]:


# Mari kita eksplore kolom pickup latitude dan longitudes.
train['pickup_latitude'].describe()


# * Garis lintang berkisar dari -90 hingga 90.
# * Garis bujur berkisar dari -180 hingga 180.
# 
# Uraian di atas dengan jelas menunjukkan beberapa outlier. <br>
# 
# Mari kita saring mereka:

# In[ ]:


train[train['pickup_latitude']<-90]


# In[ ]:


train[train['pickup_latitude']>90]


# In[ ]:


# Hapus data outliers tersebut
train = train.drop(train[(train['pickup_latitude'] < -90) | (train['pickup_latitude'] > 90)].index, axis=0)


# In[ ]:


# Dengan menggunakan fungsi shape, terlihat perbedaan adanya 12 baris terhapus.
train.shape


# In[ ]:


# Lakukan operasi yang sama untuk kolom pickup longitude.
train['pickup_longitude'].describe()


# In[ ]:


# Cek data yang bernilai lebih dari -180.
train[train['pickup_longitude']<-180]


# In[ ]:


# Cek data yang bernilai lebih dari 180.
train[train['pickup_longitude']>180]


# In[ ]:


train = train.drop(train[train['pickup_longitude']<-180].index, axis = 0)


# **Selanjutnya: Periksa kolom dropoff_latitude dan dropoff_longitudes.**

# In[ ]:


# Lakukan operasi yang sama untuk kolom dropoff latitude and longitude.
# Cek data yang bernilai lebih dari -90
train[train['dropoff_latitude']<-90]


# In[ ]:


# Cek data yang bernilai lebih dari 90
train[train['dropoff_latitude']>90]


# In[ ]:


# Hapus data outliers
train = train.drop(train[train['dropoff_latitude']>90].index, axis=0)


# In[ ]:


# Dengan menggunakan fungsi shape, terlihat perbedaan adanya 8 kolom terhapus.
train.shape


# **Periksa tipe data setiap kolom data train.**

# In[ ]:


# Menampilkan tipe data dari dataset dengan fungsi dtypes.
train.dtypes


# key and pickup_datetime tampaknya menjadi kolom datetime yang dalam format objek. 
# <br><br>
# Mari kita ubah menjadi datetime:

# In[ ]:


train['key'] = pd.to_datetime(train['key'])
train['pickup_datetime']  = pd.to_datetime(train['pickup_datetime'])


# In[ ]:


# Cek tipe data setelah di konversi.
train.dtypes


# In[ ]:


# Cek data train setelah di cleansing.
train.head()


# **Data sudah selesai di cleansing, dan selanjutnya siap untuk di masukkan kedalam model machine learning :)**

# ## BAGIAN 2 : TRANSFORMASI DATA DENGAN TIPE KATEGORI
# 
# Pada bagian ini, Anda akan mempraktikan cara untuk:
# * Melakukan transformasi terhadap data yang bersifat kategori 

# ### Dataset 2
# 
# Dataset yang akan Anda gunakan pada bagian ini adalah data sensus penduduk. Dataset ini memiliki jumlah sebanyak 48842 data dengan 15 fitur. 

# In[ ]:


from sklearn.preprocessing import OrdinalEncoder
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy.stats import ttest_ind, ttest_rel
from scipy import stats


# In[ ]:


data = pd.read_csv("https://gitlab.com/andreass.bayu/file-directory/-/raw/main/adult.csv", na_values="?" )
print('Number of rows: '+ format(data.shape[0]) +', number of features: '+ format(data.shape[1]))


# In[ ]:


## Menampilkan 10 baris teratas pada dataset.
data.head(10)


# In[ ]:


## Cek apakah terdapat nilai NA pada dataset.

C = (data.dtypes == 'object')
CategoricalVariables = list(C[C].index)

Integer = (data.dtypes == 'int64') 
Float   = (data.dtypes == 'float64') 
NumericVariables = list(Integer[Integer].index) + list(Float[Float].index)

Missing_Percentage = (data.isnull().sum()).sum()/np.prod(data.shape)*100
print("The number of missing entries before cleaning: " + str(round(Missing_Percentage,5)) + " %")


# In[ ]:


## Menampilkan seluruh list fitur yang ada.
list(data.columns)


# In[ ]:


data.dtypes


# In[ ]:


data.education.unique()


# In[ ]:


## Terdapat error saat menarik nilai unique pada kolom native-country
data.native-country.unique()


# In[ ]:


## Melakukan rename kolom, karena kolom dengan tanda "-" tidak bisa dibaca program
dataRename = data.rename(columns={'marital-status': 'maritalStatus',
                                 'native-country':'native_country'})


# In[ ]:


dataRename.head(5)


# In[ ]:


## Sintaks untuk melakukan transformasi untuk kolom marital_status dengan fungsi maping.

maritalStatus_map  = {'Never-married':0,'Married-civ-spouse':1,'Widowed':2, 'Divorced':3,'Separated':4,'Married-spouse-absent':5,'Married-AF-spouse':6}

dataRename['maritalStatus'] = dataRename['maritalStatus'].map(maritalStatus_map)
dataRename.head()


# In[ ]:


## Sintaks untuk melakukan transformasi untuk kolom marital_status dengan fungsi cat.codes
dataRename["race"] = dataRename["race"].astype('category')
dataRename["race_encoded"] = dataRename["race"].cat.codes
dataRename.head()


# In[ ]:


## Sintaks untuk melakukan transformasi untuk kolom marital_status dengan fungsi Ordinal Encoder dari library sklearn
ord_enc = OrdinalEncoder()
dataRename["gender"] = ord_enc.fit_transform(dataRename[["gender"]])
dataRename[["gender", "gender"]].head(10)


# In[ ]:


dataRename['maritalStatus'].hist(figsize=(8,8))
plt.show()


# In[ ]:


dataRename = dataRename.rename(columns={'capital-gain': 'capitalGain'})
dataRename['capitalGain'].describe()


# In[ ]:


dataRename.head(5)


# In[ ]:


dataRename.race.unique()


# In[ ]:


race1 = dataRename[dataRename["race_encoded"] == 1]
race2 = dataRename[dataRename["race_encoded"] == 2]
race3 = dataRename[dataRename["race_encoded"] == 3]
race4 = dataRename[dataRename["race_encoded"] == 4]
race5 = dataRename[dataRename["race_encoded"] == 5]


# In[ ]:


race2.dtypes


# In[ ]:


race1.head(10)


# In[ ]:


plt.figure(figsize=(7,7))
total = float(len(race4) )

ax = sns.countplot(x="income", data=race4[race4["age"]>70])
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2.,
            height + 3,
            '{:1.2f}'.format((height/total)*100),
            ha="center") 
plt.show()


# In[ ]:


fig = plt.figure(figsize=(10,10)) 
sns.boxplot(x="income", y="age", data=race3)
plt.show()


# ### Instruksi Praktikum untuk mahasiswa FIKTI dan FTI (kecuali Teknik Industri, Teknik Mesin dan Agroteknologi)
# * Lakukan teknik data cleaning untuk data yang bernilai NaN pada Dataset 2. 
# * Lakukan analisis histogram kolom <code>income</code> pada setiap kategori race, apakah yang dapat Anda simpulkan ?
# * Ganti kolom <code>hours-per-week</code> dengan nama <code>hoursPerWeek</code>
# * Berapa jumlah responden yang bekerja lebih dari 40 jam per minggunya untuk masing-masing kategori race?  

# ### Instruksi Praktikum mahasiswa Teknik Industri, Teknik Mesin, Agroteknologi, FTSP, FIKF
# 
# * Ganti kolom <code>hours-per-week</code> dengan nama <code>hoursPerWeek</code>
# * Lakukan analisis histogram pada kolom <code>hoursPerWeek</code> pada setiap data race1, race2, race3, race4 dan race5. Informasi apa yang dapat Anda simpulkan ?
# * Terdapat berapa kategori data yang mengisi kolom <code>workclass</code>? Apa saja kategori yang ada?
# * Jelaskan hasil boxplot yang diperoleh untuk data <code>income</code> dan umur untuk data race1 !

# <div class="alert alert-info">
#     <strong>Catatan!</strong><br>
#     Pada bagian <code>#CODE HERE</code> digantikan dengan code python sesuai dengan perintah.<br>
#     </div>

# <div class ="alert alert-warning">
# <strong>Notes: </strong> Tambahkan cell code jika dibutuhkan.
# </div>

# In[ ]:


# No 1
# CODE HERE ...


# In[ ]:


# No 2
# CODE HERE ...


# In[ ]:


# No 3
# CODE HERE ...


# In[ ]:


# No 4
# CODE HERE ...


# 
# 
# ---
# 
# 
# Copyright © Pengelola MK Praktikum Unggulan (Praktikum DGX), Universitas Gunadarma 
# 
# 
# https://www.praktikum-hpc.gunadarma.ac.id/
