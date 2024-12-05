import plotly.express as px
import streamlit as st

def perfilesMaximos(df_selection):
      # Aquí muestra los gráficos o estadísticas que se relacionen con el resumen general
    st.write("Dashboard: Perfiles Maximos en Competicion")
    
    max_total_distance = int(df_selection["Total Distance"].max())
    max_b5_total_distance = int(df_selection["Velocity Band 5 Total Distance"].max())
    max_b6_total_distance = int(df_selection["Velocity Band 6 Total Distance"].max())
    max_b7_total_distance = int(df_selection["Velocity Band 7 Total Distance"].max())
    
    max_acc_2_4 = int(df_selection["Aceleraciones 2 a 4"].max())
    max_acc_4 = int(df_selection["Aceleraciones mayores a 4"].max())
    max_dec_2_4 = int(df_selection["Desaceleraciones 2 a 4"].max())
    max_dec_4 = int(df_selection["Desaceleraciones mayores a 4"].max())
    
    max_mt_min = int(df_selection["Meterage Per Minute"].max())
    max_velocity = int(df_selection["Maximum Velocity"].max())
    max_acc = int(df_selection["Max Acceleration"].max())
    max_dec = int(df_selection["Max Deceleration"].max())
    
    # Create 3 main columns: left_col, mid_col, right_col
    col1, col2, col3, col4 = st.columns(4)  # Set the relative widths as needed

    col1.subheader("Max Total Distance (m)")
    col1.subheader(f"{max_total_distance} m")
    col2.subheader("Max B5 Distance (m)")
    col2.subheader(f"{max_b5_total_distance} m")
    col3.subheader("Max B6 Distance (m)")
    col3.subheader(f"{max_b6_total_distance} m")
    col4.subheader("Max B7 Distance (m)")
    col4.subheader(f"{max_b7_total_distance} m")
    
    col1.subheader("Max Acc 2-4 (Nº Esf)")
    col1.subheader(f"{max_acc_2_4}")
    col2.subheader("Max Acc >4 (Nº Esf)")
    col2.subheader(f"{max_acc_4}")
    col3.subheader("Max Dec 2-4 (Nº Esf)")
    col3.subheader(f"{max_dec_2_4}")
    col4.subheader("Max Dec >4 (Nº Esf)")
    col4.subheader(f"{max_dec_4}")
    
    col1.subheader("Max Meters/Min")
    col1.subheader(f"{max_mt_min}")
    col2.subheader("Max Vel Max (km/h)")
    col2.subheader(f"{max_velocity}")
    col3.subheader("Max Acc (m/s2)")
    col3.subheader(f"{max_acc}")
    col4.subheader("Max Dec (m/s2)")
    col4.subheader(f"{max_dec}")