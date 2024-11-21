import plotly.express as px
import streamlit as st

def decelerations(df_selection):
    
    st.write("DEC")

    left_col, right_col = st.columns(2)
    
    dec_2ms = int(df_selection["Deceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    dec_2_4 = int(df_selection["Desaceleraciones 2 a 4"].sum())
    dec_4 = int(df_selection["Desaceleraciones mayores a 4"].sum())
    
    with left_col:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Dec (+2 m/s2)")
            st.subheader(f"{dec_2ms} m")
        with col2:
            st.subheader("Dec (2-4 m/s2)")
            st.subheader(f"{dec_2_4} m")
        with col3:
            st.subheader("Dec (+4 m/s2)")
            st.subheader(f"{dec_4} m")
    
    fig_acc = (
        df_selection.groupby("Dia")[["Desaceleraciones 2 a 4",
                                    "Desaceleraciones mayores a 4"]].agg("sum")
    )

    fig_acc_reset = fig_acc.reset_index()

    fig_acc = px.bar(
        fig_acc_reset,
        x="Dia",  # Eje X basado en el día
        y=["Desaceleraciones 2 a 4","Desaceleraciones mayores a 4"],  # Múltiples bandas de velocidad en Y
        title="Dec (Nº Efforts)",
        labels={"value": "Num Efforts", "variable": "Dec"},
        template="plotly_white",
        barmode="group"  # Aquí agrupamos las barras en lugar de apilarlas
    )

    left_col.plotly_chart(fig_acc, use_container_width=True)
    
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
        barmode="group"  # Aquí agrupamos las barras en lugar de apilarlas
    )
    
    fig_dec_by_player.update_layout(height=650)
    right_col.plotly_chart(fig_dec_by_player, use_container_width=True)