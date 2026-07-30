import folium 

# Center roughly on the Aral Sea

m = folium.Map(
    location=[45.0, 60.0],
    zoom_start=6 
)

# Marker for the Aral Sea 
folium.Marker(
  [45.0, 60.0],
  popup="Aral Sea"
).add_to(m)

folium.Marker(
    [44.8, 59.5],
    popup="Amu Darya"
).add_to(m)

folium.Marker(
    [46.3, 61.2],
    popup="Syr Darya"
).add_to(m)

folium.Marker(
    [46.8, 61.7],
    popup="Aralsk"
).add_to(m)

folium.Marker(
    [43.8, 59.0],
    popup="Munak"
).add_to(m)




# Save the map
m.save("docs/reference_map.html")

print("Map saved to docs/reference_map.html")
