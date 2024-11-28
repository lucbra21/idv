import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def max_velocity(df_selection):
    st.header("Maximun Velocity")

    total_distance_by_player = (
        df_selection.groupby("Apellido")["Maximum Velocity"].agg("max").sort_values(ascending=False)
    )
    relative_distance_ordered = df_selection.set_index("Apellido").loc[
        total_distance_by_player.index, "Max Vel (% Max)"
    ]
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Maximum Velocity",
        title="Velocidad Maxima",
        orientation="v",
        template="plotly_white",
        color_discrete_sequence=["#118DFF"],
        text=total_distance_by_player.values.astype(int)
    )
        
    relative_distance_trace = go.Scatter(
    x=total_distance_by_player.index,
    y=relative_distance_ordered,
    mode='lines+markers+text',
    line=dict(color='#62B8FF'),
        text=relative_distance_ordered.round(2),  # Etiquetas numéricas redondeadas
        textposition="bottom center",
        textfont=dict(
        color="black",  # Color del texto
        size=14  # (Opcional) Tamaño del texto
        ),
    yaxis="y2"
    )
    
    fig_player_distance.update_layout(
        showlegend=False,
        yaxis2=dict(
            title=None,
            overlaying="y",
            side="right"
        ),
    yaxis=dict(title="Velocidad Maxima")
    )
    fig_player_distance.update_layout(
        title={
            'text': "Total Distance",        # Texto del título
            'x': 0.5,                       # Centrar horizontalmente
            'xanchor': 'center',            # Anclar al centro
            'yanchor': 'top'                # Anclar en la parte superior
        },
        yaxis_title=None,
        xaxis_title=None
    )
    fig_player_distance.update_traces(
        textfont_size=16,
    )
    fig_player_distance.add_trace(relative_distance_trace)

    st.plotly_chart(fig_player_distance, use_container_width=True)
    