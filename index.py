
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import dash

from app import server
from app import app
from layouts import layout1, layout2
import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
    dcc.Link('Dash Datavisualisation Tab', href='/Dash_Datavisualisation_Tab'),
    html.Br(),
    dcc.Link('Analysis of the Pipe', href='/Analysis_of_the_Pipe'),
])



# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Dash_Datavisualisation_Tab':
        return layout1
    elif pathname == '/Analysis_of_the_Pipe':
        return layout2
    else:
        return index_page
    # You could also return a 404 "URL not found" page here



if __name__ == '__main__':
    app.run_server(debug=True)