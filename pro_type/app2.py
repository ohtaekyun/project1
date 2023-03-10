import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

# import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap'); 

# html, body, [class*="css"] {
#     font-family: 'Roboto', sans-serif; 
#     font-size: 10;
#     font-weight: 500;
#     color: #091747;
# }

# with open( "app\style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.title('ë°©ë°©ì½ì½')

from search import run_search
from predict import run_predict
from suggestions import run_suggestions

selected3 = option_menu(None, ["ð Home", "ðì ìì¸ ê²ì",  "ðì ì¸ ìì¸ ìì¸¡", 'ð¬ê±´ìì¬í­'], 
    # icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "gray", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#47C83E"},
    }
)

# í í­
if selected3 == "ð Home":
    st.subheader('ê°ì¥ HOTí ëë¤ë ì´ë? (ì ì¸+ìì¸ ê¸°ì¤)')
    data = pd.read_csv('data/bds_data.csv', encoding='cp949')
    # st.write(data.head())
    # st.dataframe(data, 200, 100)
    # st.write(data.columns)
    # st.write(data.shape)
    # df_sample = data.loc[0:10, 'SGG_CD', 'FLR_NO', 'CNTRCT_DE']
    # st.dataframe(df_sample)
    # st.write(df_sample['ì§ì­êµ¬'].unique())
    # df_sample_value.columns = ['a']
    # list1 = df_sample['íì ë'].tolist()
    # st.write(df_sample)
    goo = data[['SGG_NM']]
    st.write(goo)
    st.write(goo.type)
    a = data[['SGG_NM', 'BJDONG_NM']]
    st.write(a)

    # b = data.groupby('SGG_NM').BJDONG_NM.value_counts(normalize=True)
    # st.write(b)



    cols = ['SGG_NM', 'BJDONG_NM']
    a['êµ¬/ë'] = a[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    st.write(a)
    st.write(a['êµ¬/ë'].value_counts())
    st.write(a['êµ¬/ë'].head(10))
    a['êµ¬/ë'].value_counts()
    st.write(a['êµ¬/ë'].value_counts())
    a['ê±°ëíì'] = a['êµ¬/ë'].value_counts()
    st.write(a['ê±°ëíì'])
    st.write(a['êµ¬/ë', 'ê±°ëíì'])














                           


    st.write('top1: ê°ìêµ¬ ë§ê³¡ë(8894í)')
    st.write('top2: ë¸ìêµ¬ ìê³ë(6000í)')
    st.write('top3: ìì²êµ¬ ì ì ë(5000í)')
    st.write('top4: ìíêµ¬ ì§ê´ë(4500í)')
    st.write('top5: ì¡íêµ¬ ê±°ì¬ë(3200í)')


    df_sample = data[['SGG_NM', 'BJDONG_NM']] 
    st.write(df_sample)
    # st.write(df_sample)
    data2 = {'ì£¼ì':data[['SGG_NM']],
            'íì ë':data[['BJDONG_NM']]
            # 'counts':data[['BJDONG_NM']==data2{'íì ë'}].value_counts
            }

    
    st.write(data2)
    st.write(type(data2))
    st.write(df_sample.value_counts())
    df_sample.value_counts().groupby(level=[0,1])
    st.write(df_sample)

    # grouped = df.groupby([df.index.get_level_values(0),'Num']).size()
    
    
    # df = pd.DataFrame(data2)
    # st.write(df)


    # df_sample.columns = ['ì§ì­êµ¬','íì ë']  
    # df = pd.DataFrame(df_sample.value_counts())





    # st.write(type(df_sample))
    # st.write(type(df_sample_value))

     

    

    # st.write(df_sample.loc[0][0])
    # st.write(df_sample.loc[0][1])
    # st.write(df_sample_value.loc[[1],[1]])
    # st.write(df_sample_value.loc[[1],[2]])
    
    
    
    
    



    
    # st.write('count = f'{df_sample['íì ë'].count()}'')
    # f'{df_sample['íì ë'].count()}
   


# ì ìì¸ ê²ì í­
elif selected3 == "ðì ìì¸ ê²ì":
    run_search()

# ì ì¸ ìì¸ ìì¸¡ í­ 
elif selected3 == "ðì ì¸ ìì¸ ìì¸¡":
    run_predict()

# ê±´ìì¬í­ í­
elif selected3 == "ð¬ê±´ìì¬í­":
    run_suggestions()
else:
    selected3 == "ð Home"