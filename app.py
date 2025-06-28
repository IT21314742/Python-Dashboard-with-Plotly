# Imports
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output  # <-- include html here
import plotly.express as px
import pandas as pd

# Load Dataset
def load_data():
    data = pd.read_csv('assets/healthcare.csv')
    data["Billing Amount"] = pd.to_numeric(data["Billing Amount"], errors='coerce')
    data["Data of Admission"] = pd.to_datetime(data["Data of Admission"])
    data["YearMonth"] = data["Data of Admission"].dt.to_period("M")
    return data

data = load_data()

num_records = len(data)
avg_billing = data["Billing Amount"].mean()


# Create a web App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App Layout And Design
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Healthcare Dashboard"), width=15, className="text-center my-5")
    ])
    
    #Hospital Statistics
    dbc.row([
        dbc.col(html.Div("Total Patient Records: {num_records}", className="text-center my-3 top-text"))
    ])
])


        
if __name__ == "__main__":
    app.run_server(debug=True)
