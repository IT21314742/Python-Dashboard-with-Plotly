#Imports
import dash
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output
import plotly.express as px
import pandas as pd



# Load Dataset
def load_data():
    df = pd.read_csv('assets/healthcare.csv')
    data["Billing Amount"] = pd.to_numeric()