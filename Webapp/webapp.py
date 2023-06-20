import streamlit as st
import requests
import pandas as pd
import numpy as np
from functions import organize_data_collected

st.title("Rome House Prices Prediction Project")
# st.header("Calculate the estimated price of house in Rome using an XGBoost machine learning model")
# st.markdown("The model was trained over 15.000 house data collected through web-scraping on a Italian Real Estate "
#             "Website")
st.subheader("Estimate your house price now!")
st.markdown("Press Enter in every required field to load the data")

address = st.text_input(label="Type house address", value="Roma")
st.write('Address selected is ', address)

if 'coordinates' not in st.session_state:
    lat = 41.8933203
    lon = 12.4829321
    df = pd.DataFrame(np.array((lat, lon)).reshape(1, 2), columns=['lat', 'lon'])
    st.session_state.coordinates = [df, lat, lon]

coordinates = st.button("Search Address")
if coordinates:
    base_url = "http://nominatim.openstreetmap.org/search?q=%s&format=json&polygon=1&addressdetails=1"
    adress = address.strip().replace(" ", "+")
    url = base_url % adress
    data_json = requests.get(url, timeout=2.50)
    lat = float(data_json.json()[0]['lat'])
    lon = float(data_json.json()[0]['lon'])
    df = pd.DataFrame(np.array((lat, lon)).reshape(1, 2), columns=['lat', 'lon'])
    st.session_state.coordinates = [df, lat, lon]

st.write('Latitude:', st.session_state.coordinates[1])
st.write('Longitude:', st.session_state.coordinates[2])
st.map(st.session_state.coordinates[0], zoom=14)

year = st.number_input(label="Estimated year of construction, if you don't know leave it to 0",
                       min_value=0,
                       max_value=2030,
                       value=0,
                       step=1)
st.write('Selected year is ', year)

surface = st.number_input(label="Surface area in square meters, m^2",
                          min_value=0.,
                          max_value=10000.,
                          value=0.,
                          step=0.1)
st.write('Selected surface is ', surface)

floor = st.selectbox(label="Select the floor level",
                     options=["Ground floor - Piano terra", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                              "Underground floor - Sottosuolo", "Mezzanine floor - Piano Rialzato", "Other"])
st.write('Selected floor is ', floor)

new = st.radio(label="Is the house new?", options=["Yes", "No"], index=1)

luxury = st.radio(label="Can be considered a luxury house?", options=["Yes", "No"], index=1)

features = st.multiselect('Select all the features available in the house:',
                          ['Balcony', 'Terrace', 'Cellar', 'Swimming-pool', 'Garden'])

rooms = st.selectbox(label="Select the number of rooms:",
                     options=["1", "2", "3", "4", "5", "More than 5"])
st.write('Selected number of rooms ', rooms)

bathrooms = st.selectbox(label="Select the number of bathrooms:",
                         options=["1", "2", "3", "More than 3"])
st.write('Selected number of bathrooms ', bathrooms)

garage = st.selectbox(label="Select the number of garages:",
                      options=["0", "1", "2", "3", "4", "Other"])
st.write('Selected number of garages ', garage)

typology = st.selectbox(label="Typology of house:",
                        options=["Flat - Appartamento", "House - Casa indipendente", "Loft", "Penthouse - Attico",
                                 "Country house - Casale", "Villa", "Other typology"])
st.write('Selected typology ', typology)

condition = st.selectbox(label="Structural condition of the house:",
                         options=["Good - Buono/Abitabile", "To be renovated - Da ristrutturare",
                                  "New/Under construction - Nuovo/In costruzione",
                                  "Excellent/Renovated - Ottimo/Ristrutturato", "Other conditions"])
st.write('Selected condition ', condition)

test = organize_data_collected(st.session_state.coordinates[1], st.session_state.coordinates[2], year, surface, floor,
                               new, luxury, features, rooms, bathrooms, garage, typology, condition)
st.write(test)
