import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Set app title
st.title("Local Climate Zones (LCZ) Web App")

# Load GeoJSON file
geojson_path = "data/LCZ.GeoJson.geojson"
gdf = gpd.read_file(geojson_path)

# Display GeoJSON map
st.header("Interactive LCZ Map")
map_center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]
m = folium.Map(location=map_center, zoom_start=10)

# Add GeoJSON layer to the map
folium.GeoJson(geojson_path, name="LCZ").add_to(m)
st_folium(m, width=700, height=500)

st.write("This map displays the Local Climate Zones (LCZ) data.")

