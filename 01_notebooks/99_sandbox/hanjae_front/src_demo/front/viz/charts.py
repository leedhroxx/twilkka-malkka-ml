import plotly.graph_objects as go


def make_trend_chart(monthly_trend: dict) -> go.Figure:
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=monthly_trend["months"],
            y=monthly_trend["이탈률"],
            mode="lines+markers",
            name="이탈률(주지표)",
            line=dict(color="#FF0A16", width=4),
            marker=dict(size=7, color="#FF0A16"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=monthly_trend["months"],
            y=monthly_trend["시청감소율"],
            mode="lines+markers",
            name="시청감소율(보조지표)",
            line=dict(color="#3B82F6", width=3),
            marker=dict(size=6, color="#3B82F6"),
            opacity=0.85,
        )
    )

    fig.update_layout(
        height=380,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.05,
            xanchor="left",
            x=0,
            font=dict(color="#E5E7EB"),
        ),
        xaxis=dict(
            showgrid=False,
            tickfont=dict(color="#D1D5DB"),
        ),
        yaxis=dict(
            title=dict(
                text="비율(%)",
                font=dict(color="#D1D5DB"),
            ),
            showgrid=True,
            gridcolor="rgba(255,255,255,0.08)",
            zeroline=False,
            tickfont=dict(color="#D1D5DB"),
        ),
    )
    return fig


def make_risk_donut(risk_segments: dict) -> go.Figure:
    colors = ["#E50914", "#F97316", "#FACC15", "#22C55E"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=risk_segments["labels"],
                values=risk_segments["values"],
                hole=0.65,
                marker=dict(colors=colors),
                textinfo="none",
                sort=False,
            )
        ]
    )

    fig.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        annotations=[
            dict(
                text=f"<b>{sum(risk_segments['values']):,}</b><br>총 사용자",
                x=0.5,
                y=0.5,
                font=dict(size=18, color="#F9FAFB"),
                showarrow=False,
            )
        ],
    )
    return fig


def make_genre_donut(genres: list[dict]) -> go.Figure:
    labels = [g["label"] for g in genres]
    values = [g["value"] for g in genres]
    colors = ["#E50914", "#8B5CF6", "#3B82F6", "#F59E0B", "#10B981"]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.65,
                marker=dict(colors=colors),
                textinfo="none",
                sort=False,
            )
        ]
    )

    fig.update_layout(
        height=280,
        margin=dict(l=10, r=10, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    return fig