# --- pages/2_Interactive_Map.py ---
import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("🗺️ Interactive House Price Map")
st.sidebar.title("🗺️ Interactive House Price Map")

data = pd.read_csv("data.csv")

city_coords = {
    "Ahmedabad": (23.0225, 72.5714), "Bangalore": (12.9716, 77.5946), "Bhopal": (23.2599, 77.4126),
    "Chennai": (13.0827, 80.2707), "Coimbatore": (11.0168, 76.9558), "Delhi": (28.7041, 77.1025),
    "Hyderabad": (17.3850, 78.4867), "Indore": (22.7196, 75.8577), "Jaipur": (26.9124, 75.7873),
    "Kanpur": (26.4499, 80.3319), "Kolkata": (22.5726, 88.3639), "Lucknow": (26.8467, 80.9462),
    "Mumbai": (19.0760, 72.8777), "Nagpur": (21.1458, 79.0882), "Patna": (25.5941, 85.1376),
    "Pune": (18.5204, 73.8567), "Surat": (21.1702, 72.8311), "Varanasi": (25.3176, 82.9739),
    "Haridwar": (29.9457, 78.1642), "Jammu": (32.7266, 74.8570), "Bijnor": (29.3732, 78.1351)
}

data["lat"] = data["location"].map(lambda x: city_coords.get(x, (None, None))[0])
data["lon"] = data["location"].map(lambda x: city_coords.get(x, (None, None))[1])
data.dropna(subset=["lat", "lon"], inplace=True)

st.sidebar.header("📌 Filter Cities")
selected = st.sidebar.multiselect("Select Cities", options=data["location"].unique(), default=list(data["location"].unique()))
filtered = data[data["location"].isin(selected)]

agg = filtered.groupby(["location", "lat", "lon"]).agg(
    AveragePrice=("price", "mean"),
    MedianPrice=("price", "median"),
    Listings=("price", "count")
).reset_index()

agg["avg_price_fmt"] = agg["AveragePrice"].apply(lambda x: f"₹{x:,.0f}")
agg["median_price_fmt"] = agg["MedianPrice"].apply(lambda x: f"₹{x:,.0f}")

layer = pdk.Layer(
    "ScatterplotLayer",
    data=agg,
    get_position='[lon, lat]',
    get_radius='AveragePrice / 1000',
    radius_scale=6,
    get_fill_color='[138, 43, 226, 150]',
    pickable=True,
    auto_highlight=True
)

view = pdk.ViewState(latitude=22.9734, longitude=78.6569, zoom=4.3)

tooltip = {
    "html": "<b>{location}</b><br>Avg: {avg_price_fmt}<br>Median: {median_price_fmt}<br>Listings: {Listings}",
    "style": {"backgroundColor": "black", "color": "white"}
}

st.pydeck_chart(pdk.Deck(map_style="mapbox://styles/mapbox/dark-v10", initial_view_state=view, layers=[layer], tooltip=tooltip))
