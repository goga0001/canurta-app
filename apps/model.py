import streamlit as st
from bokeh.models.widgets import Div

def app():
    #st.title('My Profile')
    #st.write("profile (where the user can input to capture pain, mood")
    #st.write("share data to doctor using the share symbol (get the doctors info/email), maybe use fullscript as link to connect to portal)")   
    
    header = st.container()
    user_input = st.container()
    personal_info = st.container()
    share_results = st.container()

    with header:
        st.title("My Profile")

    with user_input: #mood and pain user input 
        mood_slider = st.slider("Daily Mood Tracker", min_value=0, max_value=10, value=5, step=1)
        pain_slider = st.slider("Daily Pain Tracker", min_value=0, max_value=10, value=5, step=1)

    with personal_info:
        st.subheader("Personal Info")
        st.text("Name:")
        st.text("Age:")
        st.text("Height:")
        st.text("Weight:")
        if st.button("Subscription Details"): #creating a button with a hyperlink
            js = "window.open('https://www.canurta.com/')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div) 


    with share_results: 
        st.subheader("Share My Results")
        st.button("Send Report to My Doctor")

        if st.button("Connect to Fullscript"): #creating a button with a hyperlink
            js = "window.open('https://fullscript.com/')"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

        text_col, image_col = st.columns(2)
        image_col.image("images/share_symbol.png") #putting an image in almost centre of page



        
   
