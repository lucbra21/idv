import plotly.express as px
import streamlit as st

def hsr_vhsr(df_selection):
    
    st.write("HSR & VHSR")

    left_col, right_col = st.columns(2)
    
    total_distance = int(df_selection["Total Distance"].sum())
    total_hsr = int(df_selection["Dist +17 km/h"].sum())
    avg_hsr = int(df_selection["Dist +17 km/h"].mean())
    hsr_pct = round((total_hsr/total_distance)*100, 1)
    
    total_vhsr = int(df_selection["Dist +25 km/h"].sum())
    avg_vhsr = int(df_selection["Dist +25 km/h"].mean())
    vhsr_pct = round((total_vhsr/total_distance)*100, 1)
    
    with left_col:
        col1, col2, col3,col4, col5, col6 = st.columns(6)
        with col1:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Total HSR \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{total_hsr} m</text></h3>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Avg HSR \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{avg_hsr} m</text></h3>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">HSR % \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{hsr_pct} %</text></h3>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <h3 style="font-size: 22px; text-align: center; color: #333;">Total VHSR \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{total_vhsr} m</text></h3>
            """, unsafe_allow_html=True)
        with col5:
            st.markdown(f"""
            <h3 style="font-size: 22px; text-align: center; color: #333;">Avg VHSR \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{avg_vhsr} m</text></h3>
            """, unsafe_allow_html=True)
        with col6:
            st.markdown(f"""
            <h3 style="font-size: 22px; text-align: center; color: #333;">VHSR % \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{vhsr_pct} %</text></h3>
            """, unsafe_allow_html=True)
    
    fig_hsr_vhsr = (
        df_selection.groupby("Dia")[["Dist +17 km/h","Dist +25 km/h"]].agg("sum")
    )
    
    fig_hsr_vhsr = fig_hsr_vhsr.rename(columns={
        "Dist +17 km/h": "HSR",
        "Dist +25 km/h": "VHSR",
    })

    fig_hsr_vhsr_reset = fig_hsr_vhsr.reset_index()

    fig_hsr_vhsr = px.bar(
        fig_hsr_vhsr_reset,
        x="Dia",  # Eje X basado en el día
        y=["HSR","VHSR"],  # Múltiples bandas de velocidad en Y
        title="HSR & VHSR",
        labels={"value": "Distance", "variable": "HSR & VHSR"},
        template="plotly_white",
        barmode="group",  # Aquí agrupamos las barras en lugar de apilarlas
        text_auto=".0f"
    )
    
    fig_hsr_vhsr.update_layout(
        title={
            'text': "HSR & VHSR",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    fig_hsr_vhsr.update_traces(
        textfont=dict(
            color="black",  # Color del texto
            size=18  # (Opcional) Tamaño del texto
        )
    )

    left_col.plotly_chart(fig_hsr_vhsr, use_container_width=True)
    
    fig_hsr_vhsr_by_player = (
        df_selection.groupby("Apellido")[["Dist +17 km/h","Dist +25 km/h"]].agg("sum")
    )
    
    fig_hsr_vhsr_by_player = fig_hsr_vhsr_by_player.rename(columns={
        "Dist +17 km/h": "HSR",
        "Dist +25 km/h": "VHSR",
    })

    fig_hsr_vhsr_by_player_reset = fig_hsr_vhsr_by_player.reset_index()

    fig_hsr_vhsr_by_player = px.bar(
        fig_hsr_vhsr_by_player_reset,
        x=["HSR","VHSR"],  # Eje X basado en el día
        y="Apellido",  # Múltiples bandas de velocidad en Y
        title="HSE & VHSR",
        labels={"value": "Num Efforts", "variable": "Acc & Dec"},
        template="plotly_white",
        barmode="group",  # Aquí agrupamos las barras en lugar de apilarlas
        text_auto=".0f"
    )
    fig_hsr_vhsr_by_player.update_traces(
        textfont=dict(
            color="black",  # Color del texto
            size=18  # (Opcional) Tamaño del texto
        )
    )
    
    fig_hsr_vhsr_by_player.update_layout(
        height=650,
        yaxis_title=None,
        title={
            'text': "HSR % VHSR by Player",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
    )
    
    right_col.plotly_chart(fig_hsr_vhsr_by_player, use_container_width=True)
