# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Charger modèle et scaler
model = joblib.load('xgb_model.joblib')

st.title("🏠 Prédiction de prix de logement en Californie")

# Création des inputs utilisateurs
MedInc = st.slider("Revenu médian", 0.5, 15.0, 3.0)
HouseAge = st.slider("Âge moyen des maisons", 1, 50, 20)
AveRooms = st.slider("Nombre moyen de pièces", 1, 10, 5)
AveBedrms = st.slider("Nombre moyen de chambres", 0.5, 5.0, 1.0)
Population = st.slider("Population", 100, 5000, 1000)
AveOccup = st.slider("Occupation moyenne", 1, 6, 3)
Latitude = st.slider("Latitude", 32.5, 42.0, 36.0)
Longitude = st.slider("Longitude", -124.3, -114.0, -120.0)

# Créer une observation
user_input = pd.DataFrame([[
    MedInc, HouseAge, AveRooms, AveBedrms,
    Population, AveOccup, Latitude, Longitude
]], columns=[
    'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
    'Population', 'AveOccup', 'Latitude', 'Longitude'
])

# Scaler + prédire
prediction = model.predict(user_input)[0]

st.subheader(f"🏡 Valeur estimée : {prediction:.2f}")
