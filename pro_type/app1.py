import streamlit as st
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import numpy as np
from streamlit_option_menu import option_menu


def main():

    st.title('ìì¸ ë³¼ë?')
    (" ")
    (" ")
    (" ")

    selected = option_menu(None, ["ð Home", " ðì ìì¸ ê²ì",  "ðì ì¸vsìì¸?", 'ð¬ê±´ìì¬í­'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#ebb0b0"},
    })   
    
    submenu = st.sidebar.title('ê°í¸ ê²ì')
    submenu_lists1 = ["ìë±í¬êµ¬", 'ê´ìêµ¬', 'êµ¬êµ¬êµ¬']
    submenu_lists2 = ["ìë±í¬ 1ë", 'ìë±í¬ 2ë', 'ìë±í¬ 3ë']
    submenu_lists3 = ["30ë¯¸ë§", '30ì´ì 40ë¯¸ë§', '40ì´ì 50ë¯¸ë§']
    submenu_lists4 = ["500ë¯¸ë§", '500ì´ì 2000ì´í', '2000ì´ì 5000ë¯¸ë§']
    submenu_lists5 = ["ìíí¸", 'ì¤í¼ì¤í', 'ë¹ë¼']

    submenu = st.sidebar.selectbox('ì§ì­', submenu_lists1)
    submenu = st.sidebar.selectbox('ë/ì/ë©´', submenu_lists2)
    submenu = st.sidebar.selectbox('ìì¸', submenu_lists3)
    submenu = st.sidebar.selectbox('ë³´ì¦ê¸', submenu_lists4)
    submenu = st.sidebar.selectbox('ê±´ë¬¼ íì', submenu_lists5)
    submenu = st.sidebar.button('ê²ì', type = 'primary')

    if (selected=='ðì ìì¸ ê²ì'):
        pass


    elif (selected=='ð Home'):        
        data = pd.read_csv('bds_data.csv', encoding='cp949')
        st.write(data.head())


    elif (selected=='ð¬ê±´ìì¬í­'):
        title_input = st.text_input('ì ëª©')
        st.title(title_input)
        msg_input = st.text_area('ë´ì©', height=100)
        st.write(msg_input)
        password_input = st.text_input('ë¹ë°ë²í¸')
        st.title(password_input)
        st.button('ë±ë¡')


        


    else:
        pass

    
       
    
    


if __name__ == "__main__":
    main()