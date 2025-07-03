import streamlit as st
import requests

# Configuration
st.set_page_config("Krishi Alert", "🌾")

OPENWEATHER_API_KEY = "YOUR_OPENWEATHERMAP_KEY"  # free signup at openweathermap.org
DAM_PRICE_URL = "https://market.dam.gov.bd/market_daily_price_report?L=E"

# Static pest alerts
PEST_ALERTS = {
    "Paddy": "⚠️ Recent outbreaks of Brown Planthopper in Boro fields. Monitor water levels & use resistant varieties.",
    "Maize": "⚠️ Fall armyworm & stem borer detected. Deploy pheromone traps or early scouting advised.",
    "Potato": "⚠️ Late blight risk. Avoid overhead irrigation and spray fungicide early."
}

# Real fertilizer data
FERTILIZER_DATA = {
    "Paddy": [
        {"Stage": "Basal (land prep)", "Fertilizer": "1/3 Urea, full TSP & MOP, gypsum, ZnSO₄ (per bigha)"},
        {"Stage": "Tillering (20–25 days)", "Fertilizer": "1/3 Urea"},
        {"Stage": "Panicle initiation", "Fertilizer": "1/3 Urea"}
    ],
    "Maize": [
        {"Stage": "Basal", "Fertilizer": "1/3 N + full P, K, S, Mg, Zn, B (per ha)"},
        {"Stage": "30–35 DAS", "Fertilizer": "1/3 N"},
        {"Stage": "50–60 DAS", "Fertilizer": "1/3 N"}
    ],
    "Potato": [
        {"Stage": "Before planting", "Fertilizer": "Cow dung, Urea, TSP, MOP, S (per ha)"},
        {"Stage": "30 DAP", "Fertilizer": "Top-dress Urea if needed"},
        {"Stage": "50 DAP", "Fertilizer": "MOP if deficiency"}
    ]
}

# --- UI ---
st.title("🌾 Krishi Alert: Farmer Assistant")
district = st.selectbox("📍 Select District", ["Dhaka","Rajshahi","Khulna","Chattogram","Sylhet","Mymensingh"])
crop = st.selectbox("🌱 Select Crop", ["Paddy","Maize","Potato"])

if st.button("🔍 Get Recommendations"):
    # Fertilizer
    st.subheader("🧪 Fertilizer Schedule")
    for item in FERTILIZER_DATA.get(crop, []):
        st.markdown(f"✅ **{item['Stage']}**: {item['Fertilizer']}")

    # Pest Alerts
    st.subheader("🦟 Pest Alerts")
    st.info(PEST_ALERTS.get(crop, "No current alerts for this crop."))

    # Weather Forecast
    st.subheader("🌦️ 7‑Day Weather Forecast")
    weather = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast/daily",
        params={"q": district+",BD", "cnt":7, "appid": OPENWEATHER_API_KEY, "units":"metric"}
    ).json()
    for day in weather.get("list", []):
        dt = day["dt"]
        temp = day["temp"]
        st.write(f"{st.time.strftime('%a, %d %b', st.time.localtime(dt))}: High {temp['max']}°C / Low {temp['min']}°C — {day['weather'][0]['description']}")

    # Market Prices
    st.subheader("💰 Today’s Market Prices")
    res = requests.get(DAM_PRICE_URL)
    data = res.text
    prices = {}
    for line in data.splitlines():
        if any(term in line for term in ["Onion-local","Green Chili","Aman-Fine","Boro-Medium"]):
            parts = line.strip().split(":")
            if len(parts)==2:
                item, val = parts
                prices[item.strip()] = val.strip()
    for item,val in prices.items():
        st.write(f"• **{item}**: {val}")

    st.markdown("📌 *Prices source: DAM*")
