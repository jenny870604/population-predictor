# 台灣各縣市人口預測 API（2024）

本專案使用 Python、Pandas、scikit-learn 建立機器學習模型，預測 2024 年台灣各縣市人口，並透過 FastAPI 提供 REST API 介面。部署於 [Railway](https://railway.app/) 平台。

## 🧠 專案內容

- 讀取 2015–2023 年整合人口統計資料
- 以 `LinearRegression` 與 `RandomForestRegressor` 模型預測 2024 年人口
- 將預測結果儲存為 CSV 與 Pickle
- 透過 FastAPI 建立 `/forecast` API，提供 JSON 回應

## 🚀 API 部署（使用 Railway）

部署網址範例：  
https://your-project-name.up.railway.app

### 可用 API：

- `/`：歡迎訊息  
- `/forecast`：回傳預測人口資料（JSON 格式）

---

## 🧾 專案結構

```bash
.
├── model.py                # 預測與圖表產生腳本
├── main.py                 # FastAPI 主應用程式
├── 2024_人口預測.pkl       # 預測結果序列化檔
├── requirements.txt        # 套件清單
├── Procfile                # Railway 啟動設定
└── README.md               # 專案說明文件
