import dash
from dash import dcc as dcc
from dash import html as html
import plotly.graph_objects as go
import pandas as pd
import numpy as np



if __name__ == '__main__':

app = dash.Dash()

app.layout = html.Div([html.H1(children='Current Topics In Data Science',
                style={'textAlign': 'center',
                    'color': '#000205'}
                ),
        html.Br()])
		
app.run_server(port=4050)