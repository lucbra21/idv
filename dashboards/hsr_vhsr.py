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
            st.subheader("Total HSR")
            st.subheader(f"{total_hsr} m")
        with col2:
            st.subheader("Avg HSR")
            st.subheader(f"{avg_hsr} m")
        with col3:
            st.subheader("HSR %")
            st.subheader(f"{hsr_pct}")
        with col4:
            st.subheader("Total VHSR")
            st.subheader(f"{total_vhsr} m")
        with col5:
            st.subheader("Avg VHSR")
            st.subheader(f"{avg_vhsr} m")
        with col6:
            st.subheader("VHSR %")
            st.subheader(f"{vhsr_pct}")
    
    fig_acc = (
        df_selection.groupby("Dia")[["Dist +17 km/h","Dist +25 km/h"]].agg("sum")
    )
    
    fig_acc = fig_acc.rename(columns={
        "Dist +17 km/h": "HSR",
        "Dist +25 km/h": "VHSR",
    })

    fig_acc_reset = fig_acc.reset_index()

    fig_acc = px.bar(
        fig_acc_reset,
        x="Dia",  # Eje X basado en el día
        y=["HSR","VHSR"],  # Múltiples bandas de velocidad en Y
        title="HSE & VHSR",
        template="plotly_white",
        barmode="group"  # Aquí agrupamos las barras en lugar de apilarlas
    )

    left_col.plotly_chart(fig_acc, use_container_width=True)
    
    fig_dec_by_player = (
        df_selection.groupby("Apellido")[["Dist +17 km/h","Dist +25 km/h"]].agg("sum")
    )
    
    fig_dec_by_player = fig_dec_by_player.rename(columns={
        "Dist +17 km/h": "HSR",
        "Dist +25 km/h": "VHSR",
    })

    fig_dec_by_player_reset = fig_dec_by_player.reset_index()

    fig_dec_by_player = px.bar(
        fig_dec_by_player_reset,
        x=["HSR","VHSR"],  # Eje X basado en el día
        y="Apellido",  # Múltiples bandas de velocidad en Y
        title="HSE & VHSR)",
        template="plotly_white",
        barmode="group"  # Aquí agrupamos las barras en lugar de apilarlas
    )
    
    fig_dec_by_player.update_layout(height=650)
    right_col.plotly_chart(fig_dec_by_player, use_container_width=True)
