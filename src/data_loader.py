import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_dataset(filename: str) ->dict:
    """Load a GeoJSON dataset from the data dictionary."""
    path = DATA_DIR / filename

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def dataset_summary(filename: str) -> dict:
    """Return useful metadata about a GeoJSON dataset."""
    data = load_dataset(filename)

    features = data.get("features", [])

    geometry_types = sorted(
        {
          feature.get("geometry", {}).get("type")
          for feature in features
          if feature.get("geometry")
        }
    )
    crs_name = (
        data.get("crs", {})
        .get("properties", {})
        .get("name")
    )

    return {
        "name": data.get("name"),
        "type": data.get("type"),
        "features": len(features),
        "geometry_types": geometry_types,
        "crs": crs_name,
    }

def list_datasets() -> list[dict]:
    """Return Summaries for all the GeoJSON datasets."""
    datasets = []

    for path in sorted(DATA_DIR.glob("*.json")):
        datasets.append(dataset_summary(path.name))

    return datasets
