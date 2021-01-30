# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 21:53:41 2021

@author: VolkanKarakuş
"""

#%% creating data frame
import pandas as pd

dictionary1={'NAME':['Volkan','Ali','Ayse'],
            'SURNAME':['Karakus','Uslu','Korkmaz'],
            'AGE':[25,24,26],
            }

dataFrame1=pd.DataFrame(dictionary1)

dictionary2={'NAME':['Kagan','Gungor','Emre','Berkay'],
             'SURNAME':['Sahbaz','Uludag','Aydin','Birol'],
             'AGE':[24,26,25,25]
             }
dataFrame2=pd.DataFrame(dictionary2)

#%% drop and concatenating

#bir tane feature i drop edelim.
#dataFrame1=dataFrame1.drop(['AGE'],axis=1) # salary level'i butun sutunlariyla drop et.
#yukaridaki islemi esitlemeden yapmanin yolu var.
#dataFrame1.drop(['AGE'],axis=1,inplace=True) # inplace=True kismi olmasa dataFrame1 aslen degismezdi.

#concatenating(birlestirme)
# vertical concetenating
dataConcatVertical=pd.concat([dataFrame1,dataFrame2],axis=0)

# horizontal concetanating
dataConcatHorizontal=pd.concat([dataFrame1,dataFrame2],axis=1)


#%% Transforming Data
dataConcatVertical.reset_index(inplace=True, drop=True) # dataFrame1 ve dataFrame2'yi birlestirmistik. 
                                                        # burada indexler 0 1 2 3 0 1 2 3 diye gidiyordu.
                                                        # Bunu burada duzelttik.
dataFrame3=dataConcatVertical

#simdi yeni bir column olusturup, yasin 2 katini almak istiyorum.
#1.YOL(LIST COMPREHENSION)
dataFrame3['2_times_age']=[each*2 for each in dataFrame3.AGE]

#2.YOL (APPLY METHOD)
def multiply(age):
    return age*2

#apply metodu ile 
dataFrame3['2_TIMES_AGE']=dataFrame3.AGE.apply(multiply)


