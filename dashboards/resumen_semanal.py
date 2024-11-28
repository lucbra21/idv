import plotly.express as px
import streamlit as st

def resumen_semanal(df_selection):
      # Aquí muestra los gráficos o estadísticas que se relacionen con el resumen general
    st.header("Resumen Semanal")
    
    total_distance = int(df_selection["Total Distance"].sum())
    average_distance = int(df_selection["Total Distance"].mean())
    total_hir = int(df_selection["Dist +17 km/h"].sum())
    average_hir = round(df_selection["Dist +17 km/h"].mean(), 1)
    total_hsr = int(df_selection["Velocity Band 6 Total Distance"].sum())
    average_hsr = round(df_selection["Velocity Band 6 Total Distance"].mean(), 1)
    pct_hsr = round(df_selection["HSR %"].sum(), 2)

    # Create 3 main columns: left_col, mid_col, right_col
    left_col, mid_col, right_col = st.columns([2, 2, 3])  # Set the relative widths as needed

    # Now subdivide each main column into smaller columns
    with left_col:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Total Distance \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{total_distance} m</text></h3>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Average Distance \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{average_distance} m</text></h3>
            """, unsafe_allow_html=True)
    with mid_col:
        col3, col4 = st.columns(2)
        with col3:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Total HIR \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{total_hir} m</text></h3>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Avg HIR \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{average_hir} m</text></h3>
            """, unsafe_allow_html=True)
    with right_col:
        col5, col6, col7 = st.columns(3)
        with col5:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Total HSR \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{total_hsr} m</text></h3>
            """, unsafe_allow_html=True)
        with col6:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Avg HSR \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{average_hsr} m</text></h3>
            """, unsafe_allow_html=True)
        with col7:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">% HSR \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{pct_hsr} m</text></h3>
            """, unsafe_allow_html=True)

    # Plotting graphs within the main columns
    total_distance_by_player = (
        df_selection.groupby("Semana")["Total Distance"].agg("sum")
    )
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Total Distance",
        title="Total Distance",
        orientation="v",
        template="plotly_white",
        color_discrete_sequence=["green"],
        text_auto='.0f'
    )
    fig_player_distance.update_traces(
        textfont_size=18,
    )
    fig_player_distance.update_layout(
        title={
            'text': "Total Distance",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    
    fig_player_distance.update_xaxes(
        tickmode="linear",
        dtick=1   # Interval of 1 between ticks
    )
    
    fig_player_distance.update_yaxes(
        showticklabels=False   # Ocultar etiquetas del eje X
    )

    total_hi_distance_by_player = (
        df_selection.groupby("Semana")["Dist +17 km/h"].agg("sum")
    )
    fig_hi_distance = px.bar(
        total_hi_distance_by_player,
        x=total_hi_distance_by_player.index,
        y="Dist +17 km/h",
        title="HI Distance",
        orientation="v",
        template="plotly_white",
        text_auto='.0f'
    )
    fig_hi_distance.update_traces(
        textfont_size=18,
    )
    fig_hi_distance.update_layout(
        title={
            'text': "HI Total Distance",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    
    fig_hi_distance.update_xaxes(
        tickmode="linear",
        dtick=1   # Interval of 1 between ticks
    )

    total_hsr_distance_by_player = (
        df_selection.groupby("Semana")["Velocity Band 6 Total Distance"].agg("sum")
    )
    fig_hsr_distance = px.bar(
        total_hsr_distance_by_player,
        x=total_hsr_distance_by_player.index,
        y="Velocity Band 6 Total Distance",
        title="HSR Distance",
        orientation="v",
        template="plotly_white",
        text_auto=".0f"
    )
    fig_hsr_distance.update_traces(
        textfont_size=18,
    )
    fig_hsr_distance.update_layout(
        title={
            'text': "HSR Total Distance",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    
    fig_hsr_distance.update_xaxes(
        tickmode="linear",
        dtick=1   # Interval of 1 between ticks
    )

    # Plot the charts in the larger layout columns
    left_col.plotly_chart(fig_player_distance, use_container_width=True)
    mid_col.plotly_chart(fig_hi_distance, use_container_width=True)
    right_col.plotly_chart(fig_hsr_distance, use_container_width=True)

    b5_total_distance = int(df_selection["Velocity Band 5 Total Distance"].sum())
    b6_total_distance = int(df_selection["Velocity Band 6 Total Distance"].sum())
    b7_total_distance = int(df_selection["Velocity Band 7 Total Distance"].sum())
    b8_total_distance = int(df_selection["Velocity Band 8 Total Distance"].sum())
    
    with left_col:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">B5 \n 
            <text style="font-size: 26px; text-align: center; color: #333; font-weight: bold;">{b5_total_distance} m</text></h3>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">B6 \n 
            <text style="font-size: 26px; text-align: center; color: #333; font-weight: bold;">{b6_total_distance} m</text></h3>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">B7 \n 
            <text style="font-size: 26px; text-align: center; color: #333; font-weight: bold;">{b7_total_distance} m</text></h3>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">B8 \n 
            <text style="font-size: 26px; text-align: center; color: #333; font-weight: bold;">{b8_total_distance} m</text></h3>
            """, unsafe_allow_html=True)
    
    fig_velocity_bands = (
        df_selection.groupby("Semana")[["Velocity Band 5 Total Distance", "Velocity Band 6 Total Distance",
                                    "Velocity Band 7 Total Distance", "Velocity Band 8 Total Distance"]].agg("sum")
    )

    fig_velocity_bands = fig_velocity_bands.rename(columns={
        "Velocity Band 5 Total Distance": "B5",
        "Velocity Band 6 Total Distance": "B6",
        "Velocity Band 7 Total Distance": "B7",
        "Velocity Band 8 Total Distance": "B8"
    })

    fig_velocity_bands_reset = fig_velocity_bands.reset_index()

    fig_velocity_bands_plot = px.bar(
        fig_velocity_bands_reset,
        x="Semana",
        y=["B5", "B6", "B7", "B8"],  # Nuevos nombres abreviados
        title="Total Distance by Velocity Bands",
        labels={"value": "TD by Velocity Bands", "variable": "Velocity Bands"},
        template="plotly_white",
        barmode="group",
        text_auto=".0f"
    )
    fig_velocity_bands_plot.update_traces(
        textfont_size=12,
        textangle=0 
    )
    
    fig_velocity_bands_plot.update_layout(
        title={
            'text': "Total Distance by Velocity Bands",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    
    fig_velocity_bands_plot.update_xaxes(
        tickmode="linear",
        dtick=1   # Interval of 1 between ticks
    )

    left_col.plotly_chart(fig_velocity_bands_plot, use_container_width=True)

    acc_total_efforts = int(df_selection["Acceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    dec_total_efforts = int(df_selection["Deceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    acc_mean_efforts = int(df_selection["Acceleration B2-3 Average Efforts (Session) (Gen 2)"].mean())
    dec_mean_efforts = int(df_selection["Deceleration B2-3 Average Efforts (Session) (Gen 2)"].mean())
    
    with mid_col:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
            <h3 style="font-size: 20px; text-align: center; color: #333;">Acc T.Eff \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{acc_total_efforts}</text></h3>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <h3 style="font-size: 20px; text-align: center; color: #333;">Acc AvEff \n 
            <text style="font-size: 30x; text-align: center; color: #333; font-weight: bold;">{acc_mean_efforts}</text></h3>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <h3 style="font-size: 20px; text-align: center; color: #333;">Dec T.Eff \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{dec_total_efforts}</text></h3>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <h3 style="font-size: 20px; text-align: center; color: #333;">Dec AvEff \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{dec_mean_efforts}</text></h3>
            """, unsafe_allow_html=True)

    fig_acc_dec = (
        df_selection.groupby("Semana")[["Acceleration B2-3 Average Efforts (Session) (Gen 2)",
                                    "Deceleration B2-3 Average Efforts (Session) (Gen 2)"]].agg("sum")
    )

    fig_acc_dec = fig_acc_dec.rename(columns={
        "Acceleration B2-3 Average Efforts (Session) (Gen 2)": "Acc",
        "Deceleration B2-3 Average Efforts (Session) (Gen 2)": "Dec",
    })

    fig_acc_dec_reset = fig_acc_dec.reset_index()

    fig_acc_dec = px.bar(
        fig_acc_dec_reset,
        x="Semana",  # Eje X basado en el día
        y=["Acc","Dec"],  # Múltiples bandas de velocidad en Y
        title="Acc & Dec (Nº Efforts)",
        labels={"value": "Num Efforts", "variable": "Acc & Dec"},
        template="plotly_white",
        barmode="group",  # Aquí agrupamos las barras en lugar de apilarlas
        text_auto=".0f"
    )
    
    fig_acc_dec.update_traces(
        textfont_color="white",
        textfont_size=18,
        textangle=0 
    )
    
    fig_acc_dec.update_layout(
        title={
            'text': "Acc & Dec (Nº Efforts)",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    
    fig_acc_dec.update_xaxes(
        tickmode="linear",
        dtick=1   # Interval of 1 between ticks
    )


    mid_col.plotly_chart(fig_acc_dec, use_container_width=True)

    total_vhsr = int(df_selection["VHSR"].sum())
    average_vhsr = round(df_selection["VHSR"].mean(), 1)
    pct_vhsr = round(df_selection["VHSR %"].sum(), 2)
    
    with right_col:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Total VHSR \n 
            <text style="font-size: 26px; text-align: center; color: #333; font-weight: bold;">{total_vhsr}</text></h3>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Avg VHSR \n 
            <text style="font-size: 26px; text-align: center; color: #333; font-weight: bold;">{average_vhsr}</text></h3>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">% VHSR \n 
            <text style="font-size: 26px; text-align: center; color: #333; font-weight: bold;">{pct_vhsr}</text></h3>
            """, unsafe_allow_html=True)
    
    total_vhsr_distance_by_player = (
        df_selection.groupby("Semana")["VHSR"].agg("sum")
    )
    fig_vhsr_distance = px.bar(
        total_vhsr_distance_by_player,
        x=total_vhsr_distance_by_player.index,
        y="VHSR",
        title="VHSR Distance",
        orientation="v",
        template="plotly_white",
        text_auto=".0f"
    )
    fig_vhsr_distance.update_traces(
        textfont_size=18,
        textangle=0 
    )
    
    fig_vhsr_distance.update_layout(
        title={
            'text': "VHSR Total Distance",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    
    fig_vhsr_distance.update_xaxes(
        tickmode="linear",
        dtick=1   # Interval of 1 between ticks
    )

    right_col.plotly_chart(fig_vhsr_distance, use_container_width=True)