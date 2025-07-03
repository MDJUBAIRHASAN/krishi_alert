import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config("Krishi Alert", "🌾")
OPENWEATHER_API_KEY = "YOUR_OPENWEATHERMAP_KEY"

PEST_ALERTS = {
    "Paddy": "⚠️ Brown Planthopper outbreak in Boro. Monitor water & use resistant varieties.",
    "Maize": "⚠️ Fall armyworm & stem borer detected. Use pheromone traps.",
    "Potato": "⚠️ Late blight risk. Spray fungicide early."
}

FERTILIZER_DATA = {
    "Paddy": [
        {"Stage": "Basal", "Fertilizer": "1/3 Urea, full TSP/MOP, gypsum, ZnSO₄"},
        {"Stage": "Tillering (20–25 days)", "Fertilizer": "1/3 Urea"},
        {"Stage": "Panicle initiation", "Fertilizer": "1/3 Urea"}
    ],
    "Maize": [
        {"Stage": "Basal", "Fertilizer": "1/3 N + full P/K/S/Mg/Zn/B"},
        {"Stage": "30–35 DAS", "Fertilizer": "1/3 N"},
        {"Stage": "50–60 DAS", "Fertilizer": "1/3 N"}
    ],
    "Potato": [
        {"Stage": "Before planting", "Fertilizer": "Cow dung, Urea, TSP, MOP, S"},
        {"Stage": "30 DAP", "Fertilizer": "Top‑dress Urea if needed"},
        {"Stage": "50 DAP", "Fertilizer": "MOP if deficiency"}
    ]
}

st.title("🌾 Krishi Alert: Farmer Assistant")
district = st.selectbox("📍 Select District", ["Dhaka","Rajshahi","Khulna","Chattogram","Sylhet","Mymensingh"])
crop = st.selectbox("🌱 Select Crop", ["Paddy","Maize","Potato"])

if st.button("🔍 Get Recommendations"):
    st.subheader("🧪 Fertilizer Schedule")
    for item in FERTILIZER_DATA.get(crop, []):
        st.markdown(f"✅ **{item['Stage']}**: {item['Fertilizer']}")

    st.subheader("🦟 Pest Alerts")
    st.info(PEST_ALERTS.get(crop, "No current alerts."))

    st.subheader("🌦️ 7‑Day Weather Forecast (Live)")
    # Weather widget above will display automatically

    st.subheader("💰 Today's Market Prices — Live (DAM)")

    try:
        page = requests.get("https://market.dam.gov.bd/market_daily_price_report?L=E")
        page.encoding = page.apparent_encoding
        text = page.text

        # Extract lines with a commodity format, e.g., "Aman-Fine: 72.00 - 75.00"
        lines = [line.strip() for line in text.splitlines() if ':' in line and '-' in line]
        if lines:
            for line in lines:
                parts = line.split(':', 1)
                commodity = parts[0].strip()
                price = parts[1].strip()
                if commodity and price:
                    st.write(f"• **{commodity}** — {price}")
            st.markdown("📌 *Source: Department of Agricultural Marketing (DAM)*")
        else:
            st.error("⚠️ No price lines found—DAM site format may have changed.")
    except Exception:
        st.error("⚠️ Failed to fetch market prices. DAM site may have changed.")

