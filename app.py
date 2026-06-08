import streamlit as st
import pandas as pd
import joblib
import os

# Page title

st.set_page_config(page_title="Laptop Price Predictor")

st.title("💻 Laptop Price Predictor")

# Debug information

st.write("Files in directory:", os.listdir())

# Initialize variable

model_loaded = False

# Load model

try:
    st.write("Model exists:", os.path.exists("laptop_price_model.pkl"))

    model = joblib.load("laptop_price_model.pkl")
    model_loaded = True

    st.success("Model loaded successfully!")


except Exception as e:
    st.error(f"Error Type: {type(e).__name__}")
    st.error(f"Error Details: {repr(e)}")

st.write("Enter laptop specifications")

# Inputs

inches = st.number_input(
"Screen Size (Inches)",
min_value=10.0,
max_value=20.0,
value=15.6
)

ram = st.number_input(
"RAM (GB)",
min_value=2,
max_value=128,
value=8
)

weight = st.number_input(
"Weight (kg)",
min_value=0.5,
max_value=10.0,
value=2.0
)

x_res = st.number_input(
"Screen Width Resolution",
min_value=800,
value=1920
)

y_res = st.number_input(
"Screen Height Resolution",
min_value=600,
value=1080
)

ssd = st.number_input(
"SSD Storage (GB)",
min_value=0,
value=256
)

notebook = st.selectbox(
"Is Type Notebook?",
["No", "Yes"]
)

workstation = st.selectbox(
"Is Type Workstation?",
["No", "Yes"]
)

# Convert to numeric

notebook = 1 if notebook == "Yes" else 0
workstation = 1 if workstation == "Yes" else 0

# Prediction button


if st.button("Predict Price"):

    if not model_loaded:
        st.error("Model could not be loaded.")

    else:
        input_data = pd.DataFrame({
            "Inches": [inches],
            "Ram": [ram],
            "Weight": [weight],
            "X_res": [x_res],
            "Y_res": [y_res],
            "SSD": [ssd],
            "TypeName_Notebook": [notebook],
            "TypeName_Workstation": [workstation]
        })

        try:
            prediction = model.predict(input_data)[0]
            st.success(f"Estimated Laptop Price: €{prediction:.2f}")

        except Exception as e:
            st.error(f"Prediction Error: {repr(e)}")
