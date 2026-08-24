import json
from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr

RIVER_FILE = Path("/app/data/mrb_rivers.json")
GLOFAS_FILE = Path(
    "/app/data/discharge/glofas/processed/glofas_2024.nc"
)
OUTPUT_DIR = Path(
    "/app/data/discharge/glofas/processed"
)


def load_amu_darya_coordinates():
    """Load coordinates from the Amu Darya feature."""

    with open(RIVER_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    for feature in data["features"]:
        if feature["properties"].get("RIVER") == "Amu Darya":
            return feature["geometry"]["coordinates"]

    raise ValueError("Amu Darya not found in mrb_rivers.json")


def flatten_coordinates(coordinates):
    """Flatten MultiLineString coordinates into lat/lon pairs."""

    points = []

    for line in coordinates:
        for longitude, latitude in line:
            points.append((latitude, longitude))

    return points


def main():
    print("Loading Amu Darya geometry...")

    coordinates = load_amu_darya_coordinates()
    river_points = flatten_coordinates(coordinates)

    print(f"Amu Darya geometry points: {len(river_points)}")

    print("Opening GloFAS dataset...")

    ds = xr.open_dataset(GLOFAS_FILE)

    discharge = ds["avg_dis"]

    latitudes = ds.latitude.values
    longitudes = ds.longitude.values

    selected_cells = set()

    print("Finding nearest GloFAS cells...")

    for latitude, longitude in river_points:
        lat_index = np.abs(latitudes - latitude).argmin()
        lon_index = np.abs(longitudes - longitude).argmin()

        selected_cells.add(
            (lat_index, lon_index)
        )

    print(
        f"Unique GloFAS cells selected: "
        f"{len(selected_cells)}"
    )

    records = []

    for lat_index, lon_index in selected_cells:

        latitude = float(latitudes[lat_index])
        longitude = float(longitudes[lon_index])

        values = discharge[:, lat_index, lon_index].values

        for date, value in zip(
            ds.valid_time.values,
            values
        ):
            records.append(
                {
                    "date": pd.Timestamp(date).date(),
                    "latitude": latitude,
                    "longitude": longitude,
                    "discharge_m3s": float(value),
                }
            )

    output = pd.DataFrame(records)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = (
        OUTPUT_DIR / "amu_darya_glofas_2024.csv"
    )

    output.to_csv(output_file, index=False)

    print(f"Saved: {output_file}")
    print(f"Rows: {len(output)}")


if __name__ == "__main__":
    main()
