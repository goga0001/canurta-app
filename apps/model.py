#import streamlit as st


#def app():
#    st.title('Profile')
#    st.write("profile (where the user can input to capture pain, mood")
#    st.write("share data to doctor using the share symbol (get the doctors info/email), maybe use fullscript as link to connect to portal)")


############ Helia #################
####################################

import streamlit as st
from bokeh.models.widgets import Div

header = st.container()
user_input = st.container()
share_results = st.container()
def app():
  with header:
    st.title("My Profile")

  with user_input:
    mood_slider = st.slider("Daily Mood Tracker", min_value=0, max_value=10, value=5, step=1)
    pain_slider = st.slider("Daily Pain Tracker", min_value=0, max_value=10, value=5, step=1)

  with share_results: 
    st.subheader("Share My Results")
    text_col, image_col = st.columns(2)
    image_col.image("share_symbol.png")
    st.button("Send Report to My Doctor")

    if st.button("Connect to Fullscript"):
        js = "window.open('https://fullscript.com/')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

        
   
