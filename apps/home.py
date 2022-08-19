from cProfile import label
from curses import keyname
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
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_l13zwx3i.json")
# ---- HEADER SECTION ----
#heading
def app():
    c1, c2, c3 = st.columns((5,2,1))
    with c1:
       st.subheader("Welcome back")
       st.title("Dashboard")
       st.header("This is a web app to explore your health data")

       with c2:
        st_lottie(lottie_coding, height=300, key="coding")
       with c3:
        st.button('Sign In')

    st.text("Get your product here:")
    st.write("[Order>](https://www.canurta.com/)")
    from PIL import Image
    a1, a2, a3, a4, a5= st.columns(5)
    a1.image(Image.open('images/image.png'), width=150)
    a2.metric("Daily Dose: ", "2 pills")
    a3.metric("Avg Inflammation Score","20%")
    a4.metric("Avg Pain Score", "8%")
    a5.metric("Avg mood score", "11%")