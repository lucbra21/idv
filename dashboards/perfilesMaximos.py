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
    
    with col1:
      st.markdown(f"""
      <h3 style="font-size: 24px; text-align: center; color: #333;">Max Total Distance (m) \n 
      <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{max_total_distance} m</text></h3>
      """, unsafe_allow_html=True)
    with col2:
      st.markdown(f"""
      <h3 style="font-size: 24px; text-align: center; color: #333;">Max B5 Distance (m) \n 
      <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{max_b5_total_distance} m</text></h3>
      """, unsafe_allow_html=True)
    with col3:
      st.markdown(f"""
      <h3 style="font-size: 24px; text-align: center; color: #333;">Max B6 Distance (m) \n 
      <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{max_b6_total_distance} m</text></h3>
      """, unsafe_allow_html=True)
    with col4:
      st.markdown(f"""
      <h3 style="font-size: 24px; text-align: center; color: #333;">Max B7 Distance (m) \n 
      <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{max_b7_total_distance} m</text></h3>
      """, unsafe_allow_html=True)  

    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 450,
    mode = "gauge+number+delta",
    title = {'text': "Speed"},
    delta = {'reference': 380},
    gauge = {'axis': {'range': [None, 500]},
             'steps' : [
                 {'range': [0, 250], 'color': "lightgray"},
                 {'range': [250, 400], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))

    fig.show()  
  