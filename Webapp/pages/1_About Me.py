import streamlit as st
from PIL import Image

image = Image.open('foto.jpeg')
st.set_page_config(
    page_title="Raffo's WebApp",
    page_icon="🤖"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(image, width=300)

with col3:
    st.write(' ')
st.header("Raffaello Cesetti")
st.markdown("Hi! My name is Raffaello Cesetti and I am a CESMA Master's student specializing in Data Science. "
            "During an internship experience in Lisbon, I discovered my passion for Data Science, working with Python "
            "to help the business migrate from data analysis on Excel to Python.")
st.markdown("During that time, I met some guys "
            "studying Data Science and have had the goal of becoming a Data Scientist ever since. I am fascinated by "
            "Python and its endless libraries, which have become my tool of choice for Data Science.")
st.markdown("I appreciate the "
            "flexibility, simplicity,and versatility of Python, which allow me to work on every phase of a Data Science"
            " project. I can collect data through web scraping and get as far as putting machine learning models into "
            "production, such as this web-app on Streamlit.")
st.markdown("I decided to develop this project as a personal exercise "
            "to improve my skills in all phases of the data process. In the section dedicated to the model, "
            "I explain in detail the work done.")
st.markdown("I look forward to tackling real Data Science projects, and I hope this "
            "small project will demonstrate my dedication and willingness to challenge myself. Thank you for reading "
            "this introduction about me!")

st.markdown("**LinkedIn**: https://www.linkedin.com/in/raffaello-cesetti/")
st.markdown("**GitHub**:   https://github.com/Raffozor/")
