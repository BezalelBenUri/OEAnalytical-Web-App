import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table

import pandas as pd

class DataRepository:
    
    """init

        Parameters
        ----------
        content : csv
        filename : str, optional
        date : str, optional
        """
    
    def __init__(self, content, filename, date):
        self.content = content
        self.filename = filename
        self.date = date
        
        
        
        """A parser functon that takes text file from the user and returns a html file.


        Parameters
        ----------
        content : csv or excel file
        filename : name of the uploaded file
        date:


        Returns
        -------
        html.Div
        """
    def parse_contents(contents, filename, date):
        
        """A parser functon that .

        Parameters
        ----------
        content : csv or excel file
        filename : name of the uploaded file
        date:


        Returns
        -------
        html.Div
        """
        
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
            elif 'txt' or 'tsv' in filename:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), delimiter = r'\s+')
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])

        return html.Div([
            html.H5(filename),
            html.H6(datetime.datetime.fromtimestamp(date)),

            dash_table.DataTable(
                df.to_dict('records'),
                [{'name': i, 'id': i} for i in df.columns],
                page_size = 10,
                style_header = {
            'backgroundColor': 'rgb(210, 210, 210)',
            'color': 'black',
            'fontWeight': 'bold'
        },
            ),
            
            dcc.Store(id = 'stored-data', data = df.to_dict('records'))
        ])

     # ignore this   
    
    def parse_data(contents, filename, date):
        
        """A parser functon that .

        Parameters
        ----------
        content : csv or excel file
        filename : name of the uploaded file
        date:


        Returns
        -------
        html.Div
        """
        
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
            elif 'txt' or 'tsv' in filename:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), delimiter = r'\s+')
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])

        return df