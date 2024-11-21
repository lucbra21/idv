import plotly.express as px
import streamlit as st

def acc_dec(df_selection):
    st.write("ACC & DEC")

    left_col, right_col = st.columns(2)
    
    acc_total_efforts = int(df_selection["Acceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    dec_total_efforts = int(df_selection["Deceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    acc_dec = acc_total_efforts + dec_total_efforts
    
    with left_col:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Acc Total Efforts")
            st.subheader(f"{acc_total_efforts} m")
        with col2:
            st.subheader("Dec Total Efforts")
            st.subheader(f"{dec_total_efforts} m")
        with col3:
            st.subheader("Acc + Dec Total Efforts")
            st.subheader(f"{acc_dec} m")
    
    fig_acc_dec = (
        df_selection.groupby("Dia")[["Acceleration B2-3 Average Efforts (Session) (Gen 2)",
                                    "Deceleration B2-3 Average Efforts (Session) (Gen 2)"]].agg("sum")
    )

    fig_acc_dec = fig_acc_dec.rename(columns={
        "Acceleration B2-3 Average Efforts (Session) (Gen 2)": "Acc",
        "Deceleration B2-3 Average Efforts (Session) (Gen 2)": "Dec",
    })

    fig_acc_dec_reset = fig_acc_dec.reset_index()

    fig_acc_dec = px.bar(
        fig_acc_dec_reset,
        x="Dia",  # Eje X basado en el día
        y=["Acc","Dec"],  # Múltiples bandas de velocidad en Y
        title="Acc & Dec (Nº Efforts)",
        labels={"value": "Num Efforts", "variable": "Acc & Dec"},
        template="plotly_white",
        barmode="group"  # Aquí agrupamos las barras en lugar de apilarlas
    )

    left_col.plotly_chart(fig_acc_dec, use_container_width=True)
    
    fig_acc_dec_by_player = (
        df_selection.groupby("Apellido")[["Acceleration B2-3 Average Efforts (Session) (Gen 2)",
                                    "Deceleration B2-3 Average Efforts (Session) (Gen 2)"]].agg("sum")
    )

    fig_acc_dec_by_player = fig_acc_dec_by_player.rename(columns={
        "Acceleration B2-3 Average Efforts (Session) (Gen 2)": "Acc",
        "Deceleration B2-3 Average Efforts (Session) (Gen 2)": "Dec",
    })

    fig_acc_dec_by_player_reset = fig_acc_dec_by_player.reset_index()

    fig_acc_dec_by_player = px.bar(
        fig_acc_dec_by_player_reset,
        x=["Acc","Dec"],  # Eje X basado en el día
        y="Apellido",  # Múltiples bandas de velocidad en Y
        title="Acc & Dec (Nº Efforts)",
        labels={"value": "Num Efforts", "variable": "Acc & Dec"},
        template="plotly_white",
        barmode="group"  # Aquí agrupamos las barras en lugar de apilarlas
    )
    
    fig_acc_dec_by_player.update_layout(height=650)
    right_col.plotly_chart(fig_acc_dec_by_player, use_container_width=True)
