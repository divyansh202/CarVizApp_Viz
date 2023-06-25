from dash import Dash, dcc, html, Input, Output, no_update
import pandas as pd
import plotly.express as px
import numpy as np
import requests

app = Dash(__name__)

flag = 1

def get_dataFrame(username_input):
    

    data = requests.get('http://localhost:8080/car?year=2023&make='+username_input)\
                         .json()
    #df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')    
    #print(data)
    return data


fig = px.line()

app.layout = html.Div(
    
    children=[
        html.H1(children='Title of Dash App', style={'textAlign':'center'}),
        dcc.Input(id="username_input", placeholder="Enter Make", type="text"),
        dcc.Input(id="username_input", placeholder="Enter Make", type="text"),
        dcc.Graph(id="example-graph", figure=fig),
    ]
)


@app.callback(
    Output("example-graph", "figure"), Input("username_input", "value"),
)
def func(username_input: str):
    if username_input:
        df = get_dataFrame(username_input)
        fig = px.line(df, x='model', y='city_mpg')
        return fig
    return no_update


if __name__ == "__main__":
    app.run(debug=True)