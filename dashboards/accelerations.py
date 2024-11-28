import plotly.express as px
import streamlit as st

def accelerations(df_selection):
    
    st.header("Acelerations")

    left_col, right_col = st.columns(2)
    
    acc_2ms = int(df_selection["Acceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    acc_2_4 = int(df_selection["Aceleraciones 2 a 4"].sum())
    acc_4 = int(df_selection["Aceleraciones mayores a 4"].sum())
    
    with left_col:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Acc (+2 m/s2) \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{acc_2ms}</text></h3>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Acc (2-4 m/s2) \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{acc_2_4}</text></h3>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Acc (+4 m/s2) \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{acc_4}</text></h3>
            """, unsafe_allow_html=True)
    
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
        barmode="group",  # Aquí agrupamos las barras en lugar de apilarlas
        text_auto=True
    )
    
    fig_acc.update_layout(
        title={
            'text': "Acc (Nº Efforts)",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    
    fig_acc.update_traces(
        textfont=dict(
            color="white",  # Color del texto
            size=18  # (Opcional) Tamaño del texto
        )
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
        barmode="group",  # Aquí agrupamos las barras en lugar de apilarlas
        text_auto=True
    )
    fig_acc_by_player.update_traces(
        textfont=dict(
            color="black",  # Color del texto
            size=18  # (Opcional) Tamaño del texto
        )
    )
    
    fig_acc_by_player.update_layout(
        height=650,
        yaxis_title=None,
        title={
            'text': "Acc Player (Nº Efforts)",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
    )
    
    fig_acc_by_player.update_layout(height=650)
    right_col.plotly_chart(fig_acc_by_player, use_container_width=True)
    