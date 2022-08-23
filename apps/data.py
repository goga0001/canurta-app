import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import json
import json
import matplotlib.pyplot as plt
from apps import home, data, model


def app():
    st.title('Data')
    lang = pd.read_excel('Book1.xlsx')

  
    list= lang.columns[1:8].tolist()
    choice= list
    groupby_column2 = st.multiselect(
        'What would you like to analyse?',
        ('trail', 'crp', 'il6', "tgfb",	"tgfa",	"il8","ip10")
    )
    data=lang[choice]
    st.text("A close look into the data")
     

    fig2 = px.line(
        data,
        x=lang['date'],
        y=groupby_column2)
    fig2.update_xaxes(title_text='Date')

    st.plotly_chart(fig2,use_container_width=True)

   #####SECOND GRAPH#######         FINISHED
    st.text("A close look into the data")
    list= lang.columns[8:15].tolist()
    choice1= list
    data1=lang[choice1]
    groupby_column = st.selectbox(
        'What would you like to analyse?',
        ("rhr","calories","skin_temp", "sleep")
    )

    fig1 = px.bar(
        data1,
        x=lang['date'],
        y=groupby_column,
        color_continuous_scale=['red', 'yellow', 'green'],
        template='plotly_white',
        title=f'<b>Physiological Analysis by {groupby_column}</b>'
        )
    fig1.update_xaxes(title_text='Date')
    st.plotly_chart(fig1,use_container_width=True)




    ############BUTTON#########      FINISHED
    if st.button("Share results with your doctor"):
        js = "window.open('https://www.canurta.com/')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)