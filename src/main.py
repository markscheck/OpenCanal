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
