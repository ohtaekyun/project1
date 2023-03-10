import streamlit as st
from streamlit_option_menu import option_menu

st.title('TITLE')

selected3 = option_menu(None, ["ð Home", " ðì ìì¸ ê²ì",  "ðì ì¸vsìì¸?", 'ð¬ê±´ìì¬í­'], 
    
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#47C83E"},
    }
)