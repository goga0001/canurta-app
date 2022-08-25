"""Frameworks for running multiple Streamlit applications as a single app.
"""
from __future__ import with_statement
from turtle import width
import streamlit as st
from streamlit_lottie import st_lottie
import requests 
import json


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
     return json.load(f)
lottie_coding = load_lottiefile("images/lottie.json")
#######STYLE CSS#######
hide_menu= """
<style>
#MainMenu {
     visibility: hidden;
}
#div.css-qri22k.egzxvld4 {
     visibility: hidden;
}
<style>
"""
side_bar="""
<style>
#stHorizontalBlock{
     background-color: #023334;
}
<style>
"""
 
class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """
    st.set_page_config(layout="wide")
    def __init__(self):
        self.apps = []
        
        

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        
        self.apps.append({
            "title": title,
            "function": func
        })
        #################
    

       


    def run(self):
       

        st.sidebar.image("images/canurta_logo.png", use_column_width=True, width=100)
        st.markdown(hide_menu, unsafe_allow_html= True)
        st.markdown(side_bar, unsafe_allow_html= True)


        with st.sidebar:
            
             st.image("images/background.png", width=50, )
             with st.form(key="daily_tracker"):
                mood_slider = st.slider("Daily Mood Tracker", min_value=0, max_value=10, value=5, step=1)
                pain_slider = st.slider("Daily Pain Tracker", min_value=0, max_value=10, value=5, step=1)
                submit = st.form_submit_button(label="Submit")


        app = st.sidebar.radio(
        #app = st.selectbox(
            '',
            
            self.apps,
            format_func=lambda app: app['title'],
            )
        
        

        app['function']()

    



        
        