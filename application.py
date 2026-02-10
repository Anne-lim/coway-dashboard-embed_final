import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

current_year = datetime.now().year

st.set_page_config(
     page_title="Coway Dashboard",
     page_icon="AA-logo.png",
     layout="centered",
     initial_sidebar_state="expanded")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

components.html("""
    <script>
    const hideInterval = setInterval(() => {
        const avatar = document.querySelector('img[alt="App Creator Avatar"]');
        const profileContainer = avatar?.closest('div');
        if (profileContainer) {
            profileContainer.style.display = 'none';
            clearInterval(hideInterval);
        }
    }, 500);
    </script>
""", height=0)

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.sidebar.text_input("Username", on_change=password_entered, key="username")
        st.sidebar.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.sidebar.text_input("Username", on_change=password_entered, key="username")
        st.sidebar.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.sidebar.warning("Incorrect password or username")
        return False
    else:
        # Password correct.
        return True

if check_password():
    # check_access()
    st.markdown('# Coway Data Portal')
    st.markdown(f'Ampersand Advisory, {current_year}.')
    tab1, tab2 = st.tabs(["Adex Dashboard", "Sales Map"])
    with tab1: 
        # st.markdown('Adex Dashboard.')
        # components.iframe('https://app.powerbi.com/view?r=eyJrIjoiMmQ0ZDkwZjYtODNjNS00MTU2LWJjMjctMzI3ZTY3NzVjNmM5IiwidCI6ImIxNjBhNWMzLTA2MTUtNDA3ZC1hNGNjLTc4MDRlZDc3Mzk4OSIsImMiOjEwfQ%3D%3D&pageName=ReportSectionb1c91a4c1333c6930ae6', 
        components.iframe('https://app.powerbi.com/view?r=eyJrIjoiNDQ3OTRlNmItZGM4Zi00Nzc3LTkwNGItMjFlNzZiOTA4ZjkyIiwidCI6ImIxNjBhNWMzLTA2MTUtNDA3ZC1hNGNjLTc4MDRlZDc3Mzk4OSIsImMiOjEwfQ%3D%3D', 
                    scrolling=False, height=600, width=800)

#     with tab2: 
#         # st.markdown('Maps sales into different areas.')
#         components.iframe('https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/gs5y0zdg3yve2np/keplergl_6d5a97p.json', 
#             scrolling=False, height=600, width=800)
