import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def player_load(df_selection):
    st.write("Player Load")

    left_col, right_col = st.columns(2)
    
    total_player_load = int(df_selection["Total Player Load"].sum())
    avg_player_load = int(df_selection["Total Player Load"].mean())
    total_player_load_per_min = int(df_selection["Player Load Per Minute"].sum())
    
    with right_col:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Total PL")
            st.subheader(f"{total_player_load}")
        with col2:
            st.subheader("Avg PL")
            st.subheader(f"{avg_player_load}")
        with col3:
            st.subheader("PL / Min")
            st.subheader(f"{total_player_load_per_min}")
    
    total_distance_by_player = (
        df_selection.groupby("Apellido")["Total Player Load"].agg("sum")
    )
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Total Player Load",
        title="Player Load vs Player Load/Minute",
        orientation="v",
        template="plotly_white",
        color_discrete_sequence=["green"],
        text=total_distance_by_player.values.astype(int)
    )
        
    relative_distance_trace = go.Scatter(
    x=total_distance_by_player.index,
    y=df_selection['Player Load Per Minute'],
    mode='lines+markers',
    name='Total Player Load',
    line=dict(color='blue'),
    yaxis="y2"
    )
    
    fig_player_distance.update_layout(
    yaxis2=dict(
        title="Player Load Per Minute",
        overlaying="y",
        side="right"
    ),
    yaxis=dict(title="Total Player Load per Minute")
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
        color_discrete_sequence=["green"],
        text_auto=True
    )
    
    right_col.plotly_chart(fig_player_distance, use_container_width=True)
