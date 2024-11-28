import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def band7(df_selection):
    st.header("Velocity Band 7 (Very High Speed Runnnig)")

    total_distance = int(df_selection["Total Distance"].sum())
    band7_total_distance = int(df_selection["Velocity Band 7 Total Distance"].sum()+df_selection["Velocity Band 8 Total Distance"].sum())
    total_pct_band7 = round((band7_total_distance/total_distance)*100, 2)
    band7_total_efforts = int(df_selection["Velocity Band 7 Total Effort Count"].sum())
    col1, col2, col3, col4 = st.columns(4)
        
    col1.subheader("Total Distance")
    col1.subheader(f"{total_distance} m")
    
    col2.subheader("Total Distance Band 7&8")
    col2.subheader(f"{band7_total_distance} m")
    
    col3.subheader("Distance (% Total)")
    col3.subheader(f"{total_pct_band7}")
    
    col4.subheader("Nº Esfuerzos")
    col4.subheader(f"{band7_total_efforts}")


    total_distance_by_player = (
        df_selection.groupby("Apellido")["Velocity Band 7 Total Distance"].agg("sum").sort_values(ascending=False)
    )
    
    relative_distance_ordered = df_selection.set_index("Apellido").loc[
        total_distance_by_player.index, "Band7 %"
    ]
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Velocity Band 7 Total Distance",
        title="Distancia Banda 7 (25-29 km/h)",
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
    text=relative_distance_ordered.round(2),
    textposition="top center",
    textfont=dict(
        color="black",  # Color del texto
        size=14  # (Opcional) Tamaño del texto
        ),
        yaxis="y2",
    )
    fig_player_distance.update_layout(
        showlegend=False,
        yaxis2=dict(
            title=None,
            overlaying="y",
            side="right"
        ),
    )
    fig_player_distance.update_layout(
        title={
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
    