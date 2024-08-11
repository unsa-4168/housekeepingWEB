import streamlit as st
from time import sleep

with st.sidebar:
   st.image("img/Logo_ended.jpg")


st.header("Login", divider='rainbow')
with st.expander("Solo para clientes Registrados", expanded=True):
    with st.form("Login"):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        submitted2 = st.form_submit_button("Login")
        if submitted2:
           with st.spinner('Wait for it...'):
                sleep(3)
                st.error("User Not Found!")