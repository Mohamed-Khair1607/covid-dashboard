---

# 🦠 COVID-19 Interactive Dashboard (Built with Dash, Not Streamlit)

> “Wait, you used Dash? That’s actually kinda hardcore.” — Random Dev at a Hackathon

---

## 🤷‍♂️ What is this, really?

It’s a full-featured, interactive COVID-19 data dashboard built with **Plotly Dash** — the “I want full control over my layout and callbacks” framework.

No magic decorators. No auto-reload fairy dust. Just pure Python, some HTML-like components, and a whole lot of `@app.callback`.

Built for:
- Data folks who need more control than Streamlit gives
- Devs who like writing explicit state logic
- Anyone who’s ever muttered “but I need a div here…”

---

## 🎯 Why Dash? Why This?

Because sometimes you need:
✅ Real layout control (grids, containers, custom CSS? Yes.)  
✅ Complex interactivity (chained dropdowns, dynamic tabs, loading states)  
✅ Production-readiness (auth, scaling, embedding — it’s all possible)  
✅ To flex on your friends who still use Streamlit 😎

Also, free public access > paywalled dashboards. Still true.

---

## ✨ What It Actually Does

### Charts That Don’t Suck (and You Control Them)
- Time-series graphs with hover, zoom, pan — all the Plotly goodness
- Choropleth maps (yes, even Antarctica shows up — with zero cases, as expected)
- Country comparison charts (dropdown → graph → repeat)
- Mortality & recovery rate trends (because percentages > raw numbers)

### Predictions (Handle With Care)
- 30-day forecasts using sklearn’s LinearRegression (it’s not GPT, calm down)
- Model metrics displayed: MAE, RMSE, R² — so you know how sketchy it is
- Confidence bands (optional, because sometimes you just wanna believe)

### UI That’s Actually Customizable
- Responsive layout (mostly — Dash + CSS is… a journey)
- Loading spinners for when the model takes 2 extra seconds
- Error boundaries (so it doesn’t just crash when someone picks “Vatican City”)

---

## 🛠️ Built With (The Real Stack)

- **Dash** — for the app framework (callbacks, layouts, the whole shebang)
- **Plotly.py** — for charts that look like they belong in 2025
- **Pandas + NumPy** — for turning messy CSVs into something usable
- **Scikit-learn** — slapped a `.fit()` on it and called it “machine learning”
- **JHU Data** — the OG pandemic dataset. Still weirdly well-organized.

---

## 🚀 How to Run This Locally

1. **Prereqs**: Python 3.8+, terminal courage, and a tolerance for `pip install` logs.

2. **Clone that repo**
   ```bash
   git clone https://github.com/your-username/covid-dashboard.git
   cd covid-dashboard
   ```

3. **Virtual env? Do it.**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

4. **Install the universe**
   ```bash
   pip install -r requirements.txt
   ```

5. **Data time**
   - Create a folder: `dataset/`
   - Grab these from the JHU GitHub repo:
     - `time_series_covid_19_confirmed.csv`
     - `time_series_covid_19_deaths.csv`
     - `time_series_covid_19_recovered.csv`

6. **Fire it up**
   ```bash
   python app.py  # or whatever your main Dash file is called
   ```
   Then open `http://localhost:8050` — and hope you didn’t typo a callback.

---

##  Folder Structure 

```
covid-dashboard/
├── app.py                    ← Main Dash app (callbacks, layout, server)
├── data_loader.py            ← Loads & cleans JHU CSVs
├── forecasting.py            ← Fits models, returns predictions
├── requirements.txt          ← All your pip needs
├── assets/                   ← CSS, images, favicon.ico
│   └── style.css
├── dataset/                  ← Your JHU CSVs live here
│   ├── confirmed.csv
│   ├── deaths.csv
│   └── recovered.csv
└── README.md                 ← You’re reading it. Hi.
```

---
Found a bug? Think my layout looks like a 2007 Geocities page?
---

##  IMPORTANT DISCLAIMER

> This app was built for **learning, research, and mild procrastination**. The predictions? Based on old data + simple models. **Do NOT use this to make real public health decisions.** 

---

 Share it.

---

This version respects your tech stack (Dash), gives you real deployment options (Render, Docker, etc.), and keeps the tone human, humble, and slightly sarcastic — like a real dev wrote it after wrestling with a callback for 3 hours.

No Streamlit. No fluff. Just Dash, data, and deployment that actually works.
