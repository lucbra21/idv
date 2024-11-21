import plotly.express as px
import streamlit as st

def accelerations(df_selection):
    
    st.write("ACC")

    left_col, right_col = st.columns(2)
    
    acc_2ms = int(df_selection["Acceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    acc_2_4 = int(df_selection["Aceleraciones 2 a 4"].sum())
    acc_4 = int(df_selection["Aceleraciones mayores a 4"].sum())
    
    with left_col:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Acc (+2 m/s2)")
            st.subheader(f"{acc_2ms} m")
        with col2:
            st.subheader("Acc (2-4 m/s2)")
            st.subheader(f"{acc_2_4} m")
        with col3:
            st.subheader("Acc (+4 m/s2)")
            st.subheader(f"{acc_4} m")
    
    fig_acc = (
        df_selection.groupby("Dia")[["Acceleration B2-3 Average Efforts (Session) (Gen 2)",
                                    "AccMayoresGen2"]].agg("sum")
    )

    fig_acc = fig_acc.rename(columns={
        "Acceleration B2-3 Average Efforts (Session) (Gen 2)": "Acc",
        "AccMayoresGen2": "Acc Mayores Gen2",
    })

    fig_acc_reset = fig_acc.reset_index()

    fig_acc = px.bar(
        fig_acc_reset,
        x="Dia",  # Eje X basado en el día
        y=["Acc","Acc Mayores Gen2"],  # Múltiples bandas de velocidad en Y
        title="Acc (Nº Efforts)",
        labels={"value": "Num Efforts", "variable": "Acc & Dec"},
        template="plotly_white",
        barmode="group"  # Aquí agrupamos las barras en lugar de apilarlas
    )

    left_col.plotly_chart(fig_acc, use_container_width=True)
    
    fig_acc_by_player = (
        df_selection.groupby("Apellido")[["Acceleration B2-3 Average Efforts (Session) (Gen 2)",
                                    "AccMayoresGen2"]].agg("sum")
    )

    fig_acc_by_player = fig_acc_by_player.rename(columns={
        "Acceleration B2-3 Average Efforts (Session) (Gen 2)": "Acc",
        "AccMayoresGen2": "Acc Mayores Gen2",
    })

    fig_acc_by_player_reset = fig_acc_by_player.reset_index()

    fig_acc_by_player = px.bar(
        fig_acc_by_player_reset,
        x=["Acc","Acc Mayores Gen2"],  # Eje X basado en el día
        y="Apellido",  # Múltiples bandas de velocidad en Y
        title="Acc & Dec (Nº Efforts)",
        labels={"value": "Num Efforts", "variable": "Acc & Dec"},
        template="plotly_white",
        barmode="group"  # Aquí agrupamos las barras en lugar de apilarlas
    )
    
    fig_acc_by_player.update_layout(height=650)
    right_col.plotly_chart(fig_acc_by_player, use_container_width=True)
    