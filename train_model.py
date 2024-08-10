# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 10:50:13 2024

@author: yxg084228
"""

# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Cargar los datos del Titanic
df = pd.read_csv('titanic.csv')

# Preprocesamiento simple
df = df.dropna()
X = df[['Pclass', 'Age', 'SibSp', 'Parch']]
y = df['Survived']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo RandomForest
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Guardar el modelo entrenado
with open('titanic_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Modelo entrenado y guardado como 'titanic_model.pkl'")
