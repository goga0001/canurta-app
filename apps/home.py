from cProfile import label
from curses import keyname
from email.mime import image
from tarfile import PAX_FIELDS
from turtle import width
import requests
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
from matplotlib import pyplot as plt
import plost
import seaborn as sns
from streamlit_option_menu import option_menu
from multiapp import MultiApp
from apps import home, data, model
from bokeh.models.widgets import Div

#ICON
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Page setting

with open('src/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
 
# Data
df= pd.read_csv('https://raw.githubusercontent.com/goga0001/canurta/main/Untitled%20spreadsheet%20-%20Sheet1.csv')

#load assets
def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")
# ---- HEADER SECTION ----
#heading
def app():
    
    

    c1, c2 = st.columns((4,1))
    with c1:
       st.subheader("Welcome back")
       st.title("Dashboard")
       st.header("This is a web app to explore your health data")
    
       with c2:
        st.button('Sign In')

    space(2)
    a1, a2 = st.columns((5,1.5))
    with a1:
     from PIL import Image
     image = Image.open('images/canurta1.png')
     st.image(image, width=300)

    with a2:
        from PIL import Image
        image = Image.open('images/canurta.png')
        st.image(image, width=350)


    if  st.button("Get your product here"): 
             js = "window.open('https://www.canurta.com/')"
             html = '<img src onerror="{}">'.format(js)
             div = Div(text=html)
             st.bokeh_chart(div)
    space(1)
    from PIL import Image
    a1, a2, a3, a4= st.columns(4)
    a1.metric("Daily Dose: ", "2 pills")
    a2.metric("Avg Inflammation Score","20%")
    a3.metric("Avg Pain Score", "8%")
    a4.metric("Avg mood score", "11%")