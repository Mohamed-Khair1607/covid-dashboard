# COVID-19 Interactive Dashboard

## 📊 Project Overview

The COVID-19 Interactive Dashboard is a comprehensive web application that provides visual analytics and forecasting for COVID-19 data across different countries. This project was developed to help researchers, policymakers, and the general public understand the progression of the pandemic through interactive visualizations and predictive modeling.

## 🎯 Purpose & Need

The COVID-19 pandemic has generated vast amounts of data that can be difficult to interpret. This dashboard addresses several critical needs:

1. **Data Accessibility**: Makes complex COVID-19 data understandable through visualizations
2. **Trend Analysis**: Helps identify patterns and trends in case numbers, deaths, and recoveries
3. **Predictive Insights**: Provides forecasting to anticipate potential future outbreaks
4. **Comparative Analysis**: Allows comparison between different countries and regions
5. **Open Access**: Provides free access to analyzed COVID-19 data for researchers and the public

## ✨ Features

### 📈 Interactive Visualizations
- Time series charts showing confirmed cases, deaths, and recoveries
- Mortality and recovery rate trends
- Geographic heat maps showing global distribution of cases
- Comparative analysis between countries

### 🔮 Predictive Analytics
- 30-day forecasting using linear regression models
- Model performance metrics (MAE, RMSE, R²)
- Confidence intervals for predictions
- Trend analysis based on historical data

### 🌐 User-Friendly Interface
- Country selection dropdown for focused analysis
- Tab-based navigation for different visualization types
- Responsive design that works on desktop and mobile devices
- Interactive charts with hover information and zoom capabilities

### 📊 Data Processing
- Automated data loading and preprocessing
- Calculation of derived metrics (mortality rate, recovery rate)
- Handling of multiple data sources and formats
- Efficient data aggregation and transformation

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Visualization**: Plotly Express
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Data Sources**: Johns Hopkins University COVID-19 dataset

## 🚀 How to Run the Project

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/covid-dashboard.git
   cd covid-dashboard
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your dataset files**
   - Create a `dataset` folder in the project directory
   - Add the following CSV files to the dataset folder:
     - `time_series_covid_19_confirmed.csv`
     - `time_series_covid_19_deaths.csv`
     - `time_series_covid_19_recovered.csv`
     - (Other COVID-19 datasets as available)

5. **Run the application locally**
   ```bash
   streamlit run streamlit_app.py
   ```

6. **Access the dashboard**
   - Open your web browser and go to `http://localhost:8501`
   - The dashboard will load with interactive controls and visualizations

## 🌐 Deployment on Streamlit Cloud

To deploy your dashboard for free on Streamlit Cloud:

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Sign up for Streamlit Cloud**
   - Visit https://streamlit.io/cloud
   - Sign in with your GitHub account

3. **Deploy your application**
   - Click "New app"
   - Select your repository, branch, and main file path
   - Click "Deploy"

4. **Access your live dashboard**
   - Streamlit Cloud will provide you with a public URL
   - Your app will automatically update when you push changes to GitHub

## 📁 Project Structure

```
covid-dashboard/
├── streamlit_app.py          # Main Streamlit application
├── data_loader.py            # Data loading and preprocessing
├── forecasting.py            # Predictive modeling functions
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── dataset/                  # COVID-19 data files
    ├── time_series_covid_19_confirmed.csv
    ├── time_series_covid_19_deaths.csv
    ├── time_series_covid_19_recovered.csv
    └── ... (other data files)
```

## 🤝 Contributing

Contributions to improve the COVID-19 Dashboard are welcome! Here's how you can help:

1. **Report bugs** by opening an issue with detailed information
2. **Suggest new features** through the issues page
3. **Submit pull requests** with improvements or bug fixes
4. **Improve documentation** to help other users

Please ensure your code follows PEP 8 guidelines and includes appropriate tests.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Data provided by Johns Hopkins University Center for Systems Science and Engineering
- Built with Streamlit, Plotly, and other open-source libraries
- Inspired by the need for accessible COVID-19 data analysis tools

## 📞 Support

If you encounter any issues or have questions about the dashboard:

1. Check the existing [issues](../../issues) to see if your problem has already been reported
2. Create a new issue with detailed information about your problem
3. For urgent inquiries, contact the maintainers directly

---

**Note**: This dashboard is intended for educational and research purposes. The forecasts are based on historical data and should not be used as the sole basis for medical or public health decisions.
