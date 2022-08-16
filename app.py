import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
from matplotlib import pyplot as plt
import plost

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(layout="wide")

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
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_5njp3vgg.json")
# ---- HEADER SECTION ----
#heading
c1, c2, c3 = st.columns((5,2,1))
with c1:
   st.subheader("Welcome back")
   st.title("Dashboard")
st.write("Check Your Acitivity")
st.write("[Learn More >](https://www.canurta.com/)")
with c2:
     st_lottie(lottie_coding, height=300, key="coding")
with c3:
    st.button('Sign In')


    
 
 

# Row A
a1, a2, a3 = st.columns(3) 
a1.metric("Biomarker 1", "30 pg mL-1", "7%")
a2.metric("Biomarker 2","20 pg mL-1", "-5%")
a3.metric("Biomarker 3","11 pg mL-1", "2%")

st.text("")

# Row B
c1, c2 = st.columns((7,3))

with c1:
    st.markdown('### Mood Analysis')


 
with c2:
    st.markdown('### Bar chart')
    plost.donut_chart(
        data=stocks,
        theta='q2',
        color='company')


st.dataframe(df)
#sidebar
with st.sidebar:
    st.sidebar.header("Please Filter Here:")
    biomarkers = ("trail","crp","il6","tgfb","tgfa","il8","ip10")
    dropdown= st.multiselect("Pick your biomarker", biomarkers)
    start = st.date_input("Start", value=pd.to_datetime("2022-01-01"))
    end = st.date_input("End", value=pd.to_datetime("2022-03-31"))

if len(dropdown)>0:
    df= int(dropdown)(start, end) ["Adj Close"]
    st.line_chart(df)


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
