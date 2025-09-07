import pandas as pd
import os
from datetime import datetime

def load_available_data():
    """
    Load available COVID-19 datasets from the local dataset folder
    using relative paths that work across different environments
    """
    # Get the directory where this script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(f"Script directory: {script_directory}")
    
    # The dataset folder is in the same directory as this script
    dataset_path = os.path.join(script_directory, 'dataset')
    print(f"Dataset path: {dataset_path}")
    
    # Check if the dataset directory exists
    if not os.path.exists(dataset_path):
        error_msg = f"""
        Dataset directory not found at: {dataset_path}
        
        Please ensure:
        1. You have a 'dataset' folder in your project directory
        2. The folder contains the required CSV files:
           - time_series_covid_19_confirmed.csv
           - time_series_covid_19_deaths.csv  
           - time_series_covid_19_recovered.csv
           - (and other COVID-19 datasets)
        
        Your current project structure should look like:
        /your-project-directory/
        ├── app.py
        ├── data_loader.py
        ├── forecasting.py
        └── dataset/
            ├── time_series_covid_19_confirmed.csv
            ├── time_series_covid_19_deaths.csv
            ├── time_series_covid_19_recovered.csv
            └── ...other files...
        """
        raise FileNotFoundError(error_msg)
    
    # List all files in the dataset directory
    all_files = os.listdir(dataset_path)
    print("Available files in dataset folder:")
    for file in all_files:
        print(f"  - {file}")

    data_dict = {}

    # Try to load time series data
    time_series_files = {
        'confirmed': None,
        'deaths': None,
        'recovered': None
    }

    # Find the actual time series files
    for file in all_files:
        if 'confirmed' in file.lower() and file.endswith('.csv'):
            time_series_files['confirmed'] = file
        elif 'death' in file.lower() and file.endswith('.csv'):
            time_series_files['deaths'] = file
        elif 'recovered' in file.lower() and file.endswith('.csv'):
            time_series_files['recovered'] = file

    print(f"\nTime series files found: {time_series_files}")

    # Load time series data if available
    if all(time_series_files.values()):
        print("Loading time series data...")
        confirmed = pd.read_csv(os.path.join(dataset_path, time_series_files['confirmed']))
        deaths = pd.read_csv(os.path.join(dataset_path, time_series_files['deaths']))
        recovered = pd.read_csv(os.path.join(dataset_path, time_series_files['recovered']))

        # Process time series data
        id_vars = ['Province/State', 'Country/Region', 'Lat', 'Long']
        value_vars = confirmed.columns[4:]

        confirmed_long = confirmed.melt(id_vars=id_vars, value_vars=value_vars,
                                       var_name='Date', value_name='Confirmed')
        deaths_long = deaths.melt(id_vars=id_vars, value_vars=value_vars,
                                  var_name='Date', value_name='Deaths')
        recovered_long = recovered.melt(id_vars=id_vars, value_vars=value_vars,
                                       var_name='Date', value_name='Recovered')

        # Merge time series data
        merged = confirmed_long.merge(deaths_long, on=id_vars+['Date'])
        merged = merged.merge(recovered_long, on=id_vars+['Date'])
        
        # Try to parse dates with different formats
        try:
            merged['Date'] = pd.to_datetime(merged['Date'], format='%m/%d/%y')
        except:
            try:
                merged['Date'] = pd.to_datetime(merged['Date'], format='%Y-%m-%d')
            except:
                merged['Date'] = pd.to_datetime(merged['Date'])
        
        # Group by country and date
        country_data = merged.groupby(['Country/Region', 'Date']).agg({
            'Confirmed': 'sum',
            'Deaths': 'sum',
            'Recovered': 'sum'
        }).reset_index()

        # Calculate additional metrics
        country_data['Mortality_Rate'] = (country_data['Deaths'] / country_data['Confirmed'] * 100).fillna(0)
        country_data['Recovery_Rate'] = (country_data['Recovered'] / country_data['Confirmed'] * 100).fillna(0)

        data_dict['time_series'] = country_data
        print(f"Successfully loaded time series data for {country_data['Country/Region'].nunique()} countries")
    else:
        print("Warning: Not all time series files found")
        missing_files = [k for k, v in time_series_files.items() if v is None]
        print(f"Missing files: {missing_files}")
        data_dict['time_series'] = None

    # Try to load other datasets
    datasets_to_try = [
        'covid_19_data', 'COVID19_line_list_data', 'COVID19_open_line_list',
        'sars_2003_complete_dataset_clean', 'countries of the world'
    ]

    for dataset_name in datasets_to_try:
        try:
            # Find the file
            matching_files = [f for f in all_files if dataset_name.lower() in f.lower() and f.endswith('.csv')]
            if matching_files:
                file_path = os.path.join(dataset_path, matching_files[0])
                data_dict[dataset_name] = pd.read_csv(file_path)
                print(f"Loaded {dataset_name} from {matching_files[0]}")
            else:
                data_dict[dataset_name] = None
                print(f"Could not find file for {dataset_name}")
        except Exception as e:
            data_dict[dataset_name] = None
            print(f"Error loading {dataset_name}: {e}")

    return data_dict

# Test the function
if __name__ == "__main__":
    print("Testing data loader...")
    data = load_available_data()
    if data.get('time_series') is not None:
        print("\nTime series data sample:")
        print(data['time_series'].head())
        print(f"\nLoaded time series data for {data['time_series']['Country/Region'].nunique()} countries")
    else:
        print("Failed to load time series data")
