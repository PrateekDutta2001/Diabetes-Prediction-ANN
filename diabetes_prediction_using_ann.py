# -*- coding: utf-8 -*-
"""Diabetes-Prediction-using-ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XxEkJ_Uxh0YzRApXvVcph5SdKJewWBfP
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/gdrive/')
# %cd /gdrive

ls

cd/gdrive/My Drive/ANN-Diabetes/

ls

import numpy as np 
import pandas as pd

df = pd.read_csv('diabetes.csv')

df.head()

df.shape

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(15,10))
sns.heatmap(df.corr(),annot=True)

sns.pairplot(df)

sns.lineplot(x='Age',y='Glucose',hue='Outcome',data=df)

"""From the above graph it is very much clear that people with high glucose levels are more likely to have diabetes."""

sns.countplot(x='Outcome',data=df)

plt.figure(figsize=(15,10))
sns.countplot(x='Pregnancies',hue='Outcome',data=df)

sns.lineplot(x='Age',y='BloodPressure',hue='Outcome',data=df)

sns.lineplot(x='Age',y='Insulin',hue='Outcome',data=df)

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

X = df.iloc[:,0:-1].values
y = df.iloc[:,-1].values

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

import tensorflow as tf
ann = tf.keras.Sequential()

ann.add(tf.keras.layers.Dense(units=12,activation='relu'))
ann.add(tf.keras.layers.Dense(units=12,activation='relu'))
ann.add(tf.keras.layers.Dense(units=12,activation='relu'))
ann.add(tf.keras.layers.Dense(units=1,activation='sigmoid'))

ann.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

ann.fit(X_train,y_train,batch_size=12,epochs=200)

y_pred = ann.predict(X_test)
y_pred = (y_pred>0.75)

for i in range(len(y_pred)):
    print("Predicted %d------> Expected %d" %(y_pred[[i]],y_test[i]))

from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_pred,y_test)
acc = accuracy_score(y_pred,y_test)

cm

acc

