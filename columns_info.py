import streamlit as st

def column_info_data() :
    with st.expander('Columns') :
        st.text('Company : 회사명')
        st.text('Product : 제품명')
        st.text('TypeName : 노트북 타입 (Notebook, Ultrabook, Gaming, etc.)')
        st.text('Inches : 화면 크기')
        st.text('ScreenResolution : 화면 해상도')
        st.text('Cpu : Cpu 값')
        st.text('Ram : RAM(GB)')
        st.text('Memory : Hard Disk / SSD Memor')
        st.text('Gpu : 그래픽 처리 장치')
        st.text('OpSys : 작동 시스템')
        st.text('Weight : 노트북 무게')
        st.text('Price_euro : 노트북 가격')
    