# Laptop Price Predictor

A machine learning web application that predicts laptop prices based on hardware specifications such as RAM, weight, screen size, storage, and display resolution.

## Features

* Predicts laptop prices using a trained Random Forest Regressor.
* Interactive web interface built with Streamlit.
* Real-time price prediction based on user inputs.
* Lightweight and easy to deploy.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

## Model Features

The model uses the following features:

* Inches
* Ram
* Weight
* X_res
* Y_res
* SSD
* TypeName_Notebook
* TypeName_Workstation

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd laptop-price-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Project Structure

```text
.
├── app.py
├── laptop_price_model.pkl
├── requirements.txt
├── README.md
└── .streamlit/
```

## Deployment

The application can be deployed using Streamlit Community Cloud.

## Author

Farooq Khan
