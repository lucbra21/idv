import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

def total_relative_distance(df_selection):
 
    st.header("Total & Relative Distance")

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
        df_selection.groupby("Apellido")["Total Distance"].agg("sum").sort_values(ascending=False)
    )
    relative_distance_ordered = df_selection.set_index("Apellido").loc[
        total_distance_by_player.index, "Relative Distance"
    ]
    fig_player_distance = px.bar(
        total_distance_by_player,
        x=total_distance_by_player.index,
        y="Total Distance",
        title="Total Distance",
        orientation="v",
        template="plotly_white",
        color_discrete_sequence=["#118DFF"],
        text=total_distance_by_player.values.astype(int)
    )
        
    relative_distance_trace = go.Scatter(
        x=total_distance_by_player.index,
        y=relative_distance_ordered,
        mode="lines+markers+text",  # Agrega texto
        line=dict(color="#62B8FF"),
        text=relative_distance_ordered.round(2),  # Etiquetas numéricas redondeadas
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
    yaxis=dict(title="Total Distance")
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