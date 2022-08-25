import streamlit as st
import sqlite3
conn = sqlite3.connect("personal_data.db", check_same_thread=False)
cur = conn.cursor()
from streamlit_option_menu import option_menu #used to make navigation bar


def app():
    #st.title('My Profile')
    #st.write("profile (where the user can input to capture pain, mood")
    #st.write("share data to doctor using the share symbol (get the doctors info/email), maybe use fullscript as link to connect to portal)")   
    
    st.title("My Profile :clipboard:")

    #with user_input: #mood and pain user input 
    #    mood_slider = st.slider("Daily Mood Tracker", min_value=0, max_value=10, value=5, step=1)
    #    pain_slider = st.slider("Daily Pain Tracker", min_value=0, max_value=10, value=5, step=1)

    selected = option_menu(
        menu_title=None,
        options=["Personal Info", "Share Results", "Subsctiption Details"],
        icons=["book","share","file-earmark-medical"],
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "20px"}, 
            "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )
    
    if selected == "personal_info":
        st.subheader("Personal Info")
        def form():
            with st.form(key="Information Form"):
                name = st.text_input("Full Name: ")
                age = st.text_input("Age: ")
                height = st.text_input("Height: ")
                weight = st.text_input("Weight: ")
                submission = st.form_submit_button(label="Submit")
                if submission == True:
                    addData(name,age,height,weight)
    
    
        def addData(a,b,c,d):
            cur.execute("""CREATE TABLE IF NOT EXISTS personal_form(NAME TEXT(50), AGE TEXT(50), HEIGHT TEXT(50), WEIGHT TEXT(50));""")
            cur.execute("INSERT INTO personal_form VALUES (?,?,?,?)", (a,b,c,d))
            conn.commit()
            conn.close()
            st.success("Successfully submitted!")
        form()
            
            
        col1, col2, col3 = st.columns(3) #putting an image in centre
        col2.image("profile_page_pic2.png") 


    if selected == "share_results": 
        st.subheader("My Physician")
        def physician_form():
            with st.form(key="Physician Form"):
                doctor_name = st.text_input("Doctor's Name: ")
                doctor_email = st.text_input("Email: ")
                submission = st.form_submit_button(label="Invite")
                if submission == True:
                   st.success("Successfully submitted!") 
        physician_form()
        #st.write("[Connect with my doctor >](https://mail.yahoo.com/)")
        st.markdown(
            """<a style='display: block; text-align: center;' href="https://fullscript.com/">Connect to Fullscript</a>
            """, 
            unsafe_allow_html=True
            )
        
        col1, col2, col3 = st.columns(3) #putting an image in centre
        col2.image("profile_page_pic3.png")
        
    if selected == "Subsctiption Details":
        st.markdown(
            """<a style='display: block; text-align: center;' href="https://www.canurta.com/">Subscription Details</a>
            """, 
            unsafe_allow_html=True
            )

        col1, col2, col3 = st.columns(3) #putting an image in centre
        col2.image("profile_page_pic4.png")

    #these next few line hide the hamburger bar at top and the "run with stremlit" text at bottom of page
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)


        
   
