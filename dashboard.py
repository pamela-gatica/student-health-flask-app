import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

RISK_ORDER = ["Low", "Moderate", "High"]
RISK_COLORS = {"Low": "#10b981", "Moderate": "#f59e0b", "High": "#ef4444"}

SLEEP_ORDER = ["Poor", "Moderate", "Good"]
ACTIVITY_ORDER = ["Low", "Moderate", "High"]
MOOD_ORDER = ["Happy", "Neutral", "Stressed"]
GENDER_COLORS = {"F": "#8b5cf6", "M": "#2dd4bf"}

AGE_BINS = [17, 19, 21, 23, 25]
AGE_LABELS = ["18-19", "20-21", "22-23", "24"]


def _style(fig, title):
    fig.update_traces(selector=dict(type="bar"), marker_cornerradius=4)
    fig.update_traces(selector=dict(type="pie"), marker=dict(line=dict(color="white", width=2)))
    fig.update_layout(
        title=dict(
            text=f"<b>{title}</b>", x=0.5, xanchor="center",
            font=dict(size=16, family="Georgia, serif", color="#1f1b63"),
        ),
        font=dict(family="Arial, sans-serif", color="#334155", size=12),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=50, b=10, l=10, r=10),
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5, title=None),
        autosize=True,
    )
    return fig.to_html(full_html=False, include_plotlyjs=False, config={"responsive": True, "displayModeBar": False})


def _risk_percentages(df, group_col, order):
    table = pd.crosstab(df[group_col], df["Health_Risk_Level"], normalize="index") * 100
    table = table.reindex(columns=RISK_ORDER, fill_value=0).reindex(order)
    return table.reset_index().melt(id_vars=group_col, var_name="Health_Risk_Level", value_name="Percentage")


def _high_risk_factors_fig(df):
    activity_rate = df.groupby("Physical_Activity")["Health_Risk_Level"].apply(lambda s: (s == "High").mean() * 100).reindex(ACTIVITY_ORDER)
    sleep_rate = df.groupby("Sleep_Quality")["Health_Risk_Level"].apply(lambda s: (s == "High").mean() * 100).reindex(SLEEP_ORDER)
    mood_rate = df.groupby("Mood")["Health_Risk_Level"].apply(lambda s: (s == "High").mean() * 100).reindex(MOOD_ORDER)

    fig = make_subplots(
        rows=1, cols=3, shared_yaxes=True, horizontal_spacing=0.06,
        subplot_titles=["Physical Activity", "Sleep Quality", "Mood"],
    )
    fig.add_trace(go.Bar(x=ACTIVITY_ORDER, y=activity_rate.values, marker_color="#ef4444", showlegend=False), row=1, col=1)
    fig.add_trace(go.Bar(x=SLEEP_ORDER, y=sleep_rate.values, marker_color="#f59e0b", showlegend=False), row=1, col=2)
    fig.add_trace(go.Bar(x=MOOD_ORDER, y=mood_rate.values, marker_color="#8b5cf6", showlegend=False), row=1, col=3)

    fig.update_yaxes(title_text="High Risk %", row=1, col=1)
    fig.update_annotations(font=dict(family="Arial, sans-serif", size=12, color="#475467"))
    return fig


