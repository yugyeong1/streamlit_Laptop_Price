import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app
from app_user_choice_product import run_app_user_choice
from app_about import run_about_app

def main() :
    st.title('Laptop Company Price List  분석')


    menu = ['Home', 'EDA', 'User choice product', 'About']
 
    choice = st.sidebar.selectbox('메뉴', menu)



    if choice == 'Home' :
        run_home_app()
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'User choice product' :
        run_app_user_choice()
    elif choice == 'About' :
        run_about_app()



if __name__ == '__main__' :
    main()