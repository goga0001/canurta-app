import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.title('Data')
    with st.form("my_form"):
      st.write("How is your mood")
      slider_val = st.slider("Form slider", 0, 7, 10)
     # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val  )
    st.write("Outside the form")


