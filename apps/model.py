import streamlit as st
#from bokeh.models.widgets import Div
import sqlite3
conn = sqlite3.connect("personal_data.db", check_same_thread=False)
cur = conn.cursor()
st.set_page_config(page_title="My Profile", page_icon=":memo:", layout="wide")

def app():
    #st.title('My Profile')
    #st.write("profile (where the user can input to capture pain, mood")
    #st.write("share data to doctor using the share symbol (get the doctors info/email), maybe use fullscript as link to connect to portal)")   
    
    header = st.container() 
    user_input = st.container()
    personal_info = st.container()
    share_results = st.container()

    with header:
        st.title("My Profile :star2:")

    with user_input: #mood and pain user input 
        mood_slider = st.slider("Daily Mood Tracker", min_value=0, max_value=10, value=5, step=1)
        pain_slider = st.slider("Daily Pain Tracker", min_value=0, max_value=10, value=5, step=1)

    with personal_info:
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
            
            
        #if st.button("Subscription Details"): #creating a button with a hyperlink
        #    js = "window.open('https://www.canurta.com/')"
        #    html = '<img src onerror="{}">'.format(js)
        #    div = Div(text=html)
        #    st.bokeh_chart(div) 
        st.write("[Subscription Details >](https://www.canurta.com/)")


    with share_results: 
        st.subheader("Share My Results")
        #st.button("Send Report to My Doctor")

        st.write("[Send report to my doctor >](https://mail.yahoo.com/)")
        st.write("[Connect to Fullscript >](https://fullscript.com/)")
        
        #if st.button("Connect to Fullscript"): #creating a button with a hyperlink
        #    js = "window.open('https://fullscript.com/')"
        #    html = '<img src onerror="{}">'.format(js)
        #    div = Div(text=html)
        #    st.bokeh_chart(div)

        text_col, image_col = st.columns(2)
        image_col.image("images/share_symbol.png") #putting an image in almost centre of page



        
   
