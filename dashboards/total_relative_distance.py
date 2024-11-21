import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def total_relative_distance(df_selection):
 
    st.write("Total & Relative Distance")

    left_col, mid_col, right_col = st.columns(3)  # Set the relative widths as needed
    
    total_distance = int(df_selection["Total Distance"].sum())
    average_distance = round(df_selection["Total Distance"].mean(), 1)
    average_relative_distance = round(df_selection["Relative Distance"].mean(), 1)

    left_col.subheader("Total Distance")
    left_col.subheader(f"{total_distance} m")
    
    mid_col.subheader("Avg Distance")
    mid_col.subheader(f"{average_distance} m")
    
    right_col.subheader("Avg Relative Distance")
    right_col.subheader(f"{average_relative_distance} m")


    total_distance_by_player = (
        df_selection.groupby("Apellido")["Total Distance"].agg("sum")
    )
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Total Distance",
        title="Total Distance",
        orientation="v",
        template="plotly_white",
        color_discrete_sequence=["green"],
        text=total_distance_by_player.values.astype(int)
    )
        
    relative_distance_trace = go.Scatter(
    x=total_distance_by_player.index,
    y=df_selection['Relative Distance'],
    mode='lines+markers',
    name='Relative Distance',
    line=dict(color='blue'),
    yaxis="y2"
    )
    
    fig_player_distance.update_layout(
    yaxis2=dict(
        title="Relative Distance",
        overlaying="y",
        side="right"
    ),
    yaxis=dict(title="Total Distance")
    )
    fig_player_distance.add_trace(relative_distance_trace)

    st.plotly_chart(fig_player_distance, use_container_width=True)