from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Population Forecast API"}

# @app.get("/forecast")
# def get_forecast():
#     base_dir = os.path.dirname(__file__)  # 這時是根目錄
#     pkl_path = os.path.join(base_dir, "2024_人口預測.pkl")
#     df = pd.read_pickle(pkl_path)
#     return df.to_dict(orient="records")
@app.get("/forecast")
def get_forecast():
    csv_path = os.path.join(os.path.dirname(__file__), "2024_人口預測.csv")
    df = pd.read_csv(csv_path)
    return df.to_dict(orient="records")
