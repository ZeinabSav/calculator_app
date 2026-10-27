from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Calculator is running!"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}
