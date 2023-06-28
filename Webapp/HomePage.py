import streamlit as st
import requests
import pandas as pd
import numpy as np
from functions import organize_data_collected, scaling_values, price_prediction

st.set_page_config(
    page_title="Raffaello's WebApp",
    page_icon="🏙️"
)

st.title("Rome House Prices Prediction")
# st.header("Calculate the estimated price of house in Rome using an XGBoost machine learning model")
# st.markdown("The model was trained over 15.000 house data collected through web-scraping on a Italian Real Estate "
#             "Website")

st.sidebar.markdown("Press Enter in every required field to load the data")

address = st.sidebar.text_input(label="Type house address", value="Roma")

if 'coordinates' not in st.session_state:
    lat = 41.8933203
    lon = 12.4829321
    df = pd.DataFrame(np.array((lat, lon)).reshape(1, 2), columns=['lat', 'lon'])
    st.session_state.coordinates = [df, lat, lon]

coordinates = st.sidebar.button("Search Address")
if coordinates:
    base_url = "http://nominatim.openstreetmap.org/search?q=%s&format=json&polygon=1&addressdetails=1"
    adress = address.strip().replace(" ", "+")
    url = base_url % adress
    data_json = requests.get(url, timeout=2.50)
    lat = float(data_json.json()[0]['lat'])
    lon = float(data_json.json()[0]['lon'])
    df = pd.DataFrame(np.array((lat, lon)).reshape(1, 2), columns=['lat', 'lon'])
    st.session_state.coordinates = [df, lat, lon]

year = st.sidebar.number_input(label="Estimated year of construction, if you don't know leave it to 0",
                               min_value=0,
                               max_value=2030,
                               value=0,
                               step=1)

surface = st.sidebar.number_input(label="Surface area in square meters, m^2",
                                  min_value=0.,
                                  max_value=10000.,
                                  value=0.,
                                  step=0.1)

floor = st.sidebar.selectbox(label="Select the floor level",
                             options=["Ground floor - Piano terra", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                      "Underground floor - Sottosuolo", "Mezzanine floor - Piano Rialzato", "Other"])

new = st.sidebar.radio(label="Is the house new?", options=["Yes", "No"], index=1)

luxury = st.sidebar.radio(label="Can be considered a luxury house?", options=["Yes", "No"], index=1)

features = st.sidebar.multiselect('Select all the features available in the house:',
                                  ['Balcony', 'Terrace', 'Cellar', 'Swimming-pool', 'Garden'])

rooms = st.sidebar.selectbox(label="Select the number of rooms:",
                             options=["1", "2", "3", "4", "5", "More than 5"])

bathrooms = st.sidebar.selectbox(label="Select the number of bathrooms:",
                                 options=["1", "2", "3", "More than 3"])

garage = st.sidebar.selectbox(label="Select the number of garages:",
                              options=["0", "1", "2", "3", "4", "Other"])

typology = st.sidebar.selectbox(label="Typology of house:",
                                options=["Flat - Appartamento", "House - Casa indipendente", "Loft",
                                         "Penthouse - Attico",
                                         "Country house - Casale", "Villa", "Other typology"])

condition = st.sidebar.selectbox(label="Structural condition of the house:",
                                 options=["Good - Buono/Abitabile", "To be renovated - Da ristrutturare",
                                          "New/Under construction - Nuovo/In costruzione",
                                          "Excellent/Renovated - Ottimo/Ristrutturato", "Other conditions"])

data = organize_data_collected(st.session_state.coordinates[1], st.session_state.coordinates[2], year, surface, floor,
                               new, luxury, features, rooms, bathrooms, garage, typology, condition)
scaled_values = scaling_values(data)

calculate_price = st.button("Estimate Price")

if calculate_price:

    price = price_prediction(scaled_values)
    st.subheader(f"The estimated price is {price}")
else:
    st.subheader(f"Press the button to get an estimated price")

st.write(f'Address selected is {address} with Latitude: {"{:.2f}".format(st.session_state.coordinates[1])} and ' +
         f'Longitude: {"{:.2f}".format(st.session_state.coordinates[2])}')

st.sidebar.write('Latitude:', st.session_state.coordinates[1])
st.sidebar.write('Longitude:', st.session_state.coordinates[2])
st.map(st.session_state.coordinates[0], zoom=14)
# st.write(os.getcwd())
