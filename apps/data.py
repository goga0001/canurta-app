import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def app():
    def app():
     st.title('Data')
    lang = pd.read_excel('Book1.xlsx')

    with st.expander(" Choose your filters"):
      list= lang.columns[1:8].tolist()
      choice= st.multiselect("Pick your biomarker", list, list[:3])
      start = st.date_input("Start", value=pd.to_datetime("2022-01-01"))
      end = st.date_input("End", value=pd.to_datetime("2022-03-31"))

    data=lang[choice]
    st.text("A close look into the data")
    st.line_chart(data)
    
    if st.button("Share results with your doctor"):
        js = "window.open('https://www.canurta.com/')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
    
   

