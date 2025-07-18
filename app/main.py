from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Population Forecast API"}

@app.get("/forecast")
def get_forecast():
    df = pd.read_pickle("./app/2024_人口預測.pkl")
    return df.to_dict(orient="records")
