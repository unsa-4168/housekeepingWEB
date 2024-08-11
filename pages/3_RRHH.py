import streamlit as st

with st.sidebar:
   st.image("img/Logo_ended.jpg")


st.header("Recursos Humanos", divider='rainbow')

with st.form(key="publish", clear_on_submit= True):
    st.write("Mandanos Tu CV")
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")
    Posicion = st.selectbox("Posicion-Role",["Limpieza general", "Jardineria", "Limpieza de edificios", "Tintoreria y Lavado de prendas", "Administracion"])
    descripcion = st.text_input("Descripcion")
    CV = st.file_uploader("CV") 
    submit = st.form_submit_button("Subir")
    if submit:
        if len(nombre) == 0 or len(apellido) == 0:
           st.error("Intenta Nuevamente") 
        else:
           st.success("CV Registrado")

