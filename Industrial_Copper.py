# import streamlit as st
# import pickle
# import numpy as np
# import sklearn
# from streamlit_option_menu import option_menu


# # Functions
# def predict_status(ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,slgplg,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):

#     #change the datatypes "string" to "int"
#     itdd= int(itmdt)
#     itdm= int(itmmn)
#     itdy= int(itmyr)

#     dydd= int(deldtdy)
#     dydm= int(deldtmn)
#     dydy= int(deldtyr)
#     #modelfile of the classification
#     with open("Classification_model.pkl","rb") as f:
#         model_class=pickle.load(f)

#     user_data= np.array([[ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,slgplg,itdd,itdm,itdy,dydd,dydm,dydy]])
                       
    
#     y_pred= model_class.predict(user_data)

#     if y_pred == 1:
#         return 1
#     else:
#         return 0

# def predict_selling_price(ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):
                   

#     #change the datatypes "string" to "int"
#     itdd= int(itmdt)
#     itdm= int(itmmn)
#     itdy= int(itmyr)

#     dydd= int(deldtdy)
#     dydm= int(deldtmn)
#     dydy= int(deldtyr)
#     #modelfile of the classification
#     with open("Regression_Model.pkl","rb") as f:
#         model_regg=pickle.load(f)

#     user_data= np.array([[ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
#                        itdd,itdm,itdy,dydd,dydm,dydy]])
    
#     y_pred= model_regg.predict(user_data)

#     ac_y_pred= np.exp(y_pred[0])

#     return ac_y_pred


# st.set_page_config(layout= "wide")

# st.title(":blue[**INDUSTRIAL COPPER MODELING**]")

# with st.sidebar:
#     option = option_menu('SUDHAKAR', options=["PREDICT SELLING PRICE", "PREDICT STATUS"])

# if option == "PREDICT STATUS":

#     st.header("PREDICT STATUS (Won / Lose)")
#     st.write(" ")

#     col1,col2= st.columns(2)

#     with col1:
#         country= st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
#         item_type= st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
#         application= st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
#         width= st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
#         product_ref= st.number_input(label="**Enter the Value for PRODUCT_REF**/ Min:611728, Max:1722207579")
#         quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**/ Min:-0.322, Max:6.924",format="%0.15f")
#         customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910, Max:17.23015",format="%0.15f")
#         thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.71479, Max:3.28154",format="%0.15f")
    
#     with col2:
#         selling_price_log= st.number_input(label="**Enter the Value for SELLING PRICE (Log Value)**/ Min:5.97503, Max:7.39036",format="%0.15f")
#         item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
#         item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
#         item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
#         delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
#         delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
#         delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

#     button= st.button(":violet[***PREDICT THE STATUS***]",use_container_width=True)

#     if button:
#         status= predict_status(country,item_type,application,width,product_ref,quantity_tons_log,
#                                customer_log,thickness_log,selling_price_log,item_date_day,
#                                item_date_month,item_date_year,delivery_date_day,delivery_date_month,
#                                delivery_date_year)
        
#         if status == 1:
#             st.write("## :green[**The Status is WON**]")
#         else:
#             st.write("## :red[**The Status is LOSE**]")

# if option == "PREDICT SELLING PRICE":

#     st.header("**PREDICT SELLING PRICE**")
#     st.write(" ")

#     col1,col2= st.columns(2)

#     with col1:
#         country= st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
#         status= st.number_input(label="**Enter the Value for STATUS**/ Min:0.0, Max:8.0")
#         item_type= st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
#         application= st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
#         width= st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
#         product_ref= st.number_input(label="**Enter the Value for PRODUCT_REF**/ Min:611728, Max:1722207579")
#         quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY_TONS (Log Value)**/ Min:-0.3223343801166147, Max:6.924734324081348",format="%0.15f")
#         customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910565821408, Max:17.230155364880137",format="%0.15f")
        
    
#     with col2:
#         thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.7147984280919266, Max:3.281543137578373",format="%0.15f")
#         item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
#         item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
#         item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
#         delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
#         delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
#         delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

#     button= st.button(":violet[***PREDICT THE SELLING PRICE***]",use_container_width=True)

#     if button:
#         price= predict_selling_price(country,status,item_type,application,width,product_ref,quantity_tons_log,
#                                customer_log,thickness_log,item_date_day,
#                                item_date_month,item_date_year,delivery_date_day,delivery_date_month,
#                                delivery_date_year)
        
        
#         st.write("## :green[**The Selling Price is :**]",price)




