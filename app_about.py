import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from columns_info import column_info_data


laptop = pd.read_csv('data/laptop_price.csv', encoding= 'latin-1')
laptop = laptop.drop(columns= 'laptop_ID')

def run_about_app():

    img1 = st.sidebar.image('https://images.velog.io/images/osk3856/post/673a3997-1da6-40f5-bea2-8b6fc2ee66b1/dataanalysis.jpg')
    st.text('')
    st.text('')
    st.markdown('#### 📌  데이터분석에 이용한 데이터프레임')
    st.text('')

    st.dataframe(laptop)
    column_info_data()
