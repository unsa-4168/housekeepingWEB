import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configuración del servidor y del correo electrónico
smtp_server = 'smtp.mail.me.com'
smtp_port = 587
email_user = 'chesteraraoz12.0@icloud.com'
email_password = 'onld-fcta-uamq-jrax'


with st.sidebar:
   st.image("img/Logo_ended.jpg")

st.header("Contacta con Nosotros", divider='rainbow')
st.text("""Nuestra filosofía de trabajo es brindar el mejor servicio al mejor precio. 
Para comprobarlo no tiene más que comunicarse con nosotros y descubrirá nuestra eficiencia,
idoneidad y celeridad para solucionar sus problemas con el personal más apto para ello.
Llena todos los campos y te contestaremos a la brevedad""")

with st.form(key="contacto", clear_on_submit= True):
    st.write("Escribe aqui tu consulta")
    correo = st.text_input("Tu Correo")
    nombre = st.text_input("Nombre o Empresa")
    msg = st.text_input("Mensaje")
    submit = st.form_submit_button("Enviar")
    if submit:
        if len(correo) == 0:
           st.error("Intenta Nuevamente") 
        else:
           # Información del correo electrónico
            from_email = 'chesteraraoz12.0@icloud.com'
            to_email = 'chesteraraoz12.0@gmail.com'
            subject = 'agencia de limpieza'
            body = f"{correo, nombre, msg}"

           # Crear el mensaje
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject
           # Adjuntar el cuerpo del mensaje en HTML
            msg.attach(MIMEText(body, 'html'))

           # Conectar al servidor SMTP y enviar el correo
            try:
               server = smtplib.SMTP(smtp_server, smtp_port)
               server.starttls()  # Iniciar la conexión TLS (segura)
               server.login(email_user, email_password)
               text = msg.as_string()
               server.sendmail(from_email, to_email, text)
               print('Correo enviado exitosamente')
            except Exception as e:
               print(f'Error al enviar el correo: {e}')
            finally:
               server.quit()
            st.success("Consulta enviada")


st.header('Informacion de contacto', divider='rainbow')

st.text("Direccion: Barrio municipal de Atocha manzana B lote 36")
st.text("correo: clean.and.shine.sas@gmail.com")
st.text("Telefono: +5493816425902")