def build_dashboard(df):
    df = df.copy()
    df["Age_Group"] = pd.cut(df["Age"], bins=AGE_BINS, labels=AGE_LABELS)

    # Overall risk distribution
    risk_counts = df["Health_Risk_Level"].value_counts().reindex(RISK_ORDER).reset_index()
    risk_counts.columns = ["Health_Risk_Level", "Count"]
    fig_risk_dist = px.pie(
        risk_counts, values="Count", names="Health_Risk_Level",
        color="Health_Risk_Level", color_discrete_map=RISK_COLORS,
        category_orders={"Health_Risk_Level": RISK_ORDER}, hole=0.45,
    )

    # Risk by gender
    gender_risk = _risk_percentages(df, "Gender", ["F", "M"])
    fig_risk_gender = px.bar(
        gender_risk, x="Gender", y="Percentage", color="Health_Risk_Level",
        barmode="group", color_discrete_map=RISK_COLORS,
        category_orders={"Health_Risk_Level": RISK_ORDER},
    )
    fig_risk_gender.update_yaxes(title="% of students")

    # Risk by age group
    age_risk = _risk_percentages(df, "Age_Group", AGE_LABELS)
    fig_risk_age = px.bar(
        age_risk, x="Age_Group", y="Percentage", color="Health_Risk_Level",
        barmode="stack", color_discrete_map=RISK_COLORS,
        category_orders={"Health_Risk_Level": RISK_ORDER, "Age_Group": AGE_LABELS},
    )
    fig_risk_age.update_xaxes(title="Age group")
    fig_risk_age.update_yaxes(title="% of students")

    # Average stress by risk level
    stress_means = (
        df.groupby("Health_Risk_Level")[["Stress_Level_Biosensor", "Stress_Level_Self_Report"]]
        .mean().reindex(RISK_ORDER).reset_index()
        .melt(id_vars="Health_Risk_Level", var_name="Metric", value_name="Average Stress (0-10)")
    )
    stress_means["Metric"] = stress_means["Metric"].map({
        "Stress_Level_Biosensor": "Biosensor",
        "Stress_Level_Self_Report": "Self-Reported",
    })
    fig_stress_risk = px.bar(
        stress_means, x="Health_Risk_Level", y="Average Stress (0-10)", color="Metric",
        barmode="group", color_discrete_sequence=["#2dd4bf", "#8b5cf6"],
        category_orders={"Health_Risk_Level": RISK_ORDER},
    )

    # Risk by sleep quality
    sleep_risk = _risk_percentages(df, "Sleep_Quality", SLEEP_ORDER)
    fig_risk_sleep = px.bar(
        sleep_risk, x="Sleep_Quality", y="Percentage", color="Health_Risk_Level",
        barmode="stack", color_discrete_map=RISK_COLORS,
        category_orders={"Health_Risk_Level": RISK_ORDER, "Sleep_Quality": SLEEP_ORDER},
    )
    fig_risk_sleep.update_yaxes(title="% of students")

    # Risk by physical activity
    activity_risk = _risk_percentages(df, "Physical_Activity", ACTIVITY_ORDER)
    fig_risk_activity = px.bar(
        activity_risk, x="Physical_Activity", y="Percentage", color="Health_Risk_Level",
        barmode="stack", color_discrete_map=RISK_COLORS,
        category_orders={"Health_Risk_Level": RISK_ORDER, "Physical_Activity": ACTIVITY_ORDER},
    )
    fig_risk_activity.update_xaxes(title="Physical activity")
    fig_risk_activity.update_yaxes(title="% of students")

    # Study hours distribution by health risk level
    fig_study_risk = px.box(
        df, x="Health_Risk_Level", y="Study_Hours", color="Health_Risk_Level",
        color_discrete_map=RISK_COLORS, category_orders={"Health_Risk_Level": RISK_ORDER},
    )
    fig_study_risk.update_xaxes(title="Health Risk Level")
    fig_study_risk.update_yaxes(title="Study Hours / Week")
    fig_study_risk.update_layout(showlegend=False)

    charts = {
        "risk_dist": _style(fig_risk_dist, "Overall Health Risk Distribution"),
        "risk_gender": _style(fig_risk_gender, "Health Risk by Gender"),
        "risk_age": _style(fig_risk_age, "Health Risk by Age Group"),
        "stress_risk": _style(fig_stress_risk, "Average Stress by Health Risk Level"),
        "risk_sleep": _style(fig_risk_sleep, "Health Risk by Sleep Quality"),
        "risk_activity": _style(fig_risk_activity, "Health Risk by Physical Activity"),
        "high_risk_factors": _style(_high_risk_factors_fig(df), "High Risk Rate by Activity, Sleep & Mood"),
        "study_hours_risk": _style(fig_study_risk, "Study Hours by Health Risk Level"),
    }

    insights = build_insights(df)
    return charts, insights


