"""Netflix 이탈 예측 분석 대시보드 진입점.

실행 방법
---------
    streamlit run app.py
"""

import streamlit as st

from src_demo.front.views.dashboard_view import render_dashboard


st.set_page_config(
    page_title="Netflix 이탈 예측 분석 대시보드",
    page_icon="🎬",
    layout="wide",
)

render_dashboard()
