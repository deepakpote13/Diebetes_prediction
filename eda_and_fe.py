# -*- coding: utf-8 -*-
"""EDA_and_FE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/deepakpote1/Data-Science/blob/master/Diebetes/EDA_and_FE.ipynb
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline
pd.pandas.set_option('display.max_columns',None)

"""### Exploratory Data Analysis

#### Uploading the dataset
"""

dataset = pd.read_csv('diabetes_dataset.csv')

dataset

"""#### Finding number of features"""

dataset.shape # (768, 9)

dataset.columns.values 
'''array(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
       'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
      dtype=object)'''

dependent_variable = ['Outcome'] # 1 = having diebetes
indepenent_variables = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
       'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

"""#### Finding missing values in the dataset"""

dataset.isnull().sum() # missing value
#for i in dataset.columns.values:
 #   print('{} : {}'/format(i, dataset[i].isna().sum()))

"""#### Finding Numerical Features"""

#All the features are numerical features

# No date feature is present

# All features are continueous features

for i in indepenent_variables:
    data=dataset.copy()
    data[i].hist(bins=10)
    plt.xlabel(i)
    plt.ylabel("Count")
    plt.title(i)
    plt.show()
#Features not following gaussian dist :
non_gauss = ['Pregnancies', 'Insulin','DiabetesPedigreeFunction', 'Age']  #Right Skewd
#Features following gaussian dist :
#['Glucose', 'BloodPressure', 'SkinThickness', 'BMI']
#From the histogram we can observe that some features like ['Glucose','BloodPressure', 'BMI'] should not be zero

"""#### Finding features containing zeroes."""

p=[]
for i in indepenent_variables:
    if any(dataset[i]==0):
        p.append(i)
p

#Age is the only variable which do not contain zero.
#Trying to make it normal dist.
data = dataset.copy()
data['Age'] = np.log(data['Age'])
data['Age'].hist(bins=10)
plt.xlabel('Age')
plt.ylabel("Count")
plt.title('Age')
plt.show() # not forming normal Dist.
'''for i in non_gauss:
    data=dataset.copy()
    data=dataset.copy()
    if 0 in data[i]:
        continue
    else:
        #data[i]= data[i].apply(lambda x: np.log(x) if x!=0 else np.nan)
        data[i]= np.log(data[i])
        data[i].hist(bins=50)
        plt.xlabel(i)
        plt.ylabel("Count")
        plt.title(i)
        plt.show()'''
#not possible

# Insulin and Pregnancies can be zero but others can't. So we droping these two features from zero_features. 
# First replacing zero values of zero_features ['Glucose','BloodPressure', 'BMI'] features with mode
#'Glucose' contains 5 zeroes
#'BloodPressure' contains 35 zeroes
#''BMI' contains 11 zeroes
zero_features = ['Glucose','BloodPressure', 'BMI', 'SkinThickness']
for i in zero_features:
    print('{}: {}'.format(i,(dataset[dataset[i]==0][i].count())/768))
#dataset[dataset['BMI']==0]['BMI'].count()

dataset.corr()

# Checking whether data is imbalanced or not
dataset.groupby('Outcome').count()
#outcome 0 is having 500 values
#outcome 1 is having 268 values

"""### Feature Engineering"""

# First replacing zero values of ['Glucose','BloodPressure', 'BMI'] features with median
for i in zero_features:
    k=dataset[i][dataset[i]>0].median()
    dataset[i][dataset[i]==0]=k
    #dataset[i][dataset[i].values==k]
zero_features = ['Glucose','BloodPressure', 'BMI', 'SkinThickness']
for i in zero_features:
    print('{}: {}'.format(i,(dataset[dataset[i]==0][i].count())/768))

#SkinThickness feature contains upper boundary ouliers
dataset['SkinThickness'][dataset['SkinThickness'] > 80] = dataset['SkinThickness'][dataset['SkinThickness']<=80].median()
for i in indepenent_variables:
    data=dataset.copy()
    data[i].hist(bins=10)
    plt.xlabel(i)
    plt.ylabel("Count")
    plt.title(i)
    plt.show()

# Handling imbalanceness of dataset
#Here, our dataset is not large enough to apply downsampling
#So, we will upsample the data

#dataset.to_csv('Dataset_after_feature_engineering.csv', index = False)

