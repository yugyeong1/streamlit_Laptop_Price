import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from columns_info import column_info_data

laptop = pd.read_csv('data/laptop_price.csv', encoding= 'latin-1')
laptop = laptop.drop(columns= 'laptop_ID')

def run_app_user_choice():

    img4 = st.sidebar.image('https://blog.elpo.net/wp-content/uploads/2021/09/lenovo-bootlogo.png')
    img2 = st.sidebar.image('https://dlcdnimgs.asus.com/websites/global/Sno/79183.jpg')
    img3 = st.sidebar.image('https://www.pngplay.com/wp-content/uploads/9/HP-Logo-Download-Free-PNG.png')



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
        st.text('')

        check1 = st.checkbox('📈 기본 데이터프레임 보기', value = True)
        check2 = st.checkbox('📈 사용자가 선택한 제품 데이터 보기')



    if check1 :
        st.text('')
        st.text('')
        tab1, tab2, tab3 = st.tabs(["📑 기본 정렬", "📄 가격 저렴한 순" , '📑 무게가 가벼운 순'])

        with tab1 :
            st.dataframe(laptop)

        with tab2 :
            st.dataframe(laptop.sort_values('Price_euros', ascending= True))

        with tab3 :
            st.dataframe(laptop.sort_values('Weight', ascending= True))

        st.text('')

    if check2 :
       
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
