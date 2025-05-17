import warnings
from streamlit_option_menu import option_menu
import numpy as np
import pickle
import streamlit as st
st.set_page_config(layout="wide")
warnings.filterwarnings('ignore')

# streamlit run Industrial_Copper.py

# Load Models


@st.cache_resource
def load_models():
    with open("Classification_model.pkl", "rb") as f:
        model_class = pickle.load(f)
    with open("Regression_Model.pkl", "rb") as f:
        model_regg = pickle.load(f)
    return model_class, model_regg


model_class, model_regg = load_models()

# Prediction Function for Status


def predict_status(features):
    y_pred = model_class.predict([features])
    return "WON" if y_pred[0] == 1 else "LOSE"

# Prediction Function for Selling Price


def predict_selling_price(features):
    y_pred = model_regg.predict([features])
    return np.exp(y_pred[0])  # Convert log price back to actual price


# Streamlit Page Configuration
st.title(":green[**INDUSTRIAL COPPER MODELING**]")


# Sidebar Menu
with st.sidebar:
    option = option_menu(
        menu_title='Predict Price/Status',
        options=["PREDICT SELLING PRICE", "PREDICT STATUS"],
        icons=['currency-dollar', 'bar-chart-line'],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "5px", "background-color": "#d3d3d3"},
            "icon": {"color": "#cc3366", "font-size": "20px"},
            "nav-link": {
                "font-size": "18px",
                "color": "#2C3E50",
                "padding": "10px",
                "border-radius": "5px"
            },
            "nav-link-selected": {
                "background-color": "#1ABC9C",
                "color": "white",
                "font-weight": "bold"
            },
        }
    )

# Selling Price Prediction Page
if option == "PREDICT SELLING PRICE":
    # st.header("PREDICT SELLING PRICE")
    st.markdown("## :blue[**PREDICT SELLING PRICE**]")
    col1, col2 = st.columns(2)

    with col1:
        country = st.number_input(
            "Enter COUNTRY (25-113)", min_value=25, max_value=113)
        status = st.number_input("Enter STATUS (0-8)",
                                 min_value=0.0, max_value=8.0)
        item_type = st.number_input(
            "Enter ITEM TYPE (0-6)", min_value=0.0, max_value=6.0)
        application = st.number_input(
            "Enter APPLICATION (2-87.5)", min_value=2.0, max_value=87.5)
        width = st.number_input("Enter WIDTH (700-1980)",
                                min_value=700.0, max_value=1980.0)
        # product_ref = st.number_input("Enter PRODUCT_REF (611728-1722207579)")
        product_ref = st.number_input("Enter PRODUCT_REF (611728-1722207579)",
                                      min_value=611728.0, max_value=1722207579.0)
        quantity_tons_log = st.number_input("Enter QUANTITY_TONS (Log Value)")
        customer_log = st.number_input("Enter CUSTOMER (Log Value)")

    with col2:
        thickness_log = st.number_input("Enter THICKNESS (Log Value)")
        item_date = [int(st.selectbox("ITEM DATE - Day", [str(i) for i in range(1, 32)])),
                     int(st.selectbox("ITEM DATE - Month",
                         [str(i) for i in range(1, 13)])),
                     int(st.selectbox("ITEM DATE - Year", ["2020", "2021"]))]
        delivery_date = [int(st.selectbox("DELIVERY DATE - Day", [str(i) for i in range(1, 32)])),
                         int(st.selectbox("DELIVERY DATE - Month",
                             [str(i) for i in range(1, 13)])),
                         int(st.selectbox("DELIVERY DATE - Year", ["2020", "2021", "2022"]))]

    st.markdown(
        "<style>div.stButton > button:first-child {background-color: #4CAF50; color: white; font-weight: bold; border-radius: 6px;}</style>", unsafe_allow_html=True)

    if st.button("PREDICT THE SELLING PRICE", use_container_width=True):
        features = [country, status, item_type, application, width, product_ref, quantity_tons_log,
                    customer_log, thickness_log] + item_date + delivery_date
        price = predict_selling_price(features)
        st.markdown(
            f"<h4 style='color:green;'>💰 The Selling Price is: ₹{price:.2f}</h4>", unsafe_allow_html=True)


# Status Prediction Page
if option == "PREDICT STATUS":
    # st.header("PREDICT STATUS (Won / Lose)")
    st.markdown("## :blue[**PREDICT STATUS (Won / Lose)**]")

    col1, col2 = st.columns(2)
    with col1:
        country = st.number_input(
            "Enter COUNTRY (25-113)", min_value=25, max_value=113)
        item_type = st.number_input(
            "Enter ITEM TYPE (0-6)", min_value=0.0, max_value=6.0)
        application = st.number_input(
            "Enter APPLICATION (2-87.5)", min_value=2.0, max_value=87.5)
        width = st.number_input("Enter WIDTH (700-1980)",
                                min_value=700.0, max_value=1980.0)
        # product_ref = st.number_input("Enter PRODUCT_REF (611728-1722207579)")
        product_ref = st.number_input("Enter PRODUCT_REF (611728-1722207579)",
                                      min_value=611728.0, max_value=1722207579.0)
        quantity_tons_log = st.number_input("Enter QUANTITY_TONS (Log Value)")
        customer_log = st.number_input("Enter CUSTOMER (Log Value)")
        thickness_log = st.number_input("Enter THICKNESS (Log Value)")

    with col2:
        selling_price_log = st.number_input("Enter SELLING PRICE (Log Value)")
        item_date = [int(st.selectbox("ITEM DATE - Day", [str(i) for i in range(1, 32)])),
                     int(st.selectbox("ITEM DATE - Month",
                         [str(i) for i in range(1, 13)])),
                     int(st.selectbox("ITEM DATE - Year", ["2020", "2021"]))]
        delivery_date = [int(st.selectbox("DELIVERY DATE - Day", [str(i) for i in range(1, 32)])),
                         int(st.selectbox("DELIVERY DATE - Month",
                             [str(i) for i in range(1, 13)])),
                         int(st.selectbox("DELIVERY DATE - Year", ["2020", "2021", "2022"]))]

    st.markdown(
        "<style>div.stButton > button:first-child {background-color: #FF5733; color: white; font-weight: bold; border-radius: 6px;}</style>", unsafe_allow_html=True)

    if st.button("PREDICT THE STATUS", use_container_width=True):
        features = [country, item_type, application, width, product_ref, quantity_tons_log, customer_log,
                    thickness_log, selling_price_log] + item_date + delivery_date
        status = predict_status(features)
        st.markdown(
            f"<h4 style='color:red;'>🚩 The Status is: {status}</h4>",
            unsafe_allow_html=True
        )
