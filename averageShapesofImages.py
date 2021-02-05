# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 04:47:06 2021

@author: VolkanKarakuş
"""
import glob
import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt 

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
    w.append(image_data[each].shape[1])
    h.append(image_data[each].shape[0])

columnName1=['Widths']
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

landscape=dataWH.Widths>dataWH.Heights
dataWH['Shape']=['landscape' if i==True else 'portrait' for i in landscape]

filteredLandscape=dataWH[dataWH.Shape=='landscape']
filteredPortrait=dataWH[dataWH.Shape=='portrait']
numericFeaturesFilteredLandscape=filteredLandscape.describe()
numericFeaturesFilteredPortrait=filteredPortrait.describe()

#histogram
# plt.hist(dataFrameW.Widths,bins=50,color='red',alpha=0.5,label='Widhts')
# plt.hist(dataFrameH.Heights,bins=50,color='green',alpha=0.5,label='Heights')
# plt.legend()
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.show()

# plt.hist(filteredLandscape.Widths,bins=50,color='red',alpha=0.5,label='Widths')
# plt.hist(filteredLandscape.Heights,bins=50,color='green',alpha=0.5,label='Heights')
# plt.legend()
# plt.ylabel('Frequency')
# plt.title('Histogram of Landscape')
# plt.show()

plt.hist(filteredPortrait.Widths,bins=50,color='red',alpha=0.5,label='Widths')
plt.hist(filteredPortrait.Heights,bins=50,color='green',alpha=0.5,label='Heights')
plt.legend()
plt.ylabel('Frequency')
plt.title('Histogram of Portrait')
plt.show()
