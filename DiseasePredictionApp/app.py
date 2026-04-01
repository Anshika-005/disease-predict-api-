import streamlit as st
import pickle
import json

# Load model & encoder
model = pickle.load(open("model.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# Load symptoms list
with open("columns.json") as f:
    symptoms_list = json.load(f)

# Page setup
st.set_page_config(page_title="Disease Predictor", layout="centered")

st.title("🧠 Disease Prediction System")
st.write("Select your symptoms to predict disease")

# Sidebar
st.sidebar.title("About")
st.sidebar.info("AI-based disease prediction system")

# User input
selected_symptoms = st.multiselect(
    "Choose symptoms:",
    symptoms_list
)

# Convert input to model format
input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptoms_list]

# Predict button
if st.button("Predict"):

    if len(selected_symptoms) == 0:
        st.warning("Please select at least one symptom")
    else:
        prediction = model.predict([input_data])
        disease = le.inverse_transform(prediction)

        st.success(f"🩺 Predicted Disease: {disease[0]}")

        st.warning("⚠️ Not a medical diagnosis. Consult a doctor.")

        st.write("### Selected Symptoms:")
        st.write(", ".join(selected_symptoms))