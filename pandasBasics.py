# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 01:55:41 2021

@author: VolkanKarakuş
"""
#1) pandas, dataframeleri kullanmak icin hizli ve etkili.
# dataframe bir excel dosyasi gibi.

# isim yas  medeni hal
# veli 20      bekar
# ahmet 25     bekar gibi...

#2) csv ve text dosyalarini acip inceleyip,sonuclari bu dosya tiplerine rahatlikla kaydedilebilir.

#3) Datanin icinde her zaman tum degerler olmak zorunda degil.
#   bazi missing datalar olabilir. -> birinin maasini yazmayi unutmus olabiliriz.(NaN value)
#   missing data'lar icin pandas kolaylik saglar.

#4) reshape'i daha etkili kullanabiliriz.
#5) sliceing ve indexing kolay. 25 yasindan buyukleri cikar gibi.
#6) time series data analysis'de cok yardimci. zaman-hız gibi.
#7) HERSEYDEN ONEMLISI PROJELERDE PANDAS COK HIZLI(OPTIMIZE EDILMIS)

import pandas as pd

dictionary={'NAME':['ali','veli','kenan','ayse','evren'],
            'AGE':[15,43,23,56,12],
            'SALARY':[10,20,21,40,22]}

dataFrame1=pd.DataFrame(dictionary) # dataframe'i olusturduk. excel dosyasina benzedi.
head=dataFrame1.head() # datalari genelde import edince iceriginde ne varmis diye bi öninceleme icin gerekli.
                       # ilk 5 datayi verir.
tail=dataFrame1.tail() # son 5 datayi verir.

# head ya da tailin icini 4 le doldursaydik. 4 datayi verecekti.
#%%
# pandas Basic Methods
columns=dataFrame1.columns # it gives the columns names. NAME,AGE,SALARY
info=dataFrame1.info() # ciktisi : 5 girdi var. 0'dan 4 e . Data column =3 (indexi column olarak saymaz.)
dataTypes=dataFrame1.dtypes # herbir feature'in data type'ini verir.
numericFeatures=dataFrame1.describe() #numeric featurelara ait ozellikleri verir.max,min,count,std gibi. %50 dedigi:medyan.

#%% Indexing and Slicing
#ben sadece isimleri almak istiyorsam:
name=dataFrame1['NAME']
# ya da 
name2=dataFrame1.NAME

#yeni bir feature eklemek istersek:
dataFrame1['COUNTRY']=['England','Finland','Norway','Canada','USA']

#tum satirlari al, sadece COUNTRY feature'ini al.
country=dataFrame1.loc[:,'COUNTRY']
ilk4Country=dataFrame1.loc[:3,'COUNTRY'] # numpy ve pythonda 3 exclusive'di.pandasta inclusive!!!

# ilk 3 satir, featurelar da AGE'den COUNTRY'ye
example=dataFrame1.loc[:2,'AGE':'COUNTRY']

#ilk 3 satir, featurelar sadece AGE ve COUNTRY
example2=dataFrame1.loc[:2,['AGE','COUNTRY']]

#dataFrame'i tersten yazdir.
example3=dataFrame1.loc[::-1,:]

#tum satirlari yazdir ama AGE'e kadar olan featurelari yazdir.
example4=dataFrame1.loc[:,:'AGE'] # pandasta inclusive
#yukaridaki ornegi feature ismi yerine indexi olarak yazabiliriz.
example5=dataFrame1.iloc[:,:2] # INDEX LOCATION

#%% FILTERING
# mesela maası 20'nin uzerinde olanlari bulmak istiyoruz.
filter1=dataFrame1.SALARY >20
#filter1'e baktigimizda False False True True True döndü.
typeFilter=type(filter1) # pandas Serisi dondu. -> tek bir column donerse buna seri deniyor.

filteredData=dataFrame1[filter1]

#yasi genc, ve maasi iyi birisi olsun.
filter2=dataFrame1.AGE <20 
filteredData2=dataFrame1[filter1 & filter2]

#filtre yazmadan direkt olarak da yapabiliriz.
filteredData3=dataFrame1[dataFrame1.AGE<20]

#%% LIST COMPREHENSION
averageSalary=dataFrame1.SALARY.mean()
#ortalama maasi numpy ile de bulabiliriz.
import numpy as np
averageSalaryNumpy=np.mean(dataFrame1.SALARY)

#yeni bir feature olusturup ortalama maas uzerınde alanlara yuksek, altındakilere dusuk maas demek istiyorum.
dataFrame1['SALARY LEVEL']=['high' if each>averageSalary else 'low' for each in dataFrame1.SALARY]

#%%
# sacma yazilmis bir feature olusturup bunu duzeltelim.
dataFrame1['cOLoR']=['White','White','Black','White','Black']

dataFrame1.columns=[each.lower() for each in dataFrame1.columns] #hepsini kucuk yazdik.

#simdi SALARY LEVEL bosluklu oldugu icin bunu once ayirip sonra birlestirelim.
dataFrame1.columns=[each.split()[0]+'_'+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]
