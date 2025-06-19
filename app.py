#Imports
import dash
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output
import plotly.express as px
import pandas as pd



# Load Dataset
def load_data():
    data = pd.read_csv('assets/healthcare.csv')
    data["Billing Amount"] = pd.to_numeric(data["Billing Amount"], errors='coerce')
    data["Data of Admission"] = pd.to_datetime(data["data of Admission"])
    data["YearMonth"] = data["Data of Admission"].dt.to_period("M")
    return data

data = load_data()

#Create a web App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])









