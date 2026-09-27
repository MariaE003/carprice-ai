import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics import r2_score


# charger le modele
model = joblib.load("./model/car_price_model.pkl")


st.title("Prédicteur de prix de voitures d'occasion")

st.write(
    "Entrez les caractéristiques du véhicule "
    "pour obtenir une estimation de son prix."
)


year = st.number_input(
    "Année",
    min_value=1990,
    max_value=2026,
    value=2018
)


km_driven = st.number_input(
    "Kilométrage",
    min_value=0,
    value=50000
)


fuel = st.selectbox(
    "Carburant",
    ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
)


seller_type = st.selectbox(
    "Type de vendeur",
    ["Individual", "Dealer", "Trustmark Dealer"]
)


transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)


owner = st.selectbox(
    "Proprietaire",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
)


if st.button("estimer le prix"):

    car = pd.DataFrame({
        "year": [year],
        "km_driven": [km_driven],
        "fuel": [fuel],
        "seller_type": [seller_type],
        "transmission": [transmission],
        "owner": [owner]
    })

    prediction = model.predict(car)
    st.success(
        f"Prix estimé : {prediction[0]:,.0f}"
    )