import plotly.express as px
import streamlit as st

def resumen_semanal(df_selection):
    # Aquí muestra los gráficos o estadísticas que se relacionen con el resumen general
    st.write("Dashboard: Resumen por Semana")
    
    total_distance = int(df_selection["Total Distance"].sum())
    average_distance = round(df_selection["Total Distance"].mean(), 1)
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
            st.subheader("Total Distance")
            st.subheader(f"{total_distance} m")
        with col2:
            st.subheader("Avg Distance")
            st.subheader(f"{average_distance} m")

    with mid_col:
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Total HIR")
            st.subheader(f"{total_hir} m")
        with col4:
            st.subheader("Avg HIR")
            st.subheader(f"{average_hir} m")

    with right_col:
        col5, col6, col7 = st.columns(3)
        with col5:
            st.subheader("Total HSR")
            st.subheader(f"{total_hsr} m")
        with col6:
            st.subheader("Avg HSR")
            st.subheader(f"{average_hsr} m")
        with col7:
            st.subheader("% HSR")
            st.subheader(f"{pct_hsr} %")

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
        text_auto=True
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
        text_auto=True
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
        text_auto=True
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
            st.subheader("B5")
            st.subheader(f"{b5_total_distance} m")
        with col2:
            st.subheader("B6")
            st.subheader(f"{b6_total_distance} m")
        with col3:
            st.subheader("B7")
            st.subheader(f"{b7_total_distance} m")
        with col4:
            st.subheader("B8")
            st.subheader(f"{b8_total_distance} m")
    
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
        labels={"value": "TD by Velocity Bands"},
        template="plotly_white",
        barmode="group"  # Agrupado, no apilado
    )

    left_col.plotly_chart(fig_velocity_bands_plot, use_container_width=True)

    acc_total_efforts = int(df_selection["Acceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    dec_total_efforts = int(df_selection["Deceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    acc_mean_efforts = int(df_selection["Acceleration B2-3 Average Efforts (Session) (Gen 2)"].mean())
    dec_mean_efforts = int(df_selection["Deceleration B2-3 Average Efforts (Session) (Gen 2)"].mean())
    
    with mid_col:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.subheader("Acc Total Efforts")
            st.subheader(f"{acc_total_efforts} m")
        with col2:
            st.subheader("Acc Avg Efforts")
            st.subheader(f"{acc_mean_efforts} m")
        with col3:
            st.subheader("Dec Total Efforts")
            st.subheader(f"{dec_total_efforts} m")
        with col4:
            st.subheader("Dec Avg Efforts")
            st.subheader(f"{dec_mean_efforts} m")

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
        barmode="group"  # Aquí agrupamos las barras en lugar de apilarlas
    )

    mid_col.plotly_chart(fig_acc_dec, use_container_width=True)

    total_vhsr = int(df_selection["VHSR"].sum())
    average_vhsr = round(df_selection["VHSR"].mean(), 1)
    pct_vhsr = round(df_selection["VHSR %"].sum(), 2)
    
    with right_col:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Total VHSR")
            st.subheader(f"{total_vhsr} m")
        with col2:
            st.subheader("Avg VHSR")
            st.subheader(f"{average_vhsr} m")
        with col3:
            st.subheader("% VHSR")
            st.subheader(f"{pct_vhsr} %")
    
    total_vhsr_distance_by_player = (
        df_selection.groupby("Semana")["VHSR"].agg("sum")
    )
    fig_vhsr_distance = px.bar(
        total_vhsr_distance_by_player,
        x=total_vhsr_distance_by_player.index,
        y="VHSR",
        title="VHSR Distance",
        orientation="v",
        template="plotly_white"
    )

    right_col.plotly_chart(fig_vhsr_distance, use_container_width=True)