


from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]
+ [
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a Make and press submit')
]
)

# @callback(
#     Output('graph-content', 'figure'),
#     Input('dropdown-selection', 'value')
# )


@callback(
    [Output('container-button-basic', 'children'), Output('graph-content', 'figure')],
    Input('submit-val', 'value'),
    State('input-on-submit', 'value')
)

def update_graph(value):
    print(value)
    

def update_output(n_clicks, value):
    #df = pd.read_csv('http://localhost:8080/car?make=BMW')
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=True)


