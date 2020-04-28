# coding=utf-8 

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import time
import datetime as dt
import dash_table


def get_data():
    global df_nazionale, df_regioni, df_province

    df_nazionale = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")
    df_nazionale["data"] = pd.to_datetime(df_nazionale["data"]).dt.date

    df_regioni = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv")
    df_regioni["data"] = pd.to_datetime(df_regioni["data"]).dt.date

    df_province = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv")
    df_province["data"] = pd.to_datetime(df_province["data"]).dt.date  


# get initial data                                                                                                                                                            
get_data()

lista_date = (df_province["data"].unique())
ultima_data = lista_date[-1].strftime("%A %d %b  %Y")


#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__) #, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.Div([
        html.Div([
                html.Div([
                    dcc.Markdown('''
                    Intro
                    ''')
                    ],
                    id="info",
                    className="three_modified columns info_container "
                ),
                html.Div([
                    html.Div([   
                        html.P("Table 1")
                        ], id='table-one-layout', className="four columns info_container "),
                    html.Div([   
                        html.P("Table 2")
                        ], id='table-two-layout', className="four columns info_container "),
                    ],
                ),
            ], className="row"),
        html.Div([
                html.Div([
                    html.H3("Analisi Nazionale"),
                ], className="six columns pretty_container"),
                html.Div([
                    html.H3("Andamento Nuovi Totali Positivi"),
                ], className="six columns pretty_container"),
            ], className="row"),
        html.Div([
                html.Div([
                    html.H3("Analisi Regionale"),
                ],className="six columns pretty_container"),
                html.Div([
                    html.H3("Mappa"),
                    ], className="six columns pretty_container"),
            ], className="row"), 
        ])
    ],id="main")

if __name__ == '__main__':
    app.run_server(host="0.0.0.0",debug=True) #, host="0.0.0.0", port=8800)
