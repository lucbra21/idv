import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def band5(df_selection):
    st.write("Velocity Band 5 (HIR)")

    total_distance = int(df_selection["Total Distance"].sum())
    band5_total_distance = int(df_selection["Velocity Band 5 Total Distance"].sum())
    total_pct_band5 = round((band5_total_distance/total_distance)*100, 2)
    band5_total_efforts = int(df_selection["Velocity Band 5 Total Effort Count"].sum())
    col1, col2, col3, col4 = st.columns(4)
        
    col1.subheader("Total Distance")
    col1.subheader(f"{total_distance} m")
    
    col2.subheader("Total Distance Band 5")
    col2.subheader(f"{band5_total_distance} m")
    
    col3.subheader("Distance (% Total)")
    col3.subheader(f"{total_pct_band5}")
    
    col4.subheader("Nº Esfuerzos")
    col4.subheader(f"{band5_total_efforts} m")


    total_distance_by_player = (
        df_selection.groupby("Apellido")["Velocity Band 5 Total Distance"].agg("sum")
    )
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Velocity Band 5 Total Distance",
        title="Distancia Banda 5 (17-21 km/h)",
        orientation="v",
        template="plotly_white",
        color_discrete_sequence=["green"],
        text=total_distance_by_player.values.astype(int)
    )
        
    relative_distance_trace = go.Scatter(
    x=total_distance_by_player.index,
    y=df_selection['Band5 %'],
    mode='lines+markers',
    name='Band5 %',
    line=dict(color='blue'),
    yaxis="y2"
    )
    
    fig_player_distance.update_layout(
    yaxis2=dict(
        title="Band5 %",
        overlaying="y",
        side="right"
    ),
    yaxis=dict(title="Velocity Band 5 Total Distance")
    )
    fig_player_distance.add_trace(relative_distance_trace)

    st.plotly_chart(fig_player_distance, use_container_width=True)
    