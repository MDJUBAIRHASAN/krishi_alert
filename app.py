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

# Pest alerts
st.subheader("🦟 Pest Alerts")
st.info(PEST_ALERTS.get(crop, "No current alerts."))

# Weather (7-day)
st.subheader("🌦️ 7-Day Weather Forecast (Live)")
try:
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": f"{district},BD", "appid": OPENWEATHER_API_KEY, "units": "metric"}
    res = requests.get(url, params=params)
    data = res.json()

    if "list" in data:
        shown_dates = set()
        for item in data["list"]:
            dt_txt = item["dt_txt"]
            date = dt_txt.split(" ")[0]
            if date not in shown_dates and len(shown_dates) < 7:
                temp = item["main"]["temp"]
                desc = item["weather"][0]["description"].capitalize()
                humidity = item["main"]["humidity"]
                wind = item["wind"]["speed"]
                st.markdown(f"📅 {date}: 🌡️ {temp}°C, {desc}, 💧 {humidity}%, 🍃 {wind} m/s")
                shown_dates.add(date)
    else:
        st.error("Weather data unavailable.")
except:
    st.error("Weather data unavailable.")

# Market Prices
st.subheader("💰 Today's Market Prices — Live from DAM")
try:
    page = requests.get("https://www.dam.gov.bd/market_daily_price_report")
    page.encoding = "utf-8"
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find("table")

    if table:
        rows = table.find_all("tr")[1:]
        for row in rows:
            cols = [td.get_text(strip=True) for td in row.find_all("td")]
            if len(cols) >= 3:
                commodity, retail, wholesale = cols[0], cols[1], cols[2]
                st.write(f"• **{commodity}** — 🛒 Retail: {retail} | 🏬 Wholesale: {wholesale}")
        st.markdown("📌 Source: Department of Agricultural Marketing (DAM)")
    else:
        st.error("⚠️ DAM site structure may have changed.")
except Exception:
    st.error("⚠️ Failed to fetch market prices. DAM site may have changed.")

