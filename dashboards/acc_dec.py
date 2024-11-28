import plotly.express as px
import streamlit as st

def acc_dec(df_selection):
    st.header("ACC & DEC")

    left_col, right_col = st.columns(2)
    
    acc_total_efforts = int(df_selection["Acceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    dec_total_efforts = int(df_selection["Deceleration B2-3 Average Efforts (Session) (Gen 2)"].sum())
    acc_dec = acc_total_efforts + dec_total_efforts
    
    with left_col:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Acc Total Efforts \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{acc_total_efforts}</text></h3>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Dec Total Efforts \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{dec_total_efforts}</text></h3>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Acc + Dec Total Efforts \n 
            <text style="font-size: 32px; text-align: center; color: #333; font-weight: bold;">{acc_dec}</text></h3>
            """, unsafe_allow_html=True)
    
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
        barmode="group",  # Aquí agrupamos las barras en lugar de apilarlas
        text_auto=True
    )
    fig_acc_dec.update_layout(
        title={
            'text': "Total Efforts",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    fig_acc_dec.update_traces(
        textfont=dict(
            color="white",  # Color del texto
            size=18  # (Opcional) Tamaño del texto
        )
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
        barmode="group",  # Aquí agrupamos las barras en lugar de apilarlas
        text_auto=True
    )
    fig_acc_dec_by_player.update_traces(
        textfont=dict(
            color="black",  # Color del texto
            size=18  # (Opcional) Tamaño del texto
        )
    )
    
    fig_acc_dec_by_player.update_layout(
        height=650,
        yaxis_title=None,
        title={
            'text': "Acc & Dec by Player Total Efforts",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
    )
    right_col.plotly_chart(fig_acc_dec_by_player, use_container_width=True)
