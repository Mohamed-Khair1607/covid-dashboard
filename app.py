import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from data_loader import load_available_data
from forecasting import simple_forecast  # Import the forecasting function

# Load all data
data_dict = load_available_data()
time_series_data = data_dict.get('time_series')
sars_data = data_dict.get('sars_2003_complete_dataset_clean')
countries_data = data_dict.get('countries of the world')

# Only continue if we have time series data
if time_series_data is None:
    print("Error: Could not load time series data. Please check your dataset files.")
    exit()

# Get list of countries for dropdown
countries = sorted(time_series_data['Country/Region'].unique())

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout with multiple tabs
app.layout = html.Div([
    html.H1("COVID-19 Dashboard with Forecasting", style={'textAlign': 'center'}),
    
    # Country selector
    html.Div([
        html.Label("Select Country:"),
        dcc.Dropdown(
            id='country-selector',
            options=[{'label': country, 'value': country} for country in countries],
            value='US'
        )
    ], style={'width': '50%', 'margin': 'auto', 'padding': '20px'}),
    
    # Tabs for different visualizations
    dcc.Tabs([
        # COVID-19 Time Series Tab
        dcc.Tab(label='COVID-19 Time Series', children=[
            dcc.Graph(id='covid-time-series-chart'),
            dcc.Graph(id='covid-metrics-chart')
        ]),
        
        # Forecasting Tab
        dcc.Tab(label='Forecasting', children=[
            dcc.Graph(id='forecast-chart'),
            html.Div(id='forecast-metrics')
        ]),
        
        # Geographic Analysis Tab
        dcc.Tab(label='Geographic Analysis', children=[
            dcc.Graph(id='world-map')
        ])
    ])
])

# Callbacks for updating charts
@app.callback(
    [Output('covid-time-series-chart', 'figure'),
     Output('covid-metrics-chart', 'figure')],
    [Input('country-selector', 'value')]
)
def update_covid_charts(selected_country):
    # Filter data for selected country
    filtered_data = time_series_data[time_series_data['Country/Region'] == selected_country]
    
    # Create time series chart
    ts_fig = px.line(filtered_data, x='Date', y=['Confirmed', 'Deaths', 'Recovered'],
                     title=f'COVID-19 Cases in {selected_country}')
    ts_fig.update_layout(yaxis_title="Number of Cases")
    
    # Create metrics chart
    metrics_fig = px.line(filtered_data, x='Date', y=['Mortality_Rate', 'Recovery_Rate'],
                         title=f'COVID-19 Metrics in {selected_country}')
    metrics_fig.update_layout(yaxis_title="Percentage")
    
    return ts_fig, metrics_fig

@app.callback(
    [Output('forecast-chart', 'figure'),
     Output('forecast-metrics', 'children')],
    [Input('country-selector', 'value')]
)
def update_forecast(selected_country):
    # Get the forecast
    result = simple_forecast(time_series_data, selected_country)
    
    if result is None:
        return px.line(title=f'Not enough data for forecasting in {selected_country}'), \
               html.Div("Not enough historical data for forecasting")
    
    forecast, metrics = result
    
    # Get historical data for the country
    historical_data = time_series_data[time_series_data['Country/Region'] == selected_country]
    
    # Create the figure with historical data
    fig = px.line(historical_data, x='Date', y='Confirmed', 
                  title=f'COVID-19 Forecast for {selected_country}')
    
    # Add forecast to the figure
    fig.add_scatter(x=forecast['Date'], y=forecast['Forecast'], mode='lines', name='Forecast')
    
    # Add confidence interval (simple approximation)
    last_value = historical_data['Confirmed'].iloc[-1]
    forecast_upper = forecast['Forecast'] * 1.1  # 10% upper bound
    forecast_lower = forecast['Forecast'] * 0.9  # 10% lower bound
    
    fig.add_trace(go.Scatter(
        x=forecast['Date'].tolist() + forecast['Date'].tolist()[::-1],
        y=forecast_upper.tolist() + forecast_lower.tolist()[::-1],
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name='Confidence Interval'
    ))
    
    # Create metrics display
    metrics_html = html.Div([
        html.H4("Forecast Evaluation Metrics"),
        html.P(f"Mean Absolute Error (MAE): {metrics['MAE']:.2f}"),
        html.P(f"Root Mean Squared Error (RMSE): {metrics['RMSE']:.2f}"),
        html.P(f"R-squared (R²): {metrics['R2']:.4f}"),
        html.Br(),
        html.H4("Forecast Information"),
        html.P(f"Current cases: {last_value:,}"),
        html.P(f"Predicted cases in 30 days: {forecast['Forecast'].iloc[-1]:,.0f}"),
        html.P(f"Predicted growth: {(forecast['Forecast'].iloc[-1] - last_value) / last_value * 100:.1f}%"),
        html.P("Note: This is a simple linear regression forecast based on recent trends.")
    ])
    
    return fig, metrics_html

@app.callback(
    Output('world-map', 'figure'),
    [Input('country-selector', 'value')]
)
def update_world_map(selected_country):
    # Get the latest data for each country
    latest_data = time_series_data.groupby('Country/Region').last().reset_index()
    
    # Create the choropleth map
    world_fig = px.choropleth(latest_data, 
                             locations="Country/Region", 
                             locationmode="country names",
                             color="Confirmed",
                             hover_name="Country/Region",
                             hover_data=["Confirmed", "Deaths", "Recovered", "Mortality_Rate"],
                             color_continuous_scale="reds",
                             title="Global COVID-19 Cases")
    
    return world_fig

server = app.server

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
