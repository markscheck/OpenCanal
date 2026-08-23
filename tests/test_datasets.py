from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_list_datasets():
    response = client.get("/api/v1/datasets")
    assert response.status_code == 200
   
    data = response.json()
    
    assert "datasets" in data 
    assert len(data["datasets"]) >0

