from cProfile import label
from tarfile import PAX_FIELDS
import requests
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
from matplotlib import pyplot as plt
import plost
import seaborn as sns
from streamlit_option_menu import option_menu


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="App", page_icon=":seedling:",layout="wide")
###Navigation bar

EXAMPLE_NO = 1


def streamlit_menu(example=1):
     

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Results", "Profile"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

selected = streamlit_menu(example=2)

if selected == "Home":
    st.text("")
if selected == "Results":
    st.text("")
if selected == "Profile":
    st.text("")


#ICON
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
st.write("[Order>](https://www.canurta.com/)")
with c2:
     st_lottie(lottie_coding, height=300, key="coding")
with c3:
    st.button('Sign In')

####Product

st.text("Get your product")
from PIL import Image
image = Image.open('https://static.wixstatic.com/media/a1caab_e2a7ef47f7bc4a3a8fdd7a9d40399f4a~mv2.png/v1/fill/w_1270,h_1178,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/a1caab_e2a7ef47f7bc4a3a8fdd7a9d40399f4a~mv2.png')

st.image(image, caption='Product')    
 
 

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



