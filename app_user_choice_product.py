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



    st.markdown('#### π μ¬μ©μκ° μ νν μ΅μμ λΈνΈλΆμ μΆμ²ν΄μ€λλ€!')
    st.text('')
    st.text('')

    col1, col2 = st.columns(2)
    with col1 :
        img = 'https://news.samsungdisplay.com/wp-content/uploads/2021/01/210121-%EB%B3%B8%EB%AC%B8-%EC%82%BC%EC%84%B1%EB%94%94%EC%8A%A4%ED%94%8C%EB%A0%88%EC%9D%B4-%EB%85%B8%ED%8A%B8%EB%B6%81%EC%9A%A9-OLED-%ED%8C%A8%EB%84%90.jpg'
        st.image(img)
    
    with col2 :
        st.text('')
        st.text('')
        
        status = st.radio(' ', ['π μ ν κ°κ²© μμΈ‘νκΈ°', 'π μ¬μ©μκ° μ νν μ ν λ°μ΄ν° λ³΄κΈ°'] )



    if status == 'π μ ν κ°κ²© μμΈ‘νκΈ°':
        st.text('')
        st.markdown('#### μ΅μμ μ ννλ©΄ κ°κ²©μ μμΈ‘ν©λλ€! π»')
        st.text('')
        typename = st.selectbox('λΈνΈλΆ νμμ μ ννμΈμ.', float_laptop['TypeName'].unique())
        inch = st.selectbox('μνλ μΈμΉλ₯Ό μ ννμΈμ ', float_laptop['Inches'].sort_values().unique()) 
        cpu = st.selectbox('μνλ Cpu λ₯Ό μ ννμΈμ ', float_laptop['Cpu'].sort_values().unique())
        ram = st.selectbox('μνλ Ram μ μ ννμΈμ ', float_laptop['Ram'].sort_values().unique())
        memory = st.selectbox('μνλ Memory μ μ ννμΈμ ', float_laptop['Memory'].sort_values().unique())
        weight = st.selectbox('μνλ Weight λ₯Ό μ ννμΈμ (kg)', float_laptop['Weight'].sort_values().unique(), on_change=None)


        new_data = np.array([typename, inch,cpu, ram, memory, weight])
        new_data = new_data.reshape(1,6)
        new_data = ct.transform(new_data)
        new_data_pred = regressor.predict(new_data)
        st.text('')

        st.info('μ νν μ΅μμ λΈνΈλΆ μμ κ°κ²©μ {} euro μλλ€. '.format(new_data_pred[0]))




    if status == 'π μ¬μ©μκ° μ νν μ ν λ°μ΄ν° λ³΄κΈ°' :
       
        st.text('')
        st.markdown('#### π» μνλ μ΅μμ μ νν΄μ£ΌμΈμ! π»')
        st.text('')
        type_choice = st.selectbox('κ°μ₯ λ¨Όμ , μνλ λΈνΈλΆ νμμ μ ννμΈμ ', laptop['TypeName'].unique())
        type_choice_frame = laptop[laptop['TypeName']== type_choice]

        inches_choice = st.selectbox('μνλ μΈμΉλ₯Ό μ ννμΈμ ', type_choice_frame['Inches'].sort_values().unique()) 
        inches_choice_frame = type_choice_frame[type_choice_frame['Inches'] == inches_choice]

        ram_choice = st.selectbox('μνλ Ram μ μ ννμΈμ ', inches_choice_frame['Ram'].sort_values().unique())
        ram_choice_frame = type_choice_frame[type_choice_frame['Ram'] == ram_choice]

        memory_choice = st.selectbox('μνλ Memory μ μ ννμΈμ ', ram_choice_frame['Memory'].sort_values().unique())
        memory_choice_frame = ram_choice_frame[ram_choice_frame['Memory'] == memory_choice]

        cpu_choice = st.selectbox('μνλ Cpu λ₯Ό μ ννμΈμ ', memory_choice_frame['Cpu'].sort_values().unique())
        cpu_choice_frame = memory_choice_frame[memory_choice_frame['Cpu'] == cpu_choice]

        weight_choice = st.selectbox('μνλ Weight λ₯Ό μ ννμΈμ ', memory_choice_frame['Weight'].sort_values().unique(), on_change=None)
        weight_choice_frame = cpu_choice_frame[cpu_choice_frame['Weight'] == weight_choice]

        st.text('')
        st.text('')
        st.markdown('#### π’ μ νν μ΅μκ³Ό μΌμΉνλ λ°μ΄ν°μλλ€.')
        st.text('')
        st.dataframe(weight_choice_frame)

        column_info_data()