import streamlit as st

st.set_page_config(
    page_title="CLEAN&SHINE",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

with st.sidebar:
   st.image("img/Logo_ended.jpg")

st.title("CLEAN & SHINE SALTA")

st.image("img/edificio.png")

st.header('Sobre Nosotros', divider='rainbow')
st.text("""CLEAN & SHINE Salta es una empresa salteña creada en 2021 con el objetivo de satisfacer 
una demanda creciente de sevicios de limpieza. Con un personal calificado, el uso de maquinaria
y tecnologia no hemos parado de crecer.
En la actualidad es una de las empresas con mayor crecimiento en Salta.""")

col1, col2 = st.columns(2)

with col1:
   st.image("img/Agencia_de_limpieza.png", width=300)

with col2:
   st.subheader("Razones Para Contratarnos")
   st.markdown("""
- Independencia
- Riesgo Laboral Cero
- Costo Reducido
- Eficiencia
- Disponibilidad
 """)

st.header('Nuestros Servicios', divider='rainbow')

with st.expander("CLEAN & SHINE pone a su disposición una amplia gama de Servicios de Limpieza, Fijos o Eventuales",expanded=True):
   st.markdown("""
   - Limpieza general
   - Trabajos en altura
   - Espacios verdes 
   - Finales de obra
   - Tintoreria
   - Superficies vidriadas y metálicas
   - Manejo integrado de plagas""")

st.header('Informacion de contacto', divider='rainbow')

st.text("Direccion: Barrio municipal de Atocha manzana B lote 36")
st.text("correo: clean.and.shine.sas@gmail.com")
st.text("Telefono: +5493816425902")