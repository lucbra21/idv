import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import plotly.express as px
import hashlib
import os

from data.preprocess import preprocess_files
from dashboards.resumen_general import resumen_general
from dashboards.resumen_semanal import resumen_semanal
from dashboards.total_relative_distance import total_relative_distance
from dashboards.acc_dec import acc_dec
from dashboards.accelerations import accelerations
from dashboards.decelerations import decelerations
from dashboards.band5 import band5
from dashboards.band6 import band6
from dashboards.band7 import band7
from dashboards.band8 import band8
from dashboards.hsr_vhsr import hsr_vhsr
from dashboards.max_velocity import max_velocity
from dashboards.player_load import player_load
from dashboards.perfilesMaximos import perfilesMaximos


st.set_page_config(layout="wide")

@st.cache_data


def get_data():
  columns_to_read = ["Date","Semana", "Mes", "Dia", "Acceleration B2-3 Average Efforts (Session) (Gen 2)", 
                   "Posicion","Apellido", "Sesion", "Deceleration B2-3 Average Efforts (Session) (Gen 2)",
                   "PartidoEntreno", "Aceleraciones 2 a 4", "Aceleraciones mayores a 4", "AccMayoresGen2",
                   "Total Distance", "Velocity Band 5 Total Distance", "Velocity Band 5 Total Effort Count",
                   "Band5 %", "Velocity Band 6 Total Distance", "Velocity Band 6 Total Effort Count",
                   "Band6 %", "Velocity Band 7 Total Distance", "Velocity Band 7 Total Effort Count",
                   "Band7 %", "Velocity Band 8 Total Distance", "Velocity Band 8 Total Effort Count",
                   "Band8 %","Desaceleraciones 2 a 4", "Desaceleraciones mayores a 4", "Dist +17 km/h",
                   "Dist +25 km/h", "Maximum Velocity", "Max Vel (% Max)", "Total Player Load",
                   "Player Load Per Minute", "HSR %","VHSR %", "Relative Distance"]
  df = pd.read_excel("data.xlsx", usecols=columns_to_read)
  return df

# Lista de nombres de usuario y contraseñas
usernames = ["mauroceruti"]
passwords = ["1"]  # Reemplaza con tu contraseña real

# Función para hashear contraseñas
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Hashear las contraseñas
hashed_passwords = [hash_password(pw) for pw in passwords]

# Inicializar el estado de autenticación en `st.session_state`
if "authentication_status" not in st.session_state:
    st.session_state.authentication_status = None

# Página de login
if st.session_state.authentication_status != True:
    st.title("Login")

    username_input = st.text_input("Nombre de usuario")
    password_input = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if username_input in usernames:
            index = usernames.index(username_input)
            if hash_password(password_input) == hashed_passwords[index]:
                st.session_state.authentication_status = True
                st.session_state.username = username_input
                st.success(f"¡Bienvenido {username_input}!")
                
            else:
                st.error("Contraseña incorrecta")
        else:
            st.error("El nombre de usuario no existe")
