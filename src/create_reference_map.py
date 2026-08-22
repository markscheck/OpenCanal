import json

import folium

with open("data/mrb_basins.json", "r", encoding="utf-8") as f:
    basin_data = json.load(f)

with open("data/mrb_rivers.json", "r", encoding="utf-8") as f:
    river_data = json.load(f)

with open("data/mrb_rivernames.json", "r", encoding="utf-8") as f:
    river_names_data = json.load(f)

with open("data/mrb_rivnets_Q08_09.json", "r", encoding="utf-8") as f:
    rivnet_q08_09_data = json.load(f)

with open("data/mrb_rivnets_Q09_10.json", "r", encoding="utf-8") as f:
    rivnet_q09_10_data = json.load(f)

# Center roughly on the Aral Sea

m = folium.Map(
    location=[45.0, 60.0],
    zoom_start=6 
)
basin_layer = folium.FeatureGroup(name="Aral Sea Basin")
basin_layer.add_to(m)

folium.GeoJson(
    basin_data,
    name="Aral Sea Basin",
    style_function=lambda feature: {
        "fillColor": "none",
        "color": "red",
        "weight": 1,
        "fillOpacity": 0
}
).add_to(basin_layer) 

river_layer = folium.FeatureGroup(name="Rivers")
river_layer.add_to(m)

folium.GeoJson(
    river_data,
    name="Rivers"
).add_to(river_layer) 
rivnet_q08_09_layer = folium.FeatureGroup(name="River Network Q08-09")
rivnet_q08_09_layer.add_to(m)

folium.GeoJson(
    rivnet_q08_09_data,
    name="River Network Q08-09"
).add_to(rivnet_q08_09_layer)

rivnet_q09_10_layer = folium.FeatureGroup(name="River Network Q09-10")
rivnet_q09_10_layer.add_to(m)

folium.GeoJson(
    rivnet_q09_10_data,
    name="River Network Q09-10"
).add_to(rivnet_q09_10_layer)


river_names_layer = folium.FeatureGroup(name="River Names")
river_names_layer.add_to(m)

for feature in river_names_data["features"]:
    properties = feature["properties"]
    river_name = properties["RIVER"]
    coordinates = feature["geometry"]["coordinates"]

    folium.Marker(
        location=[coordinates[1], coordinates[0]],
        popup=river_name,
        tooltip=river_name
    ).add_to(river_names_layer)


# Marker for the Aral Sea 


folium.LayerControl().add_to(m)

# Save the map
m.save("docs/reference_map.html")


print("Map saved to docs/reference_map.html")
