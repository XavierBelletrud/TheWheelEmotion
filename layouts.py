import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.graph_objects as go

print("debug")
df = pd.read_csv("Emotion_final.csv", usecols=['Text','Emotion'])[['Emotion','Text']]

df2 =  pd.read_csv('score.csv')

Emotions=['happy', 'sadness', 'anger','fear','love','surprise']
labels = ['feel','feeling','like','im','really','know','time','little','get','people','would','want','one','still','even',
'think','ive','life','make','bit','something','much','could','love','going','things','dont','way','day','back','go','good',
'pretty','need','always','see','right','also','say','feelings']

p =[13973,  6461,  3661,  3055,  1201,  1091,  1032,   960,   947,
         865,   847,   811,   802,   759,   746,   744,   723,   694,
         656,   650,   646,   643,   627,   620,   616,   615,   596,
         593,   558,   540,   847,   161,    95,    74,    61,    48,
          38,    31,    26,    22]





fig1 = go.Figure([go.Bar(x=Emotions, y=[7029, 6265, 2993, 2652, 1641, 879])])

fig2 = go.Figure([go.Bar(x=labels, y=p)])


layout1 = html.Div([
    html.H1('Dash Datavisualisation Tab and Graph'),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        fixed_rows={'headers': True},
        page_size=30,
        style_cell={'textAlign':'left',
                    'whiteSpace':'normal'},
        style_table={'height': '300px', 'overflowY': 'auto'}),
    html.A(html.Button('Download Data'),
        id='download-button',
        download='Emotion_final.csv',
        href='/home/helloworld/Bureau/Brief/BriefRendus/TheWheelOfEmotions/Emotion_final.csv',
        target='_blank'),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Analysis of the Pipe', href='/page-2'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
    html.Br(),
    html.H2("Frequencies of emotions in Kaggle's data"),
    dcc.Graph(figure=fig1),
    html.H3('Words frequencies of Kaggles Data'),
    dcc.Graph(figure=fig2),


])


layout2 = html.Div([
    html.Header('Analysis of the Pipe'),
    html.Br(),
    dcc.Link('Dash Datavisualisation Tab', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
    html.Br(),
    html.H1("Kaggle's data Pipe Analysis"),
    html.Br(),
    dash_table.DataTable(
            data=df2.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df2.columns],
            fixed_rows={'headers': True},
            page_size=30,
            style_cell={'textAlign':'left',
                        'whiteSpace':'normal'},
            style_table={'height': '300px', 'overflowY': 'auto'}),
    html.H2('Concatened data Pipe Analysis'),
    dash_table.DataTable(
            data=df2.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df2.columns],
            fixed_rows={'headers': True},
            page_size=30,
            style_cell={'textAlign':'left',
                        'whiteSpace':'normal'},
            style_table={'height': '300px', 'overflowY': 'auto'}),
    html.Br(),
    html.Div(id='page-2-content'),
    
    
])
