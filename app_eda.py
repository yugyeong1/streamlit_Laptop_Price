import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from columns_info import column_info_data

laptop = pd.read_csv('data/laptop_price.csv', encoding= 'latin-1')
laptop['Weight'] = laptop['Weight'].str.split('k').str[0].astype(float)
laptop['Ram'] = laptop['Ram'].str.split('G').str[0].astype(float)
laptop = laptop.drop(columns= 'laptop_ID')

def run_eda_app():
    img2 = st.sidebar.image('https://1000logos.net/wp-content/uploads/2016/10/apple-emblem.jpg')
    img3 = st.sidebar.image('https://images.samsung.com/kdp/aboutsamsung/brand_identity/logo/360_197_1.png?$FB_TYPE_B_PNG$')
    img1 = st.sidebar.image('https://static.vecteezy.com/system/resources/previews/006/892/682/original/microsoft-logo-icon-editorial-free-vector.jpg')


    
    st.text(' ')
    st.text(' ')
    st.text(' ')

    col1, col2 = st.columns(2)

    with col1:
        
        img = 'https://img.appstory.co.kr/@files/monthly.appstory.co.kr/thum/Bdatafile/Board/dir_127/12789.jpg'
        st.image(img)

    with col2:
        st.text(' ')
        st.text(' ')
        st.text(' ')
        status = st.radio('정렬을 선택하세요', ['기본 데이터프레임', '가격이 저렴한 순으로 정렬','무게가 가벼운 순으로 정렬'] )

    st.text(' ')
    st.text(' ')


    if status == '기본 데이터프레임' :
        st.dataframe(laptop)
     
    elif status == '가격이 저렴한 순으로 정렬':
        st.dataframe(laptop.sort_values('Price_euros', ascending= True))

    elif status == '무게가 가벼운 순으로 정렬':
        st.dataframe(laptop.sort_values('Weight', ascending= True))

    # 컬럼 정보
    column_info_data()
    

    st.text('')
    st.text('')
    st.text('')
    st.text('')

    st.markdown('#### 회사별로 노트북 평균 가격과 평균 무게 분석하기')
    pri_or_wei = ['회사별 노트북 평균 가격', '회사별 노트북 평균 무게']
    pri_or_wei_choice = st.selectbox('분석하고자 하는 데이터를 선택하세요!', pri_or_wei)

    col1, col2 = st.columns([1, 3])
    
    with col1:
        if pri_or_wei_choice == '회사별 노트북 평균 가격' : 
            st.dataframe(laptop.groupby('Company')['Price_euros'].mean().sort_values(ascending= False).to_frame())

        elif pri_or_wei_choice == '회사별 노트북 평균 무게' :
            st.dataframe(laptop.groupby('Company')['Weight'].mean().sort_values(ascending= True).to_frame())

    with col2 :
        if pri_or_wei_choice == '회사별 노트북 평균 가격' : 
            fig1 = plt.figure()
            laptop.groupby('Company')['Price_euros'].mean().sort_values().plot(kind= 'barh')
            plt.title('Average Laptop Price by company')
            plt.xlabel('Average of Price euros')
            st.pyplot(fig1)
        
        elif pri_or_wei_choice == '회사별 노트북 평균 무게' :
            fig2 = plt.figure()
            laptop.groupby('Company')['Weight'].mean().sort_values(ascending= False).plot(kind= 'barh')
            plt.title('Average Laptop weight by company')
            plt.xlabel('Average of Weight')
            st.pyplot(fig2)

    st.text('')
    st.text('')
    st.text('')
    st.markdown('#### 데이터 중 가격이 최대/최소인 데이터는 ?')
    tab1, tab2 = st.tabs(["📈 Max Price", "📈 Min Price"])
        
    with tab1:
        st.dataframe(laptop[laptop['Price_euros'] == laptop['Price_euros'].max()])
        
    with tab2:
        st.dataframe(laptop[laptop['Price_euros'] == laptop['Price_euros'].min()])


    st.text('')
    st.text('')
    st.markdown('#### 데이터 중 노트북 무게가 최대/최소인 데이터는 ?')
    tab1, tab2 = st.tabs(["📈 Max Weight", "📈 Min Weight"])
        
    with tab1:
        st.dataframe(laptop[laptop['Weight'] == laptop['Weight'].max()])
        
    with tab2:
        st.dataframe(laptop[laptop['Weight'] == laptop['Weight'].min()])

    st.text('')
    st.text('')
    
    st.markdown('#### 상관계수 구하기')
    st.text('숫자로 되어있는 컬럼들의 상관계수 값을 구해줍니다')
    
    selected_list = st.multiselect('원하는 컬럼을 선택하세요', ['Inches', 'Ram','Weight','Price_euros'])
    if selected_list :
        st.dataframe(laptop[selected_list].corr()) 

    else :
        st.text('')