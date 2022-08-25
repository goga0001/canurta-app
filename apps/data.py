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
    df_biomarkers = df[df['user_id'] == 227722].iloc[:,0:8]

#subset data into biomarkers with similar ranges
# dfx = df[df['user_id'] == 227722].iloc[:,0:8]
# df_b1 = df[df['user_id'] == 227722].iloc[:,[0,1,5,7]]
# df_b2 = df[df['user_id'] == 227722].iloc[:,[0,4,6]]

#st.write(df.head(5))

  
    marker_list = df_biomarkers.columns[1:8].tolist()
    choice = marker_list
    groupby_column2 = st.multiselect(
        'What would you like to analyse?',
        ('trail', 'crp', 'il6', "tgfb",	"tgfa",	"il8","ip10")
    )
    data=df_biomarkers[choice]
    st.text("A close look into the data")
     

    fig2 = px.line(
        data,
        x=df_biomarkers['date'],
        y=groupby_column2)
    fig2.update_xaxes(title_text='Date')

    st.plotly_chart(fig2,use_container_width=True)

   #####SECOND GRAPH#######         FINISHED
    lang = pd.read_excel('Book1.xlsx')
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






        ############HEATMAP########     
    
