import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
from matplotlib import pyplot as plt
import plost

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
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')
    
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
    list= lang.columns.tolist()
    choice= st.multiselect("Pick your biomarker", list)
    start = st.date_input("Start", value=pd.to_datetime("2022-01-01"))
    end = st.date_input("End", value=pd.to_datetime("2022-03-31"))


data=lang[choice]
st.text("A close look into the data")
st.line_chart(data)

#Calories
canurta_df = pd.read_json('canurta_dashboard.json')
canurta_df_transposed = canurta_df.T
st.text("Calories tracker")
calories = pd.DataFrame(canurta_df_transposed["calories"].value_counts())
st.bar_chart(calories)

###################### Gurkamal #####################################
#####################################################################

###################### Changing dataframe datatypes #################

canurta_df = pd.read_json('canurta_dashboard.json')
canurta_df = canurta_df.T
#canurta_df.index = canurta_df['date']
#canurta_df = canurta_df.drop(['date'], axis=1)
canurta_df.iloc[:, 1:8] = canurta_df.iloc[:, 1:8].astype('float')
canurta_df.iloc[:, 8:10] = canurta_df.iloc[:, 8:10].astype('int')
canurta_df['skin_temp'] = canurta_df['skin_temp'].astype('float')
canurta_df.iloc[:, 12:15] = canurta_df.iloc[:, 12:15].astype('int')
canurta_df['date'] = canurta_df['date'].astype('datetime64')

st.write(canurta_df.head(5))



############################# Helia ######################################
##########################################################################

#practice file with sample plot for RHR using json data
import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()

with header:
    st.title("Welcome back!")


with dataset:
    canurta_df = pd.read_json('canurta_dashboard.json')
    canurta_df_transposed = canurta_df.T
    st.write(canurta_df_transposed.head())
    rhr = pd.DataFrame(canurta_df_transposed["rhr"].value_counts())
    st.bar_chart(rhr)

####Background Image####
st.markdown(
   f”””
   <style>
   p {
   background-image: url(‘img_file.jpg’);
   }
   </style>
   ”””,
   unsafe_allow_html=True)