import streamlit as st
import pickle
import numpy as np
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings('ignore')

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
st.set_page_config(layout="wide")

st.title(":green[**INDUSTRIAL COPPER MODELING**]")

# Sidebar Menu
with st.sidebar:
    option = option_menu('Predict Price/Status', options=["PREDICT SELLING PRICE", "PREDICT STATUS"])

# Status Prediction Page
if option == "PREDICT STATUS":
    # st.header("PREDICT STATUS (Won / Lose)")
    st.markdown("## :blue[**PREDICT STATUS (Won / Lose)**]")


    col1, col2 = st.columns(2)
    
    with col1:
        country = st.number_input("Enter COUNTRY (25-113)", min_value=25.0, max_value=113.0)
        item_type = st.number_input("Enter ITEM TYPE (0-6)", min_value=0.0, max_value=6.0)
        application = st.number_input("Enter APPLICATION (2-87.5)", min_value=2.0, max_value=87.5)
        width = st.number_input("Enter WIDTH (700-1980)", min_value=700.0, max_value=1980.0)
        product_ref = st.number_input("Enter PRODUCT_REF (611728-1722207579)")
        quantity_tons_log = st.number_input("Enter QUANTITY_TONS (Log Value)")
        customer_log = st.number_input("Enter CUSTOMER (Log Value)")
        thickness_log = st.number_input("Enter THICKNESS (Log Value)")
    
    with col2:
        selling_price_log = st.number_input("Enter SELLING PRICE (Log Value)")
        item_date = [int(st.selectbox("ITEM DATE - Day", [str(i) for i in range(1, 32)])),
                     int(st.selectbox("ITEM DATE - Month", [str(i) for i in range(1, 13)])),
                     int(st.selectbox("ITEM DATE - Year", ["2020", "2021"]))]
        delivery_date = [int(st.selectbox("DELIVERY DATE - Day", [str(i) for i in range(1, 32)])),
                         int(st.selectbox("DELIVERY DATE - Month", [str(i) for i in range(1, 13)])),
                         int(st.selectbox("DELIVERY DATE - Year", ["2020", "2021", "2022"]))]
    
    if st.button("PREDICT THE STATUS", use_container_width=True):
        features = [country, item_type, application, width, product_ref, quantity_tons_log, customer_log,
                    thickness_log, selling_price_log] + item_date + delivery_date
        status = predict_status(features)
        st.subheader(f":red[**The Status is {status}**]" if status == "WON" else f"### :red[**The Status is {status}**]")

# Selling Price Prediction Page
if option == "PREDICT SELLING PRICE":
    # st.header("PREDICT SELLING PRICE")
    st.markdown("## :blue[**PREDICT SELLING PRICE**]")
    col1, col2 = st.columns(2)
    
    with col1:
        country = st.number_input("Enter COUNTRY (25-113)", min_value=25.0, max_value=113.0)
        status = st.number_input("Enter STATUS (0-8)", min_value=0.0, max_value=8.0)
        item_type = st.number_input("Enter ITEM TYPE (0-6)", min_value=0.0, max_value=6.0)
        application = st.number_input("Enter APPLICATION (2-87.5)", min_value=2.0, max_value=87.5)
        width = st.number_input("Enter WIDTH (700-1980)", min_value=700.0, max_value=1980.0)
        product_ref = st.number_input("Enter PRODUCT_REF (611728-1722207579)")
        quantity_tons_log = st.number_input("Enter QUANTITY_TONS (Log Value)")
        customer_log = st.number_input("Enter CUSTOMER (Log Value)")
    
    with col2:
        thickness_log = st.number_input("Enter THICKNESS (Log Value)")
        item_date = [int(st.selectbox("ITEM DATE - Day", [str(i) for i in range(1, 32)])),
                     int(st.selectbox("ITEM DATE - Month", [str(i) for i in range(1, 13)])),
                     int(st.selectbox("ITEM DATE - Year", ["2020", "2021"]))]
        delivery_date = [int(st.selectbox("DELIVERY DATE - Day", [str(i) for i in range(1, 32)])),
                         int(st.selectbox("DELIVERY DATE - Month", [str(i) for i in range(1, 13)])),
                         int(st.selectbox("DELIVERY DATE - Year", ["2020", "2021", "2022"]))]
    
    if st.button("PREDICT THE SELLING PRICE", use_container_width=True):
        features = [country, status, item_type, application, width, product_ref, quantity_tons_log,
                    customer_log, thickness_log] + item_date + delivery_date
        price = predict_selling_price(features)
        st.subheader(f":green[**The Selling Price is: {price:.2f}**]")
