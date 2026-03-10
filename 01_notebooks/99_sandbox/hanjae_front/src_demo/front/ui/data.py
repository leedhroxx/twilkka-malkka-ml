KPI_DATA = [
    {
        "title": "총 사용자",
        "value": "2,050",
        "delta": "+5.2%",
        "delta_type": "positive",
        "icon": "👥",
    },
    {
        "title": "예상 이탈 사용자",
        "value": "247",
        "delta": "+12.3%",
        "delta_type": "negative",
        "icon": "📦",
    },
    {
        "title": "구독 유지율",
        "value": "87.9%",
        "delta": "-1.1%",
        "delta_type": "negative",
        "icon": "📊",
    },
]

MONTHLY_TREND = {
    "months": ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"],
    "이탈률": [55, 60, 63, 67, 70, 71, 75, 76, 73, 71, 69, 67],
    "시청감소율": [52, 58, 61, 66, 71, 69, 74, 77, 74, 72, 70, 68],
}

RISK_SEGMENTS = {
    "labels": ["높은 위험", "중간 위험", "낮은 위험", "안전"],
    "values": [247, 581, 684, 538],
}

OTT_USAGE = [
    {"label": "매일", "value": 42},
    {"label": "주 3~4회", "value": 28},
    {"label": "주 1~2회", "value": 18},
    {"label": "월 1~3회", "value": 12},
]

GENRES = [
    {"label": "드라마", "value": 38},
    {"label": "영화", "value": 27},
    {"label": "예능", "value": 19},
    {"label": "다큐", "value": 10},
    {"label": "애니", "value": 6},
]

CHURN_DRIVERS = [
    {"label": "비활성 일수", "value": 32},
    {"label": "주간 시청 시간 감소", "value": 24},
    {"label": "로그인 빈도 감소", "value": 18},
    {"label": "콘텐츠 다양성 부족", "value": 14},
]

HIGH_RISK_USERS = [
    {
        "name": "Sarah Johnson",
        "email": "sarah.j@email.com",
        "last_active": "2026.02.17",
        "inactive_days": "18일",
        "genre": "드라마",
        "risk": "87%",
        "risk_label": "높은 위험",
    },
    {
        "name": "David Miller",
        "email": "david.m@email.com",
        "last_active": "2026.02.15",
        "inactive_days": "20일",
        "genre": "영화",
        "risk": "84%",
        "risk_label": "높은 위험",
    },
    {
        "name": "Emma Wilson",
        "email": "emma.w@email.com",
        "last_active": "2026.02.18",
        "inactive_days": "16일",
        "genre": "예능",
        "risk": "81%",
        "risk_label": "높은 위험",
    },
]