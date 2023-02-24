import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

# Read in the data
df = pd.read_csv('path/to/Dataset', encoding='utf-8')

# Define the app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Exploratory Data Analysis Dashboard", style={'text-align': 'center'}),
    html.Div([
        dcc.Dropdown(
            id='x-axis-column',
            options=[{'label': col, 'value': col} for col in df.select_dtypes(include=['float', 'int']).columns],
            value='col1'
        ),
        dcc.Dropdown(
            id='y-axis-column',
            options=[{'label': col, 'value': col} for col in df.select_dtypes(include=['float', 'int']).columns],
            value='col2'
        ),
        dcc.Graph(id='scatterplot')
    ], style={'width': '49%', 'display': 'inline-block'}),
    html.Div([
        dcc.Dropdown(
            id='histogram-column',
            options=[{'label': col, 'value': col} for col in df.select_dtypes(include=['float', 'int']).columns],
            value='col1'
        ),
        dcc.Graph(id='histogram')
    ], style={'width': '49%', 'display': 'inline-block'}),
    dcc.Graph(id='boxplot', figure={
        'data': [
            go.Box(
                y=df[column],
                name=column
            ) for column in df.select_dtypes(include=['float', 'int']).columns
        ],
        'layout': go.Layout(
            xaxis={'title': 'Column'},
            yaxis={'title': 'Value'},
            hovermode='closest'
        )
    })
], style={'padding': '10px'})

# Define callback for scatterplot
@app.callback(
    Output('scatterplot', 'figure'),
    [Input('x-axis-column', 'value'),
     Input('y-axis-column', 'value')])
def update_scatterplot(x_column, y_column):
    data = [
        go.Scatter(
            x=df[x_column],
            y=df[y_column],
            mode='markers',
            marker=dict(color='red', size=10, opacity=0.5),
            name=f'{x_column} vs {y_column}'
        )
    ]
    layout = go.Layout(
        xaxis={'title': x_column},
        yaxis={'title': y_column},
        hovermode='closest'
    )
    return {'data': data, 'layout': layout}

# Define callback for histogram
@app.callback(
    Output('histogram', 'figure'),
    [Input('histogram-column', 'value')])
def update_histogram(column):
    data = [
        go.Histogram(
            x=df[column],
            opacity=0.75,
            name=column
        )
    ]
    layout = go.Layout(
        xaxis={'title': column},
        yaxis={'title': 'Count'},
        hovermode='closest'
    )
    return {'data': data, 'layout': layout}

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
