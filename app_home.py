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

    with st.expander('๐ ๋์๋ณด๋ ์ค๋ช') :
        st.text('์ด ์ฑ์ Kaggle์ Laptop Price ๋ฐ์ดํฐ๋ฅผ ์ด์ฉํ์ฌ์, ')
        st.text('Laptop ์ ๊ธฐ๋ณธ ์ฑ๋ฅ๊ณผ ๊ฐ๊ฒฉ์ ๋ถ์ํ์ฌ ๋ฐ์ดํฐ๋ฅผ ๋น๊ตํ์๊ณ ,')
        st.text('์ฌ์ฉ์๊ฐ ์ํ๋ ๋ธํธ๋ถ ์ต์์ ์ ํํ๋ฉด, ํด๋น ์ต์ ๊ธฐ๋ฅ์ด ์๋ ๋ธํธ๋ถ์ ์ถ์ฒํด์ฃผ๋ ์ฑ ์๋๋ค.')
        st.text('๋ฐ์ดํฐ ์ถ์ฒ : https://www.kaggle.com/datasets/muhammetvarl/laptop-price')
    
    st.text(' ')
    
    # ์ ํ๋ธ ๋์์ ์ฒจ๋ถ
    data= 'https://youtu.be/jql5JhKqIG0'
    st.video(data, format="video/mp4", start_time=0)

    data1= 'https://youtu.be/hUCKW8YUkGM'
    st.video(data1, format="video/mp4", start_time=0)

