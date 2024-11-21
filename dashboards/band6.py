import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def band6(df_selection):
    st.write("Velocity Band 6 (HSR)")

    total_distance = int(df_selection["Total Distance"].sum())
    band6_total_distance = int(df_selection["Velocity Band 6 Total Distance"].sum())
    total_pct_band6 = round((band6_total_distance/total_distance)*100, 2)
    band6_total_efforts = int(df_selection["Velocity Band 6 Total Effort Count"].sum())
    col1, col2, col3, col4 = st.columns(4)
        
    col1.subheader("Total Distance")
    col1.subheader(f"{total_distance} m")
    
    col2.subheader("Total Distance Band 6")
    col2.subheader(f"{band6_total_distance} m")
    
    col3.subheader("Distance (% Total)")
    col3.subheader(f"{total_pct_band6}")
    
    col4.subheader("Nº Esfuerzos")
    col4.subheader(f"{band6_total_efforts} m")


    total_distance_by_player = (
        df_selection.groupby("Apellido")["Velocity Band 6 Total Distance"].agg("sum")
    )
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Velocity Band 6 Total Distance",
        title="Distancia Banda 6 (22-25 km/h)",
        orientation="v",
        template="plotly_white",
        color_discrete_sequence=["green"],
        text=total_distance_by_player.values.astype(int)
    )
        
    relative_distance_trace = go.Scatter(
    x=total_distance_by_player.index,
    y=df_selection['Band6 %'],
    mode='lines+markers',
    name='Band6 %',
    line=dict(color='blue'),
    yaxis="y2"
    )
    
    fig_player_distance.update_layout(
    yaxis2=dict(
        title="Band6 %",
        overlaying="y",
        side="right"
    ),
    yaxis=dict(title="Velocity Band 6 Total Distance")
    )
    fig_player_distance.add_trace(relative_distance_trace)

    st.plotly_chart(fig_player_distance, use_container_width=True)
    