def build_insights(df):
    risk_by_sleep = pd.crosstab(df["Sleep_Quality"], df["Health_Risk_Level"], normalize="index") * 100
    risk_by_activity = pd.crosstab(df["Physical_Activity"], df["Health_Risk_Level"], normalize="index") * 100
    risk_by_age = pd.crosstab(df["Age_Group"], df["Health_Risk_Level"], normalize="index") * 100
    risk_by_gender = pd.crosstab(df["Gender"], df["Health_Risk_Level"], normalize="index") * 100
    stress_by_risk = df.groupby("Health_Risk_Level")["Stress_Level_Biosensor"].mean()

    return [
        {
            "title": "Stress is the strongest driver of risk",
            "finding": (
                f"Students with High health risk report an average biosensor stress level of "
                f"{stress_by_risk['High']:.1f}/10, compared to just {stress_by_risk['Low']:.1f}/10 "
                f"for those with Low risk — the widest gap of any factor in the dataset."
            ),
            "recommendation": (
                "Prioritize stress-management programs (mindfulness, counseling, workload pacing) "
                "as the first line of prevention."
            ),
        },
        {
            "title": "Poor sleep strongly raises risk",
            "finding": (
                f"{risk_by_sleep.loc['Poor', 'High']:.0f}% of students with Poor sleep quality fall "
                f"into the High risk group, versus only {risk_by_sleep.loc['Good', 'High']:.0f}% of "
                f"those with Good sleep quality."
            ),
            "recommendation": (
                "Promote sleep-hygiene initiatives — consistent schedules, screen-time limits, "
                "and rest-focused wellness campaigns."
            ),
        },
        {
            "title": "Older students show more risk",
            "finding": (
                f"24-year-olds have a {risk_by_age.loc['24', 'High']:.0f}% High-risk rate, compared "
                f"to {risk_by_age.loc['18-19', 'High']:.0f}% for 18-19 year-olds, suggesting risk "
                f"builds up over the academic journey."
            ),
            "recommendation": (
                "Strengthen wellness check-ins for upper-year students, when academic and "
                "career-related workloads tend to peak."
            ),
        },
        {
            "title": "High physical activity isn't always protective",
            "finding": (
                f"{risk_by_activity.loc['High', 'High']:.0f}% of students with High physical "
                f"activity fall into the High health-risk group, versus {risk_by_activity.loc['Low', 'High']:.0f}% "
                f"of those with Low activity — possibly reflecting overtraining combined with academic stress."
            ),
            "recommendation": (
                "Encourage balanced, moderate exercise and watch for signs of overexertion during "
                "high-stress periods rather than promoting maximum activity levels."
            ),
        },
        {
            "title": "Gender has a smaller effect",
            "finding": (
                f"The gap by gender is modest: {risk_by_gender.loc['M', 'High']:.0f}% High risk for "
                f"male students versus {risk_by_gender.loc['F', 'High']:.0f}% for female students."
            ),
            "recommendation": (
                "Design wellness programs inclusively rather than targeting a single gender, "
                "since the lifestyle factors above matter far more than gender alone."
            ),
        },
        {
            "title": "Study limitations to consider",
            "finding": (
                "This dashboard is based on a single cross-sectional sample of 1,000 students "
                "with self-reported and biosensor measurements, so it shows correlations at one "
                "point in time — not proven causes — and patterns may not generalize to other "
                "student populations."
            ),
            "recommendation": (
                "Treat these insights as hypotheses for further research (larger samples, "
                "repeated measurements over time) rather than definitive conclusions before "
                "designing interventions."
            ),
        },
    ]
