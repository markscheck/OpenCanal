import xarray as xr

FILE = "/app/data/discharge/glofas/glofas_test/data_0.nc"


def main():
    print("Opening GloFAS dataset...")

    ds = xr.open_dataset(FILE)

    print("Dataset opened.")

    discharge = ds["avg_dis"]

    print("Found avg_dis.")
    print(f"Dimensions: {discharge.dims}")

    max_discharge = discharge.max(dim="valid_time")

    print("Calculated maximum discharge.")

    points = max_discharge.stack(
        points=("latitude", "longitude")
    )

    points = points.sortby(points, ascending=False)

    print("\nTop 20 discharge cells:")
    print(points.isel(points=slice(0, 20)))


if __name__ == "__main__":
    main()
