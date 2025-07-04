import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(page_title="🛡️ Cybersecurity Risk Detector", layout="centered")

# Custom CSS for background and UI
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #e0f7fa, #ffffff);
}
section.main > div {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
h1, h2, h3, .stMarkdown {
    font-family: 'Segoe UI', sans-serif;
    color: #0f4c75;
}
.stButton > button {
    background-color: #0f4c75;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
    margin-top: 10px;
}
.stButton > button:hover {
    background-color: #3282b8;
}
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown("""
    <h1 style='text-align: center;'>🛡️ Cybersecurity Risk Detector</h1>
    <p style='text-align: center; font-size:18px;'>Analyze your system's security risk using ML logic</p>
    <hr style="border: 1px solid #ddd;">
""", unsafe_allow_html=True)

# Sidebar Instructions
with st.sidebar:
    st.markdown("## 🧾 Instructions")
    st.write("""
    1. Fill in system details.
    2. Click on "Predict Risk Level".
    3. Get your risk result (Low / Medium / High).
    """)
    st.markdown("---")
    st.info("📌 Example Input:\n\nVulnerabilities: 10\nUptime: 200\nIncidents: 3\nPatch: Weekly\nPorts: 15")

# Input Form
with st.form("cyber_form"):
    st.markdown("### 🛠️ Enter System Details")

    vulnerabilities = st.number_input("Number of Vulnerabilities", min_value=0, max_value=100, value=5)
    uptime = st.number_input("System Uptime (in days)", min_value=0, max_value=1000, value=30)
    incidents = st.number_input("Number of Security Incidents", min_value=0, max_value=50, value=1)
    patch = st.selectbox("Patch Update Frequency", ["Daily", "Weekly", "Monthly"])
    ports = st.slider("Number of Open Ports", min_value=0, max_value=100, value=10)

    submitted = st.form_submit_button("🔍 Predict Risk Level")

# Dummy Risk Prediction Logic
def predict_risk(vuln, uptime, incidents, patch, ports):
    score = (vuln * 2) + (incidents * 3) + ports
    if patch == "Monthly":
        score += 10
    elif patch == "Weekly":
        score += 5

    if score < 20:
        return "🟢 Low"
    elif score < 40:
        return "🟠 Medium"
    else:
        return "🔴 High"

# Show result after submission
if submitted:
    st.markdown("### 📊 Input Summary")
    input_data = {
        "Vulnerabilities": vulnerabilities,
        "Uptime (days)": uptime,
        "Incidents": incidents,
        "Patch Frequency": patch,
        "Open Ports": ports
    }
    df = pd.DataFrame([input_data])
    st.dataframe(df, use_container_width=True)

    risk_level = predict_risk(vulnerabilities, uptime, incidents, patch, ports)

    st.markdown("### 🚦 Risk Level Prediction")
    st.markdown(f"<h2 style='text-align: center;'>{risk_level}</h2>", unsafe_allow_html=True)
    st.success("✅ Prediction Complete!")
