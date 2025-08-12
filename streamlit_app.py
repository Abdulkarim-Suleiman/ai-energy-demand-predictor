import streamlit as st
import pandas as pd
import plotly.express as px

st.title("AI Meets Energy — Data Center Power Demand Forecast")

# Load data
df = pd.read_csv("data/sample_energy.csv")

workload = st.slider("AI Workload (%)", 0, 100, 50)
temp = st.slider("Temperature (°C)", 15, 45, 25)
grid = st.selectbox("Grid Profile", ["UAE", "US", "EU"])

# Simple simulation
predicted_power = (df['power_consumption_mwh'].mean() * (1 + workload/100) * (1 + (temp-25)*0.02))

st.metric("Predicted Hourly Power (MWh)", f"{predicted_power:.2f}")
fig = px.line(df, x="timestamp", y="power_consumption_mwh", title="Historical Power Consumption")
st.plotly_chart(fig)
