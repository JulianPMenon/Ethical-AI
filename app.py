#imports
import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("Ethical-Artificial-Inteligence")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Check an argument for Inapproprietness")
        
        with st.form(key='myform'):
            raw_text = st.text_area("Input an argument here.")
            submit_text = st.form_submit_button()
        
    else:
        st.subheader("About")
        
if __name__ == '__main__':
    main()