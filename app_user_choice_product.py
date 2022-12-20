import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from columns_info import column_info_data

laptop = pd.read_csv('data/laptop_price.csv', encoding= 'latin-1')
laptop['Weight'] = laptop['Weight'].str.split('k').str[0].astype(float)
laptop['Ram'] = laptop['Ram'].str.split('G').str[0].astype(float)
laptop = laptop.drop(columns= 'laptop_ID')

def run_app_user_choice():

    st.text('')
    st.text('')
    st.markdown('#### 유저가 선택한 데이터의 값을 나타냅니다.')

    col1, col2 = st.columns(2)

    with col1:
        pass

    with col2:
        company_choice = st.selectbox(' ', laptop['Company'].unique())
        type_choice = st.selectbox(' ', laptop['TypeName'].unique())
    

    st.dataframe(laptop[laptop['Company']== company_choice])


