# AI Meets Energy — Predicting Data Center Power Demand

## Overview
This project predicts hourly power consumption for AI-heavy data centers using:
- Server load and workload type (training vs inference)
- Weather data (temperature, humidity → cooling load)
- Grid mix (renewables share)

## Files
- notebooks/ai_energy_forecast.ipynb — Full Kaggle-style notebook with model training & evaluation
- streamlit_app.py — Interactive dashboard to simulate AI workloads and energy demand
- data/sample_energy.csv — Synthetic dataset for demo purposes
- prompts/prompt_pack.md — Collection of AI prompts for energy operations

## Running Locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Author
Prepared for LinkedIn showcase: AI x Energy with interactive ML & prompt engineering examples.
