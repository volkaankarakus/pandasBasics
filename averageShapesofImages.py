# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 04:47:06 2021

@author: VolkanKarakuş
"""

import glob
import numpy as np
import cv2
import pandas as pd
# Import all image files with the .jpg extension
files = glob.glob ("*.jpg")
image_data = []
for my_file in files:
    this_image = cv2.imread(my_file, 1)
    image_data.append(this_image)
    
w=[]
h=[]
x=list(range(len(image_data)))
for each in x:
    w.append(image_data[each].shape[0])
    h.append(image_data[each].shape[1])

columnName1=['Weights']
dataFrameW=pd.DataFrame(data=w,columns=columnName1)
numericFeaturesW=dataFrameW.describe()

columnName2=['Heights']
dataFrameH=pd.DataFrame(data=h,columns=columnName2)
numericFeaturesH=dataFrameH.describe()

print(numericFeaturesW)
print(numericFeaturesH)

#horizontal concatenating
dataWH=pd.concat([dataFrameW,dataFrameH],axis=1)
#index reset
dataWH.reset_index(inplace=True,drop=True)
print(dataWH)

#histogram
plt.hist(dataFrameW.Weights,bins=20,color='red',label='Weights')
plt.hist(dataFrameH.Heights,bins=20,color='green',label='Heights')
plt.legend()
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
