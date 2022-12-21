import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from columns_info import column_info_data


def run_home_app() :
    img1 = st.sidebar.image('https://file.bodnara.co.kr/logo/insidelogo.php?image=%2Fhttp%3A%2F%2Ffile.bodnara.co.kr%2Fwebedit%2Fnews%2F2015%2F1653444904-22052505.jpg')
    img2 = st.sidebar.image('https://www.pchouse.com.bd/image/cache/catalog/Brand%20Logo/chuwi-600x315h.jpg', use_column_width= True)
    img4 = st.sidebar.image('https://sg-live-01.slatic.net/p/7b0e3dd525ac2b27d6c5c3a28345bd4f.jpg')
    img3 = st.sidebar.image('https://kr.moyens.net/wp-content/uploads/2022/03/1646282416_iPhone-iPad-%EB%B0%8F-Mac%EC%97%90%EC%84%9C-Apple-%EB%A1%9C%EA%B3%A0%EB%A5%BC-%EC%9E%85%EB%A0%A5%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95.jpg')

    st.text('')
    st.text('')

    with st.expander('대시보드 설명') :
        st.text('이 앱은 Kaggle의 Laptop Price 데이터를 이용하여서, ')
        st.text('Laptop 의 기본 성능과 가격을 분석하여 데이터를 비교하였고,')
        st.text('사용자가 원하는 노트북 옵션을 선택하면, 해당 옵션 기능이 있는 노트북을 추천해주는 앱 입니다.')
        st.text('데이터 출처 : https://www.kaggle.com/datasets/muhammetvarl/laptop-price')
    
    st.text(' ')
    
    # 유튜브 동영상 첨부
    data= 'https://youtu.be/jql5JhKqIG0'
    st.video(data, format="video/mp4", start_time=0)

    data1= 'https://youtu.be/hUCKW8YUkGM'
    st.video(data1, format="video/mp4", start_time=0)

