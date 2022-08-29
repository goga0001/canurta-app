from cProfile import label
from curses import keyname
from email.mime import image
from tarfile import PAX_FIELDS
from turtle import color, width
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
from bokeh.models.widgets import Div
from apps import home, data, model
import json
import json
#STYLE
hide_menu= """
<style>
#MainMenu{
     visiibity:hidden;
}
<style>
"""
side_bar="""
<style>
div.st-bz.st-cd.st-ce.st-ae.st-af.st-ag.st-ah.st-ai.st-aj{
     font-family: Helvetica, Arial, sans-serif;
     list-style: none
}
<style>
"""
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


#load assets=add empty space
def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")
# ---- HEADER SECTION ----
#heading
def app():
    
    
    c1, c2 = st.columns((4,1))
    with c1:
       
       st.title("Dashboard")
       
       
    
       with c2:
        space(1)

    


    space(1)
    space(1)
    space(1)
    space(1)
    from PIL import Image
    a1, a2, a3, a4= st.columns(4)
    a1.metric("Dose Recomendation: ", "2 pills")
    a2.metric("Avg Inflammation \n Score","20%")
    a3.metric("Avg Pain Score", "8%")
    a4.metric("Avg mood score", "11%")

    space(1)
    st.subheader("Product Recomendations")
    space(1)
    space(1)
    b1, b2= st.columns(2)
    with b1:
       st.image("images/canurta1.png", use_column_width=True)
       button=st.button("Get your product here")
       button
      
    with b2:
       st.image("images/product.png", use_column_width=True)
       button