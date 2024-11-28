import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def player_load(df_selection):
    st.header("Player Load")

    left_col, right_col = st.columns(2)
    
    total_player_load = int(df_selection["Total Player Load"].sum())
    avg_player_load = int(df_selection["Total Player Load"].mean())
    total_player_load_per_min = int(df_selection["Player Load Per Minute"].sum())
    
    with right_col:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Total PL \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{total_player_load} m</text></h3>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">Avg PL \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{avg_player_load} m</text></h3>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <h3 style="font-size: 24px; text-align: center; color: #333;">PL / Min \n 
            <text style="font-size: 30px; text-align: center; color: #333; font-weight: bold;">{total_player_load_per_min} m</text></h3>
            """, unsafe_allow_html=True)
    
    total_distance_by_player = (
        df_selection.groupby("Apellido")["Total Player Load"].agg("sum").sort_values(ascending=False)
    )
    
    relative_distance_ordered = df_selection.set_index("Apellido").loc[
        total_distance_by_player.index, "Player Load Per Minute"
    ]
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Total Player Load",
        title="Player Load vs Player Load/Minute",
        orientation="v",
        template="plotly_white",
        color_discrete_sequence=["#118DFF"],
        text=total_distance_by_player.values.astype(int)
    )
        
    relative_distance_trace = go.Scatter(
        x=total_distance_by_player.index,
        y=relative_distance_ordered,
        mode='lines+markers+text',
        name='PL per Minute',
        line=dict(color='#62B8FF'),
        text=relative_distance_ordered.round(1),  # Etiquetas numéricas redondeadas
        textposition="top center",
        textfont=dict(
            color="black",  # Color del texto
            size=10  # (Opcional) Tamaño del texto
        ),
        yaxis="y2",
    )
    
    fig_player_distance.update_layout(
    yaxis2=dict(
        title=None,
        overlaying="y",
        side="right"
    ),
    )
    fig_player_distance.update_layout(
        title={
            'text': "Player Load vs Player Load/Minute",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        xaxis_title=None
    )
    fig_player_distance.add_trace(relative_distance_trace)

    left_col.plotly_chart(fig_player_distance, use_container_width=True)
    
    total_distance_by_player = (
        df_selection.groupby("Dia")["Total Player Load"].agg("sum")
    )
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Total Player Load",
        title="Total Player Load",
        orientation="v",
        template="plotly_white",
        color_discrete_sequence=["#118DFF"],
        text_auto='.2f'
    )
    fig_player_distance.update_layout(
        title={
            'text': "Total Player Load",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
    )
    fig_player_distance.update_traces(
        textfont=dict(
            color="white",  # Color del texto
            size=18  # (Opcional) Tamaño del texto
        )
    )
    fig_player_distance.update_xaxes(
        tickmode="linear",
        dtick=1   # Interval of 1 between ticks
    )
    
    right_col.plotly_chart(fig_player_distance, use_container_width=True)
