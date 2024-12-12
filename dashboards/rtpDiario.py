import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def rtpDiario(df_selection):
      # Aquí muestra los gráficos o estadísticas que se relacionen con el resumen general    
    max_total_distance = int(df_selection["Max Dist Partido"])
    distance = int(df_selection["Total Distance"])
    pct_distance = int((distance * 100) / max_total_distance)
    
    max_total_distance_b5 = int(df_selection["Max Dist Partido B5"])
    distance_b5 = int(df_selection["Velocity Band 5 Total Distance"])
    pct_distance_b5 = int((distance_b5 * 100) / max_total_distance_b5)

    max_total_distance_b6 = int(df_selection["Max Dist Partido B6"])
    distance_b6 = int(df_selection["Velocity Band 6 Total Distance"])
    pct_distance_b6 = int((distance_b6 * 100) / max_total_distance_b6)

    max_total_distance_b7 = int(df_selection["Max Dist Partido B7"])
    distance_b7 = int(df_selection["Velocity Band 7 Total Distance"])
    pct_distance_b7 = int((distance_b7 * 100) / max_total_distance_b7)
    
    max_maximum_vel= int(df_selection["Max Maximum Velocity"])
    max_vel = int(df_selection["Maximum Velocity"])
    pct_max_vel = int((max_vel * 100) / max_maximum_vel)
    
    max_maximum_meterage_min= int(df_selection["Max Meterage per Minute"])
    max_meterage_min = int(df_selection["Meterage Per Minute"])
    pct_max_meterage_min = int((max_meterage_min * 100) / max_maximum_meterage_min)
    
    max_maximun_acc_2_4= int(df_selection["Max Acc 2-4"])
    max_acc_2_4 = int(df_selection["Acceleration B2-3 Total Efforts (Gen 2)"])
    pct_max_acc_2_4 = int((max_acc_2_4 * 100) / max_maximun_acc_2_4)

    max_maximun_dec_2_4= int(df_selection["Max Dec 2-4"])
    max_dec_2_4 = int(df_selection["Deceleration B2-3 Total Efforts (Gen 2)"])
    pct_max_dec_2_4 = int((max_dec_2_4 * 100) / max_maximun_dec_2_4)
    
    max_maximun_acc_mayor_4= int(df_selection["Max Acc Mayor 4"])
    max_acc_mayor_4 = int(df_selection["Acceleration B3 Efforts (Gen 2)"])
    pct_max_acc_mayor_4 = int((max_acc_mayor_4 * 100) / max_maximun_acc_mayor_4)
    
    max_maximun_dec_mayor_4= int(df_selection["Max Dec Mayor 4"])
    max_dec_mayor_4 = int(df_selection["Deceleration B3 Efforts (Gen 2)"])
    pct_max_dec_mayor_4 = int((max_dec_mayor_4 * 100) / max_maximun_dec_mayor_4)
    
    max_maximum_accelerations = int(df_selection["Max Max Accelerations"])
    max_accelerations = int(df_selection["Max Acceleration"])
    pct_max_accelerations = int((max_accelerations * 100) / max_maximum_accelerations)
    
    max_maximum_decelerations = int(df_selection["Max Max Decelerations"])
    max_decelerations = int(df_selection["Max Deceleration"])
    pct_max_decelerations = int((max_decelerations * 100) / max_maximum_accelerations) #PONER BIEN
        
    # Create 3 main columns: left_col, mid_col, right_col
    col1, col2, col3, col4, col5, col6 = st.columns(6)  # Set the relative widths as needed
    
    fig_total_distance = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_distance,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, max_total_distance], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, distance], 'color': "blue"},  # Blue for the percentage value
              {'range': [distance, max_total_distance], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_total_distance.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>T.D (m)<br><br><span style='font-size:1.8em'>{distance}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col1.plotly_chart(fig_total_distance, use_container_width=True)

    fig_total_distance_b5 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_distance_b5,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, max_total_distance_b5], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, distance_b5], 'color': "blue"},  # Blue for the percentage value
              {'range': [distance_b5, max_total_distance_b5], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_total_distance_b5.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>Band 5 (m)<br><br><span style='font-size:1.8em'>{distance_b5}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col2.plotly_chart(fig_total_distance_b5, use_container_width=True)
    
    fig_total_distance_b6 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_distance_b6,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, max_total_distance_b6], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, distance_b6], 'color': "blue"},  # Blue for the percentage value
              {'range': [distance_b6, max_total_distance_b6], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_total_distance_b6.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>Band 6 (m)<br><br><span style='font-size:1.8em'>{distance_b6}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col3.plotly_chart(fig_total_distance_b6, use_container_width=True)
  
    fig_total_distance_b7 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_distance_b7,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, max_total_distance_b7], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, distance_b7], 'color': "blue"},  # Blue for the percentage value
              {'range': [distance_b7, max_total_distance_b7], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_total_distance_b7.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>Band 7 (m)<br><br><span style='font-size:1.8em'>{distance_b7}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
    )
    
    col4.plotly_chart(fig_total_distance_b7, use_container_width=True)
    
    fig_max_velocity = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_max_vel,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, 100], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, pct_max_vel], 'color': "blue"},  # Blue for the percentage value
              {'range': [pct_max_vel, 100], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_max_velocity.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>Max Vel (km/h)<br><br><span style='font-size:1.8em'>{max_vel}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col5.plotly_chart(fig_max_velocity, use_container_width=True)
    
    fig_max_meterage = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_max_meterage_min,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, 100], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, pct_max_meterage_min], 'color': "blue"},  # Blue for the percentage value
              {'range': [pct_max_meterage_min, 100], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_max_meterage.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>Mt/min<br><br><span style='font-size:1.8em'>{max_meterage_min}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col6.plotly_chart(fig_max_meterage, use_container_width=True)
    
    fig_max_acc_2_4 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_max_acc_2_4,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, 100], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, pct_max_acc_2_4], 'color': "blue"},  # Blue for the percentage value
              {'range': [pct_max_acc_2_4, 100], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_max_acc_2_4.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>N.E Acc 2-4 (m/s2)<br><br><span style='font-size:1.8em'>{max_acc_2_4}Ñ</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col1.plotly_chart(fig_max_acc_2_4, use_container_width=True)
    
    fig_max_dec_2_4 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_max_dec_2_4,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, 100], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, pct_max_dec_2_4], 'color': "blue"},  # Blue for the percentage value
              {'range': [pct_max_dec_2_4, 100], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_max_dec_2_4.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>N.E Dec 2-4 (m/s2)<br><br><span style='font-size:1.8em'>{max_dec_2_4}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col2.plotly_chart(fig_max_dec_2_4, use_container_width=True)
    
    fig_max_acc_mayor_4 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_max_acc_mayor_4,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, 100], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, pct_max_acc_mayor_4], 'color': "blue"},  # Blue for the percentage value
              {'range': [pct_max_acc_mayor_4, 100], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_max_acc_mayor_4.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>N.E Acc >4 (m/s2)<br><br><span style='font-size:1.8em'>{max_acc_mayor_4}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col3.plotly_chart(fig_max_acc_mayor_4, use_container_width=True)
    
    fig_max_dec_mayor_4 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_max_dec_mayor_4,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, 100], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, pct_max_dec_mayor_4], 'color': "blue"},  # Blue for the percentage value
              {'range': [pct_max_dec_mayor_4, 100], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_max_dec_mayor_4.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>N.E Dec >4 (m/s2)<br><br><span style='font-size:1.8em'>{max_dec_mayor_4}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col4.plotly_chart(fig_max_dec_mayor_4, use_container_width=True)
    
    fig_max_accelerations = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_max_accelerations,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, 100], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, pct_max_accelerations], 'color': "blue"},  # Blue for the percentage value
              {'range': [pct_max_accelerations, 100], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_max_accelerations.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>N.E Max Acc (m/s2)<br><br><span style='font-size:1.8em'>{max_accelerations}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col5.plotly_chart(fig_max_accelerations, use_container_width=True)
    
    fig_max_decelerations = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pct_max_decelerations,  # Percentage value
        number = {'suffix': " %"},
        gauge = {
            'axis': {'range': [0, 100], 'showticklabels': False, 'ticks': ''},
            'bar': {'color': "blue"},  # Semi-circle gauge
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
              {'range': [0, pct_max_decelerations], 'color': "blue"},  # Blue for the percentage value
              {'range': [pct_max_decelerations, 100], 'color': "lightgray"}  # Gray for the remainder
            ],  # Background
        },
    ))
    
    fig_max_decelerations.update_layout(
      title={
          'text': f"<span style='font-weight: normal;'>N.E Max Dec (m/s2)<br><br><span style='font-size:1.8em'>{max_decelerations}</span>",
          'y': 0.95,
          'x': 0.5,  # Center the title
          'xanchor': 'center',
          'yanchor': 'top',
          'font': {'size': 20}
      },
      margin=dict(t=10, b=0, l=0, r=0)  # Adjust margins for the title
      )

    col6.plotly_chart(fig_max_decelerations, use_container_width=True)
