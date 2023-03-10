# ν
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from search import run_search
from predict import run_predict
from suggestions import run_suggestions

st.title('π‘ λ΄ λ°© μ΄λ? π€·')
selected3 = option_menu(None, ["π  Home", "π μ μμΈ κ²μ",  "π μ μΈ μμΈ‘", 'π¬ κ±΄μμ¬ν­'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "1!important", "background-color": "#ede3d5"},
        "icon": {"color": "gray", "font-size": "15px"},
        "nav-link": {"font-size": "15px", "padding": "5px", "text-align": "left", "margin":"5px", "--hover-color": "#f0afa3"},
        "nav-link-selected": {"margin":"5px", "padding": "5px", "background-color": "#47C83E"},
    }
)

# ν ν­
if selected3 == "π  Home":
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    st.subheader('π¨οΈ μ€κ±°λ νν©')    
    cols = ['SGG_NM', 'BJDONG_NM']  
    data2 = data[['SGG_NM', 'BJDONG_NM', 'RENT_GBN', 'RENT_AREA', 'RENT_GTN', 'RENT_FEE', 'CNTRCT_DE', 'BLDG_NM']]
    data2.columns = ['μ§μ­κ΅¬', 'νμ λ', 'κ΅¬λΆ', 'λ©΄μ (m^2)', 'λ³΄μ¦κΈ', 'μμΈ', 'κ³μ½μΌ', 'λ¨μ§λͺ']
    data2.index = data2.index + 1
    st.write(data2.head(1000))
    (" ")
    (" ")
    (" ")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('π₯ μμΈ TOP10')        
        data_m = data[data['RENT_GBN']=='μμΈ']                
        cols = ['SGG_NM', 'BJDONG_NM']             
        data_addr = data_m[cols].value_counts().reset_index()
        data_addr.columns = ['μ§μ­κ΅¬', 'νμ λ', 'κ±°λλ']
        data_addr.index = data_addr.index+1        
        st.write(data_addr.head(10))

    with col2:
        st.subheader('π₯ μ μΈ TOP10')
        data_m = data[data['RENT_GBN']=='μ μΈ']
        cols = ['SGG_NM', 'BJDONG_NM']        
        # st.write(data_m[cols].value_counts().count())
        data_addr = data_m[cols].value_counts().reset_index()
        data_addr.columns = ['μ§μ­κ΅¬', 'νμ λ', 'κ±°λλ']
        data_addr.index = data_addr.index+1
        st.write(data_addr.head(10))


# μ μμΈ κ²μ ν­
elif selected3 == "π μ μμΈ κ²μ":
    run_search()
# μ μΈ μμΈ μμΈ‘ ν­
elif selected3 == "π μ μΈ μμΈ‘":
    run_predict()
# κ±΄μμ¬ν­ ν­
elif selected3 == "π¬ κ±΄μμ¬ν­":
    run_suggestions()
else:
    selected3 == "π  Home"