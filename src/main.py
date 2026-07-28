from fastapi import FastAPI 


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
