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
import tkinter as TK

with open('src/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
#st.set_page_config(page_title="App", page_icon=":seedling:",layout="wide")



# MULTIAPP
app = MultiApp()

#load assets


# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data", data.app)
app.add_app("Profile", model.app)
# The main app
app.run()



