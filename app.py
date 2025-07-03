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

if st.button("🔍 Get Recommendations"):
    st.success(f"Showing guidance for {crop} in {district}...")

    # Placeholder for the outputs (to be built in next steps)
    st.subheader("🧪 Fertilizer Schedule")
    st.info("Coming soon...")

    st.subheader("🦟 Pest Alerts")
    st.info("Coming soon...")

    st.subheader("🌦️ Weather Forecast")
    st.info("Coming soon...")

    st.subheader("💰 Market Price")
    st.info("Coming soon...")
