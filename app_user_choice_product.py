import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from columns_info import column_info_data
import joblib
import numpy as np


laptop = pd.read_csv('data/laptop_price.csv', encoding= 'latin-1')
laptop = laptop.drop(columns= 'laptop_ID')
float_laptop = pd.read_csv('float_laptop.csv', index_col= 0)

regressor = joblib.load('regressor.pkl')
ct = joblib.load('ct.pkl')

def run_app_user_choice():
    
    img2 = st.sidebar.image('https://blog.elpo.net/wp-content/uploads/2021/09/lenovo-bootlogo.png')
    img3 = st.sidebar.image('https://dlcdnimgs.asus.com/websites/global/Sno/79183.jpg')
    img4 = st.sidebar.image('https://www.pngplay.com/wp-content/uploads/9/HP-Logo-Download-Free-PNG.png')



    st.markdown('#### 📌 사용자가 선택한 옵션의 노트북을 추천해줍니다!')
    st.text('')
    st.text('')

    col1, col2 = st.columns(2)
    with col1 :
        img = 'https://news.samsungdisplay.com/wp-content/uploads/2021/01/210121-%EB%B3%B8%EB%AC%B8-%EC%82%BC%EC%84%B1%EB%94%94%EC%8A%A4%ED%94%8C%EB%A0%88%EC%9D%B4-%EB%85%B8%ED%8A%B8%EB%B6%81%EC%9A%A9-OLED-%ED%8C%A8%EB%84%90.jpg'
        st.image(img)
    
    with col2 :
        st.text('')
        st.text('')
        
        status = st.radio(' ', ['📈 제품 가격 예측하기', '📈 사용자가 선택한 제품 데이터 보기'] )



    if status == '📈 제품 가격 예측하기':
        st.text('')
        st.markdown('#### 옵션을 선택하면 가격을 예측합니다! 💻')
        st.text('')
        typename = st.selectbox('노트북 타입을 선택하세요.', float_laptop['TypeName'].unique())
        inch = st.selectbox('원하는 인치를 선택하세요 ', float_laptop['Inches'].sort_values().unique()) 
        cpu = st.selectbox('원하는 Cpu 를 선택하세요 ', float_laptop['Cpu'].sort_values().unique())
        ram = st.selectbox('원하는 Ram 을 선택하세요 ', float_laptop['Ram'].sort_values().unique())
        memory = st.selectbox('원하는 Memory 을 선택하세요 ', float_laptop['Memory'].sort_values().unique())
        weight = st.selectbox('원하는 Weight 를 선택하세요 (kg)', float_laptop['Weight'].sort_values().unique(), on_change=None)


        new_data = np.array([typename, inch,cpu, ram, memory, weight])
        new_data = new_data.reshape(1,6)
        new_data = ct.transform(new_data)
        new_data_pred = regressor.predict(new_data)
        st.text('')

        st.info('선택한 옵션의 노트북 예상 가격은 {} euro 입니다. '.format(new_data_pred[0]))




    if status == '📈 사용자가 선택한 제품 데이터 보기' :
       
        st.text('')
        st.markdown('#### 💻 원하는 옵션을 선택해주세요! 💻')
        st.text('')
        type_choice = st.selectbox('가장 먼저, 원하는 노트북 타입을 선택하세요 ', laptop['TypeName'].unique())
        type_choice_frame = laptop[laptop['TypeName']== type_choice]

        inches_choice = st.selectbox('원하는 인치를 선택하세요 ', type_choice_frame['Inches'].sort_values().unique()) 
        inches_choice_frame = type_choice_frame[type_choice_frame['Inches'] == inches_choice]

        ram_choice = st.selectbox('원하는 Ram 을 선택하세요 ', inches_choice_frame['Ram'].sort_values().unique())
        ram_choice_frame = type_choice_frame[type_choice_frame['Ram'] == ram_choice]

        memory_choice = st.selectbox('원하는 Memory 을 선택하세요 ', ram_choice_frame['Memory'].sort_values().unique())
        memory_choice_frame = ram_choice_frame[ram_choice_frame['Memory'] == memory_choice]

        cpu_choice = st.selectbox('원하는 Cpu 를 선택하세요 ', memory_choice_frame['Cpu'].sort_values().unique())
        cpu_choice_frame = memory_choice_frame[memory_choice_frame['Cpu'] == cpu_choice]

        weight_choice = st.selectbox('원하는 Weight 를 선택하세요 ', memory_choice_frame['Weight'].sort_values().unique(), on_change=None)
        weight_choice_frame = cpu_choice_frame[cpu_choice_frame['Weight'] == weight_choice]

        st.text('')
        st.text('')
        st.markdown('#### 📢 선택한 옵션과 일치하는 데이터입니다.')
        st.text('')
        st.dataframe(weight_choice_frame)

        column_info_data()