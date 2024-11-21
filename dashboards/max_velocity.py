import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def max_velocity(df_selection):
    st.write("Maximun Velocity")

    total_distance_by_player = (
        df_selection.groupby("Apellido")["Maximum Velocity"].agg("max")
    )
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Maximum Velocity",
        title="Velocidad Maxima",
        orientation="v",
        template="plotly_white",
        color_discrete_sequence=["green"],
        text=total_distance_by_player.values.astype(int)
    )
        
    relative_distance_trace = go.Scatter(
    x=total_distance_by_player.index,
    y=df_selection['Max Vel (% Max)'],
    mode='lines+markers',
    name='Band7 %',
    line=dict(color='blue'),
    yaxis="y2"
    )
    
    fig_player_distance.update_layout(
    yaxis2=dict(
        title="Max Vel (% Max)",
        overlaying="y",
        side="right"
    ),
    yaxis=dict(title="Velocidad Maxima")
    )
    fig_player_distance.add_trace(relative_distance_trace)

    st.plotly_chart(fig_player_distance, use_container_width=True)
    