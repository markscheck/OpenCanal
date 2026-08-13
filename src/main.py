from fastapi import FastAPI 

from src.data_loader import list_datasets, load_dataset


app = FastAPI(
    title="OpenCanal",
    version="0.1.0" 
)

@app.get("/")
def root():
    return {
       "project": "OpenCanal",
       "version": "0.1.0",
       "status": "running"

}

@app.get("/api/v1/datasets")
def datasets():
    return {
        "datasets": list_datasets()
}

@app.get("/api/v1/datasets/{filename}")
def get_dataset(filename: str):
    return load_dataset(filename)

@app.get("/api/v1/discharge/amu-darya")
def amu_darya_discharge():
    import csv

    path = "data/discharge/glofas/processed/amu_darya_glofas_2024.csv"

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)

    return {
        "river": "Amu Darya",
        "source": "GloFAS",
        "year": 2024,
        "records": len(records),
        "data": records
    }
