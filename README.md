# 🦠 COVID-19 Interactive Dashboard (Built with Dash, Not Streamlit)
---

##  What is this ?
It’s a full-featured, interactive COVID-19 data dashboard built with **Dash** framework.

---

##  What It Actually Does

### Charts 
- Time-series graphs with hover, zoom, pan — all the Plotly goodness
- Choropleth maps (yes, even Antarctica shows up — with zero cases, as expected)
- Country comparison charts (dropdown → graph → repeat)
- Mortality & recovery rate trends (because percentages > raw numbers)

### Predictions 
- 30-day forecasts using sklearn’s LinearRegression (it’s not GPT, calm down)
- Model metrics displayed: MAE, RMSE, R² — so you know how sketchy it is
- Confidence bands (optional, because sometimes you just wanna believe)

Screenshot 2025-09-07 220537.png

---

##  Built With 

- **Dash** 
- **Plotly.py** 
- **Pandas + NumPy**
- **Scikit-learn** 

---

## 🚀 How to Run This Locally

1. **Prereqs**: Python 3.8+, terminal , and a tolerance for `pip install` logs.

2. **Clone that repo**
   ```bash
   git clone https://github.com/your-username/covid-dashboard.git
   cd covid-dashboard
   ```

3. **Virtual env.**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

4. **Install the libraries**
   ```bash
   pip install -r requirements.txt
   ```

5. **Data time**
   - Create a folder: `dataset/`
   - Grab all datasets from this GitHub repo:
     - `time_series_covid_19_confirmed.csv`
     - `time_series_covid_19_deaths.csv`
     - `time_series_covid_19_recovered.csv`
     - .....
       
6. **Fire it up**
   ```bash
   python app.py  # or whatever your main Dash file is called
   ```
   Then open `http://localhost:8050` 

---

##  Folder Structure 

```
covid-dashboard/
├── app.py                    ← Main Dash app (callbacks, layout, server)
├── data_loader.py            ← Loads & cleans JHU CSVs
├── forecasting.py            ← Fits models, returns predictions
├── requirements.txt          ← All your pip needed libraries               
│   
├── dataset/                  ← Your dataset CSVs 
│   ├── confirmed.csv
│   ├── deaths.csv
│   ├── recovered.csv
│    └──  ......
│    
└── README.md                 ← You’re reading it. Hi.
```
---

##  IMPORTANT DISCLAIMER

> This app was built for **learning, research, and mild procrastination**. The predictions? Based on old data + simple models. **Do NOT use this to make real public health decisions.** 

---

 Share it.
