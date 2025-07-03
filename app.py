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
    st.info("Coming soon...")

    st.subheader("🌦️ Weather Forecast")
    st.info("Coming soon...")

    st.subheader("💰 Market Price")
    st.info("Coming soon...")
