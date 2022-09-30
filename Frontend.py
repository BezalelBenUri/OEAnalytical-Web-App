import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table

import pandas as pd

from Backend import DataRepository as pc
from Middle import GraphBuilder as gb


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

colors = {
    "graphBackground": "#F5F5F5",
    "background": "#ffffff",
    "text": "#000000"
}

app.layout = html.Div(children = [
    
    html.Div([
        html.H1(children = 'OEA Jetty Assesment Analysis',
           style = {
            'text-align' : 'center',
            'font-family' : 'serif',
            'font-weight' : 'normal',
            'text-transform' : 'uppercase',
            'border-bottom' : '1px solid #57b1dc',
            'margin-top' : '30px',
        }
                ),
        
        ]),
    
    dcc.Upload(
        id = 'resident-upload-data',
        children = html.Div([
            'Insert Residents data',
            html.A('Select Files'),
        ]),
        style = {
            'width': '20%',
            'height': '50px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple = True
    ),
    html.Div(id = 'resident-output-data-upload'),
    
    dcc.Dropdown(
            options = ["Gender", "Residents duration", "Occupation and Income", "Jetty use", "Jetty frequent use", "Mode of transportation", "Incentives", "Jetty Impact", "Impact such as"],
            placeholder = "Select metrics",
            id = "resident-plots-dropdown",
            style = {"width": "50%"},
        
        ),
    
    html.Div(id = "resident-plot-display"),
    
    # Passengers Data
    dcc.Upload(
        id = 'passenger-upload-data',
        children = html.Div([
            'Insert Passenger data',
            html.A('Select Files')
        ]),
        style = {
            'width': '20%',
            'height': '50px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple = True
    ),
    
    html.Div(id = 'passenger-output-data-upload'),
    
    dcc.Dropdown(
            options = ["Gender", "Residency", "Occupation and Income", "Usage purposes", "Perception on Tfare", "Delayed ride", "Anti delay", "Experience problems?", "Problems like", "Jetty rating"],
            placeholder="Select metric",
            id = "passenger-plots-dropdown" ,
        style = {"width": "50%"},
        ),
    
    html.Div(id = "passenger-plot-display"),
])






@app.callback(Output('resident-output-data-upload', 'children'),
              Input('resident-upload-data', 'contents'),
              State('resident-upload-data', 'filename'),
              State('resident-upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            pc.parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
    


@app.callback(Output('resident-plot-display', 'children'),
              Input('stored-data', 'data'),
              Input('resident-plots-dropdown', 'value')
)   
def display_graph(data, graph_name):
    """Serves applicant demograhic visualization.

    Parameters
    ----------
    graph_name : str
        User input given via 'demo-plots-dropdown'. Name of Graph to be returned.
        Options are 'Nationality', 'Age', 'Education'.

    Returns
    -------
    dcc.Graph
        Plot that will be displayed in 'demo-plots-display' Div.
    """
    df = pd.DataFrame(data)
    if graph_name == "Gender":
        fig = gb.what_is_your_gender(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Residents duration":
        fig = gb.residents_duration(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Occupation and Income":
        fig = gb.occupation_n_income(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Jetty use":
        fig = gb.jetty_use(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Jetty frequent use":
        fig = gb.jetty_usage(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Mode of transportation":
        fig = gb.mode_of_transportation(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Incentives":
        fig = gb.jetty_inc(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Jetty Impact":
        fig = gb.jetty_impact(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Impact such as":
        fig = gb.impact_as(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Improvement factors":
        fig = gb.improvement(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Improvement factors":
        fig = gb.improvement(df)
        return dcc.Graph(figure = fig)
    
    
    
    # passengers section

    
@app.callback(Output('passenger-output-data-upload', 'children'),
              Input('passenger-upload-data', 'contents'),
              State('passenger-upload-data', 'filename'),
              State('passenger-upload-data', 'last_modified'))
def passenger_update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            pc.parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
    


@app.callback(Output('passenger-plot-display', 'children'),
              Input('stored-data', 'data'),
              Input('passenger-plots-dropdown', 'value')
)   
def passenger_display_graph(data, graph_name):
    """Serves data visualization.

    Parameters
    ----------
    data : dataframe
    
    graph_name : str

    Returns
    -------
    dcc.Graph
        Plot that will be displayed in 'passengers-plots-display' Div.
    """
    df = pd.DataFrame(data)
    if graph_name == "Gender":
        fig = gb.what_is_your_gender(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Residency":
        fig = gb.residency(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Occupation and Income":
        fig = gb.occupation_n_income(df)
        return dcc.Graph(figure = fig)
    # elif graph_name == "Jetty frequent use":
    #     fig = gb.jetty_usage1(df)
    elif graph_name == "Perception on Tfare":
        fig = gb.fare_view(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Experience problems?":
        fig = gb.problems(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Problems like":
        fig = gb.experience(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Usage purposes":
        fig = gb.purpose(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Delayed ride":
        fig = gb.delay_ride(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Anti delay":
        fig = gb.anti_delay(df)
        return dcc.Graph(figure = fig)
    elif graph_name == "Jetty rating":
        df = gb.rating(df)
        return(dash_table.DataTable(
            df.to_dict('records'),
            [{"name": i, "id": i} for i in df.columns]
        ))