else:

    menu_option = st.sidebar.selectbox("Elige una opción", ["Subir Archivo", "Eliminar Archivo", "Ver Datos"])

    if menu_option == "Subir Archivo":
        # Página para subir archivo
        st.subheader("Sube tu archivo CSV")

        # Opción para subir archivo
        uploaded_file = st.file_uploader("Sube tu archivo", type=["csv"])

        if uploaded_file is not None:
            # Opción para elegir si es un entreno o un partido
            session_type = st.radio("Selecciona el tipo de sesión:", ("Entreno", "Partido"))
            # Crear las carpetas si no existen
            entreno_folder = "entrenos"
            partido_folder = "partidos"

            if not os.path.exists(entreno_folder):
                os.makedirs(entreno_folder)

            if not os.path.exists(partido_folder):
                os.makedirs(partido_folder)

            # Guardar el archivo en la carpeta correspondiente
            if st.button("Guardar y procesar archivo"):
                if session_type == "Entreno":
                    save_path = os.path.join(entreno_folder, uploaded_file.name)
                else:
                    save_path = os.path.join(partido_folder, uploaded_file.name)

                # Save the file
                with open(save_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success(f"Archivo guardado en la carpeta '{session_type.lower()}'.")
                preprocess_files()
        
    elif menu_option == "Eliminar Archivo":
        st.subheader("Elimina un archivo")
        # Seleccionar tipo de sesión para ver archivos
        session_type = st.radio("Selecciona el tipo de sesión:", ("Entreno", "Partido"))

        if session_type == "Entreno":
            folder = "entrenos"
        else:
            folder = "partidos"

        # Verificar si hay archivos en la carpeta seleccionada
        files = os.listdir(f"./data/{folder}") if os.path.exists(f"./data/{folder}") else []
            
        if files:
            selected_file = st.selectbox("Selecciona un archivo para eliminar:", files)
                
            # Botón para eliminar archivo seleccionado
            if st.button("Eliminar archivo"):
                file_path = os.path.join(folder, selected_file)
                    
                # Verificar si el archivo existe y eliminar
                if os.path.exists(file_path):
                    os.remove(file_path)
                    st.success(f"Archivo '{selected_file}' eliminado exitosamente.")
                    preprocess_files()
                else:
                    st.error("El archivo no existe.")
        else:
            st.write(f"No hay archivos en la carpeta '{folder}'.")
                
    elif menu_option == "Ver Datos":
        df = get_data()
        dashboard_type = st.sidebar.selectbox(
            "Selecciona el tipo de Dashboard",
            options=[
                "Resumen General", 
                "Resumen por Semana", 
                "Total & Relative Distance", 
                "ACC & DEC", 
                "ACC",
                "DEC", 
                "Vel Band 5 (HIR)",
                "Vel Band 6 (HSR)",
                "Vel Band 7 (VHSR)",
                "Vel Band 8", 
                "HSR & VHSR", 
                "Maximun Velocity", 
                "Player Load",
                "Pefiles Maximos"
            ]
        )

        st.sidebar.header("Please Filter Here: ")
        
        hoy = pd.Timestamp(datetime.now())
        
        df['Days_Difference'] = (df['Date'] - hoy).abs()

        # Obtener la fila con la menor diferencia
        fila_mas_cercana = df.loc[df['Days_Difference'].idxmin()]
        
        semana_cercana = fila_mas_cercana['Semana']
        mes_cercano = fila_mas_cercana['Mes']
        dia_cercano = fila_mas_cercana['Dia']


        st.sidebar.header("Please Filter Here: ")


        semana=st.sidebar.multiselect(
            "Elige la semana",
            options=df.Semana.unique(),
            default=semana_cercana
        )

        mes=st.sidebar.multiselect(
            "Elige el Mes",
            options=df.Mes.unique(),
            default=mes_cercano
        )

        dia=st.sidebar.multiselect(
            "Elige el Dia",
            options=df.Dia.unique(),
            default=dia_cercano
        )

        posicion=st.sidebar.multiselect(
            "Elige la Posicion",
            options=df.Posicion.unique(),
            default=df.Posicion.unique()
        )

        apellido=st.sidebar.multiselect(
            "Elige el Apellido",
            options=df.Apellido.unique(),
            default=df.Apellido.unique()
        )

        sesion=st.sidebar.multiselect(
            "Elige la Sesion",
            options=df.Sesion.unique(),
            default=df.Sesion.unique()
        )

        partido_entreno=st.sidebar.multiselect(
            "Elige entre Partido y Entreno",
            options=df["PartidoEntreno"].unique(),
            default=df["PartidoEntreno"].unique()
        )


        df_selection = df.query(
            "Semana == @semana & Mes == @mes & Dia == @dia & Posicion == @posicion & Apellido == @apellido & Sesion == @sesion & PartidoEntreno == @partido_entreno"
        )



        if dashboard_type == "Resumen General":
            resumen_general(df_selection)
        if dashboard_type == "Resumen por Semana":
            resumen_semanal(df_selection)
        if dashboard_type == "Total & Relative Distance":
            total_relative_distance(df_selection)
        if dashboard_type == "ACC & DEC":
            acc_dec(df_selection)
        if dashboard_type == "ACC":
            accelerations(df_selection)
        if dashboard_type == "DEC":
            decelerations(df_selection)
        if dashboard_type == "Vel Band 5 (HIR)":
            band5(df_selection)
        if dashboard_type == "Vel Band 6 (HSR)":
            band6(df_selection)
        if dashboard_type == "Vel Band 7 (VHSR)":
            band7(df_selection)
        if dashboard_type == "Vel Band 8":
            band8(df_selection)
        if dashboard_type == "HSR & VHSR":
            hsr_vhsr(df_selection) 
        if dashboard_type == "Maximun Velocity":
            max_velocity(df_selection)
        if dashboard_type == "Player Load":
            player_load(df_selection)
        if dashboard_type == "Pefiles Maximos":
            perfilesMaximos(df_selection)  

