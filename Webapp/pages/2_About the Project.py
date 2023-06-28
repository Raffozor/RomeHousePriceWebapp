import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="The Project",
    page_icon="🏗️"
)
st.header("The project explained")
st.markdown("The objective of this project was to apply the knowledge acquired during the Master CESMA by developing "
            "a proof of concept that demonstrates the practical application of our learning.")
st.markdown("To begin the project, I created a web crawler and scraper using Selenium and Beautiful Soup to extract "
            "information on houses for sale from an Italian Real Estate website. To sped up the process, I utilized "
            "two PCs in parallel and updated a cloud-based MySQL database on AWS.")
st.markdown("During the initial phase, a total of 15.522 observations were collected. After performing data cleaning "
            "and eliminating observations with errors, the resulting dataset comprised 14.874 observations. "
            "Subsequently, the dataset was divided into an 80% training set and a 20% test set.")
st.markdown("For categorical variables with numerous categories, mean encoding with standard deviation was employed, "
            "while one-hot encoding was used for variables with a low number of categories. The XGBoost model was "
            "selected for this proof of concept.")
st.markdown("The model underwent fine-tuning using a validation set of 20%. After the fine-tuning process, the model "
            "achieved a mean absolute percentage error of approximately 15% on the test set.")
st.markdown(
    'The final step of this project involved putting the model into "production" by integrating it into a Streamlit '
    'web application. This can allow users to estimate the price of a house based on the selected variables.')
house_coordinates = pd.read_csv('house_coordinates.csv')
st.map(house_coordinates, zoom=10)
st.markdown("Coordinates plot of all houses available")