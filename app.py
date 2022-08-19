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



###################### Gurkamal #####################################
#####################################################################

###################### Changing dataframe datatypes #################
def import_json(json_file):
    df = pd.read_json(json_file)
    df =df.T
    df.iloc[:, 1:8] = df.iloc[:, 1:8].astype('float')
    df.iloc[:, 8:10] = df.iloc[:, 8:10].astype('int')
    df['skin_temp'] = df['skin_temp'].astype('float')
    df.iloc[:, 12:15] = df.iloc[:, 12:15].astype('int')
    df['date'] = df['date'].astype('datetime64')

    return df

# import json as df
df = import_json('canurta_dashboard.json')

#subset data into biomarkers with similar ranges
dfx = df.iloc[:,0:8]
dfx_1 = dfx[df['user_id'] == 227722]
df_b1 = df[df['user_id'] == 227722].iloc[:,[0,1,5,7]]
df_b2 = df[df['user_id'] == 227722].iloc[:,[0,4,6]]

import plotly.express as px
fig = px.line(dfx_1, x='date', y=df.columns[1:8])

st.plotly_chart(fig, use_container_width=True)



