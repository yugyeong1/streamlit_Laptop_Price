import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app
from app_user_choice_product import run_app_user_choice

def main() :
    st.title('Laptop Price 데이터 분석 앱 💻')


    menu = ['Home', 'EDA' ,'User choice product']
    choice = st.sidebar.selectbox('메뉴', menu)
    st.sidebar.text('')



    if choice == 'Home' :
        run_home_app()
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'User choice product' :
        run_app_user_choice()



if __name__ == '__main__' :
    main()