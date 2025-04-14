import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Carbon Footprint Calculator", layout="centered")
st.title("🌍 Carbon Footprint Calculator")
st.markdown("Enter details about your lifestyle to calculate your annual carbon footprint.")

# --- User Inputs ---
st.header("🚶 Lifestyle Inputs")
car_km = st.slider("How many km do you drive per week?", 0, 1000, 100)
flights_per_year = st.slider("How many flights (2-hour domestic) do you take per year?", 0, 20, 2)
meat_meals = st.slider("How many meat-based meals do you eat per week?", 0, 21, 7)
electricity_kwh = st.slider("Your average monthly electricity usage (kWh)?", 0, 1000, 300)

# --- Emission Factors (kg CO2 per unit) ---
EMISSIONS = {
    "car": 0.2,                # kg CO2 per km
    "flight": 250,             # kg CO2 per short flight
    "meat_meal": 5,            # kg CO2 per meal
    "electricity": 0.5         # kg CO2 per kWh
}

# --- Calculate Emissions ---
car_emission = car_km * 52 * EMISSIONS["car"]
flight_emission = flights_per_year * EMISSIONS["flight"]
meat_emission = meat_meals * 52 * EMISSIONS["meat_meal"]
electricity_emission = electricity_kwh * 12 * EMISSIONS["electricity"]

total_emission = car_emission + flight_emission + meat_emission + electricity_emission

# --- Data for Pie Chart ---
data = pd.DataFrame({
    "Activity": ["Driving", "Flights", "Diet", "Electricity"],
    "Emissions (kg CO₂/year)": [car_emission, flight_emission, meat_emission, electricity_emission]
})

fig = px.pie(data, names="Activity", values="Emissions (kg CO₂/year)", title="Your Carbon Footprint Breakdown")

# --- Results ---
st.header("📊 Your Carbon Footprint")
st.subheader(f"🌱 Estimated Annual Emissions: {total_emission:.2f} kg CO₂")
st.caption("Global average: ~4800 kg | India average: ~1900 kg | Safe limit: ~2000 kg")
st.plotly_chart(fig)

# --- Suggestions ---
st.header("💡 Tips to Reduce Emissions")
if car_emission > 1000:
    st.markdown("- 🚗 Consider carpooling or using public transport.")
if flight_emission > 500:
    st.markdown("- ✈️ Reduce short flights, use trains when possible.")
if meat_emission > 1000:
    st.markdown("- 🥗 Try meatless meals 2-3 times per week.")
if electricity_emission > 1000:
    st.markdown("- ⚡ Switch to LED bulbs and energy-efficient appliances.")

st.markdown("---")
st.caption("This tool is for educational purposes only. Emission factors are approximate.")
