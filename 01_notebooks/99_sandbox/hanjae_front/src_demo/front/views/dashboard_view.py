import streamlit as st

from ..ui.components import (
    render_churn_drivers,
    render_genre_chart,
    render_header,
    render_high_risk_users,
    render_kpi_card,
    render_ott_usage,
    render_risk_donut,
    render_section_heading,
    render_toolbar,
)
from ..ui.data import (
    CHURN_DRIVERS,
    GENRES,
    HIGH_RISK_USERS,
    KPI_DATA,
    MONTHLY_TREND,
    OTT_USAGE,
    RISK_SEGMENTS,
)
from ..viz.charts import make_trend_chart
from ..viz.styles import inject_css


def render_dashboard() -> None:
    inject_css()
    render_header()
    filters = render_toolbar()

    kpi_cols = st.columns(3)
    for col, item in zip(kpi_cols, KPI_DATA):
        with col:
            render_kpi_card(
                title=item.get("title", "-"),
                value=item.get("value", "-"),
                delta=item.get("delta", "0.0%"),
                delta_type=item.get("delta_type", "positive"),
                icon=item.get("icon", "📌"),
            )

    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)

    left, right = st.columns([1.7, 1])

    with left:
        render_section_heading("📈 월별 이탈 추세", "최근 기간 동안의 이탈률과 시청 감소율 변화 (단위: %)")
        fig = make_trend_chart(MONTHLY_TREND)
        st.plotly_chart(fig, use_container_width=True)

    with right:
        render_risk_donut(RISK_SEGMENTS)

    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        render_ott_usage(OTT_USAGE)

    with col2:
        render_genre_chart(GENRES)

    with col3:
        render_churn_drivers(CHURN_DRIVERS)

    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
    render_high_risk_users(HIGH_RISK_USERS)

    _ = filters