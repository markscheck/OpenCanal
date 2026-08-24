from pathlib import Path

import xarray as xr

INPUT_FILE = Path(
    "/app/data/discharge/glofas/raw/data_0.nc"
)

OUTPUT_DIR = Path(
    "/app/data/discharge/glofas/processed"
)


def main():
    print("Opening GloFAS data...")

    ds = xr.open_dataset(INPUT_FILE)

    discharge = ds["avg_dis"]

    print(f"Dataset contains {discharge.sizes['valid_time']} days.")
    print(
        f"Latitude: {float(ds.latitude.min()):.2f} "
        f"to {float(ds.latitude.max()):.2f}"
    )
    print(
        f"Longitude: {float(ds.longitude.min()):.2f} "
        f"to {float(ds.longitude.max()):.2f}"
    )

    # For now, save a copy of the GloFAS data in
    # a predictable location. We will add the
    # Amu Darya extraction after validating this.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = OUTPUT_DIR / "glofas_2024.nc"

    ds.to_netcdf(output_file)

    print("\nSaved processed dataset:")
    print(output_file)


if __name__ == "__main__":
    main()
