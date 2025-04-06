# --- pages/1_House_Predictor.py ---
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from model1 import preprocess_data, train_models, prepare_input
import numpy as np

st.title("🔍 House Price Predictor")
st.sidebar.title("🏠 House Price Predictor")

st.sidebar.header("Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV (with required columns)", type="csv")

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

@st.cache_resource
def train_and_encode(data):
    data_encoded, encoder = preprocess_data(data)
    lin_reg, rf = train_models(data_encoded)
    reference_columns = data_encoded.drop(columns=['price']).columns.tolist()
    return data_encoded, encoder, lin_reg, rf, reference_columns

if uploaded_file:
    data = load_data(uploaded_file)
    st.success("✅ Data uploaded!")
else:
    data = load_data("data.csv")

required_cols = {"bedrooms", "bathrooms", "sqft", "age", "location", "air_conditioned", "price"}
if not required_cols.issubset(data.columns):
    st.error(f"Dataset must contain these columns: {required_cols}")
    st.stop()

data_encoded, encoder, lin_reg, rf, reference_columns = train_and_encode(data)

st.subheader("📋 Enter House Details")

bedrooms = st.number_input("Bedrooms", min_value=1, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, value=2)
sqft = st.number_input("Square Footage", min_value=300, value=1500)
age = st.number_input("Age of House", min_value=0, value=10)

location = st.selectbox("Location", options=sorted(data["location"].unique()))
air_conditioned = st.radio("Air Conditioned?", ["yes", "no"])

input_dict = {
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "sqft": sqft,
    "age": age,
    "air_conditioned": 1 if air_conditioned == "yes" else 0
}

if st.button("Compare Predictions"):
    final_input = prepare_input(input_dict, location, encoder, reference_columns)
    lin_pred = lin_reg.predict(final_input)[0]
    rf_pred = rf.predict(final_input)[0]

    st.success(f"📈 Linear Regression: ₹{lin_pred:,.2f}")
    st.success(f"🌲 Random Forest: ₹{rf_pred:,.2f}")

    st.subheader("📊 Price vs. Square Footage")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=data, x="sqft", y="price", hue="location", ax=ax)
    ax.set_title("Price vs. Square Footage")
    st.pyplot(fig)
