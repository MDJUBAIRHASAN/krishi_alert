import streamlit as st

st.set_page_config(page_title="Krishi Alert", page_icon="🌾")

st.title("🌾 Krishi Alert: Farmer Assistant")
st.markdown("Get crop-specific guidance for your district.")

# --- Input Section ---
district = st.selectbox("📍 Select District", [
    "Dhaka", "Rajshahi", "Rangpur", "Sylhet", "Barisal", "Khulna", "Mymensingh", "Chattogram"
])

crop = st.selectbox("🌱 Select Crop", [
    "Paddy", "Wheat", "Potato", "Brinjal", "Tomato", "Jute", "Maize"
])


fertilizer_data = {
"Paddy": [
{"Stage": "Land preparation (Basal)", "Fertilizer": "1/3 Urea (13 kg), full TSP (13 kg), full MOP (22 kg), Gypsum (15 kg), Zinc sulfate (1.5 kg) per bigha"},
{"Stage": "Tillering (20–25 days later)", "Fertilizer": "1/3 Urea (13 kg)"},
{"Stage": "Panicle initiation (5–7 days before)", "Fertilizer": "1/3 Urea (13 kg)"}
],
"Maize": [
{"Stage": "Basal (at planting)", "Fertilizer": "1/3 Nitrogen (22 kg), full Phosphorus (18 kg), full Potassium (37 kg), Sulfur (12 kg), Magnesium, Zinc, Boron per ha"},
{"Stage": "30–35 days after sowing", "Fertilizer": "1/3 Nitrogen (22 kg)"},
{"Stage": "50–60 days after sowing (tasseling)", "Fertilizer": "1/3 Nitrogen (22 kg)"}
],
"Potato": [
{"Stage": "Before planting", "Fertilizer": "Cow dung (5 tons), Urea (45 kg), TSP (10 kg), MOP (45 kg), Sulfur (5 kg) per ha"},
{"Stage": "30 days after planting", "Fertilizer": "Top dress: extra Urea if needed based on growth"},
{"Stage": "50 days after planting", "Fertilizer": "Light MOP if potassium deficiency seen"}
]
}

st.subheader("🦟 Pest Alerts")
alerts = {
    "Paddy": "⚠️ **Brown Planthopper (Current Poka)** infestations reported in Boro fields — causes plant drying. Prevent with water management and resistant varieties." ,
    "Maize": "⚠️ **Armyworm / Stem borer / Fall armyworm** are major maize pests — use pheromone traps and early scouting." ,
    "Potato": "⚠️ **Late blight** (Phytophthora infestans) common — spray fungicide at first signs; avoid overhead irrigation."
}
st.markdown(alerts.get(crop, "No current pest alerts for this crop."))

st.subheader("🌦️ Weather Forecast (Dhaka)")
# Display full 7-day forecast widget

::contentReference[oaicite:5]{index=5}

st.markdown("👆 Use this info to plan planting, spraying, or harvesting.")
st.subheader("💰 Today’s Market Prices (from DAM)")
prices = {
    "Aman-Fine Rice": "৳72–75/kg",
    "Boro-Medium Rice": "৳55–57/kg",
    "Onion (local)": "৳60–64/kg",
    "Green Chili": "৳218–237/kg",
    # add more as needed
}
for item, val in prices.items():
    st.write(f"• **{item}**: {val}")
st.markdown("Source: Department of Agricultural Marketing (DAM)")  # static snapshot from DAM data :contentReference[oaicite:7]{index=7}


if st.button("🔍 Get Recommendations"):
    st.success(f"Showing guidance for {crop} in {district}...")

    # Placeholder for the outputs (to be built in next steps)
    st.subheader("🧪 Fertilizer Schedule")
    schedule = fertilizer_data.get(crop)
    if schedule:
        for item in schedule:
            st.markdown(f"✅ {item['Stage']}: {item['Fertilizer']}")
    else:
        st.info("No fertilizer schedule available for this crop yet.")

    st.subheader("🦟 Pest Alerts")
    alerts = {
        "Paddy": "...Brown Planthopper..." ,
        "Maize": "...Armyworm..." ,
        "Potato": "...Late blight..."
    }
    st.markdown(alerts.get(crop, "No current pest alerts for this crop."))

    st.subheader("🌦️ Weather Forecast (Dhaka)")
    st.markdown("👆 For your district, adjust if needed.")
    st.markdown("Use local forecast services for higher accuracy.")

    # Market prices
    st.subheader("💰 Today’s Market Prices")
    prices = {...}
    for item,val in prices.items(): st.write(f"• **{item}**: {val}")
    st.markdown("Source: DAM")
