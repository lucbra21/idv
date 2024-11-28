import plotly.express as px
import streamlit as st

def decelerations(df_selection):
    
    st.header("Desaceleraciones")

    left_col, right_col = st.columns(2)
    
    dec_2ms = int(df_selection["Deceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    dec_2_4 = int(df_selection["Desaceleraciones 2 a 4"].sum())
    dec_4 = int(df_selection["Desaceleraciones mayores a 4"].sum())
    
    with left_col:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Dec (+2 m/s2) \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{dec_2ms}</text></h3>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Dec (2-4 m/s2) \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{dec_2_4}</text></h3>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Dec (+4 m/s2) \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{dec_4}</text></h3>
            """, unsafe_allow_html=True)
    
    fig_dec = (
        df_selection.groupby("Dia")[["Desaceleraciones 2 a 4",
                                    "Desaceleraciones mayores a 4"]].agg("sum")
    )

    fig_dec_reset = fig_dec.reset_index()

    fig_dec = px.bar(
        fig_dec_reset,
        x="Dia",  # Eje X basado en el día
        y=["Desaceleraciones 2 a 4","Desaceleraciones mayores a 4"],  # Múltiples bandas de velocidad en Y
        title="Dec (Nº Efforts)",
        labels={"value": "Num Efforts", "variable": "Dec"},
        template="plotly_white",
        barmode="group",  # Aquí agrupamos las barras en lugar de apilarlas
        text_auto=True
    )
    fig_dec.update_layout(
        title={
            'text': "Dec (Nº Efforts)",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    
    fig_dec.update_traces(
        textfont=dict(
            color="black",  # Color del texto
            size=18  # (Opcional) Tamaño del texto
        )
    )

    left_col.plotly_chart(fig_dec, use_container_width=True)
    
    fig_dec_by_player = (
        df_selection.groupby("Apellido")[["Desaceleraciones 2 a 4",
                                    "Desaceleraciones mayores a 4"]].agg("sum")
    )

    fig_dec_by_player_reset = fig_dec_by_player.reset_index()

    fig_dec_by_player = px.bar(
        fig_dec_by_player_reset,
        x=["Desaceleraciones 2 a 4","Desaceleraciones mayores a 4"],  # Eje X basado en el día
        y="Apellido",  # Múltiples bandas de velocidad en Y
        title="Dec (Nº Efforts)",
        labels={"value": "Num Efforts", "variable": "Acc & Dec"},
        template="plotly_white",
        barmode="group",  # Aquí agrupamos las barras en lugar de apilarlas
        text_auto=True
    )
    fig_dec_by_player.update_traces(
        textfont=dict(
            color="black",  # Color del texto
            size=18  # (Opcional) Tamaño del texto
        )
    )
    
    fig_dec_by_player.update_layout(
        height=650,
        yaxis_title=None,
        title={
            'text': "Dec Player (Nº Efforts)",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
    )
    fig_dec_by_player.update_layout(height=650)
    right_col.plotly_chart(fig_dec_by_player, use_container_width=True)