from cProfile import label
from tarfile import PAX_FIELDS
import requests
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
from matplotlib import pyplot as plt
import plost
import sqlite3
import plotly.express as px
import time



# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="App", page_icon=":seedling:",layout="centered")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Page setting

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Data
df= pd.read_csv('https://raw.githubusercontent.com/goga0001/canurta/main/Untitled%20spreadsheet%20-%20Sheet1.csv')

    
#load assets
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_l13zwx3i.json")
# ---- HEADER SECTION ----
#heading
c1, c2, c3 = st.columns((5,2,1))
with c1:
   st.subheader("Welcome back")
   st.title("Dashboard")
st.text("This is a web app to explore your health data")
st.write("[Learn More >](https://www.canurta.com/)")
with c2:
     st_lottie(lottie_coding, height=300, key="coding")
with c3:
    st.button('Sign In')


    
 
 

# Row A
col1, col2, col3 = st.columns(3)
col1.metric("CRP","-2%")
col2.metric("IL-6","-8%")
col3.metric("TRF","+4%")

st.text("")

#sidebar 
lang = pd.read_excel('Book1.xlsx')

with st.sidebar:
    st.sidebar.header("Please Filter Here:")
    list= lang.columns[1:8].tolist()
    choice= st.multiselect("Pick your biomarker", list)
    start = st.date_input("Start", value=pd.to_datetime("2022-01-01"))
    end = st.date_input("End", value=pd.to_datetime("2022-03-31"))


data=lang[choice]
st.text("A close look into the data")
st.line_chart(data)

#Mood feedback

with st.form("my_form"):
    st.write("How is your mood")
    slider_val = st.slider("Form slider", 0, 7, 10)
     # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val  )
st.write("Outside the form")





###################### Gurkamal #####################################
#####################################################################

###################### Changing dataframe datatypes #################

import seaborn as sns

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
df_b1 = df[df['user_id'] == 227722].iloc[:,[0,1,5,7]]
df_b2 = df[df['user_id'] == 227722].iloc[:,[0,4,6]]

sns.set_style("darkgrid")
sns.lineplot(data = df_b1)

sns.set_style("darkgrid")
sns.lineplot(data = df_b2)

st.write(df.head(5))



############################# Helia ######################################
##########################################################################

#practice file with sample plot for RHR using json data
import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()

with header:
    #st.title("Welcome back!")


with dataset:
    canurta_df = pd.read_json('canurta_dashboard.json')
    canurta_df_transposed = canurta_df.T
    #st.write(canurta_df_transposed.head())
    rhr = pd.DataFrame(canurta_df_transposed["rhr"].value_counts())
    st.bar_chart(rhr)

