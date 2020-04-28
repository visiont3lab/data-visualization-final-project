# coding=utf-8 

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
import time
import datetime as dt
import dash_table

def get_nomi_regioni(df):
    nomi_regioni = list(df["denominazione_regione"].unique())
    nomi_regioni.sort()
    return nomi_regioni

def table(df):
    valore = list(df.iloc[-1:,2:13].values[0])
    incremento = list(df.iloc[-1:,2:13].values[0] - df.iloc[-2:,2:13].values[0])
    for i in range(0,len(incremento)):
        if incremento[i]>=0:  incremento[i] = "+"+str(incremento[i])
        else: incremento[i] = str(incremento[i]) 
    table_dict = {
        "tipo" :   [i.replace("_"," ") for i in list(df.keys()[2:13])],
        "numero" : [f'{valore[i]:,}' + " (" + incremento[i] +")" for i in range(0,len(valore))],
    }
    table_pd = pd.DataFrame(table_dict)
    return table_pd

def fig_nazionale(df):
    # lista_input è una lista che contiene i nomi delle regioni da plottare
    # plot_number numero di grafici da plottare All o 10

    fig = go.Figure()
    my_dict={}
    my_dict["data"] = df["data"].unique()
    lista_keys_to_plot = list(df.keys()[2:-2])
    not_visible = ["variazione_totale_positivi","tamponi", "nuovi_positivi","casi_testati"]

    for nome_key_to_plot in lista_keys_to_plot:
        my_dict[nome_key_to_plot] = list(df[nome_key_to_plot])

        visible_str=True
        if (nome_key_to_plot in not_visible):
            visible_str="legendonly"

        xx = my_dict["data"]
        yy = my_dict[nome_key_to_plot]

        fig.add_trace(go.Scatter(
                x = xx,
                y = yy,
                #legendgroup=nome_regione,
                name=nome_key_to_plot,
                mode="lines+markers",
                showlegend=True,
                visible=visible_str,
                marker=dict(
                    symbol="circle",
                    size=4,
                ),
                hoverlabel=dict(namelength=-1),
                #fill="tozeroy", # tonexty
                line=dict(
                    width=1,
                    #color="rgb(0,255,0)",
                    #dash="longdashdot"
                )
            ),
        )
        
    fig.update_layout(
        #title=dict(
        #    text ="Analisi Regionale" ,
            #y = 0.9,
            #x = 0.1, # 0.5 center
            #xanchor = "left",
            #yanchor = "top",
        #),
        legend=dict(
            orientation="v",
            #y = 1.1,
            #x = 0,
        ),
        xaxis = dict(
            title="data",
            gridcolor="cyan",
            #gridwidth=5,
            #color="red"
            #linecolor="red",
            zeroline=False,
        ),
        yaxis = dict(
            title="numero",
            gridcolor="cyan",
            #gridwidth=5,
            #linecolor = "red",
            zeroline=False,
            #zerolinecolor="cyan",
            fixedrange=True,
        ),
        font=dict(
        #    family="Courier New, monospace",
        #    size=20,
            color="white", #"#7f7f7f", 
        ),
        dragmode="pan", #Type: enumerated , one of ( "zoom" | "pan" | "select" | "lasso" | "orbit" | "turntable" | False
        hovermode='x',  #['x unified', 'y', 'closest', False]
        plot_bgcolor = "rgb(44,44,44)",
        paper_bgcolor="rgb(33, 33, 33)",
        margin={"t":50, "b": 10}
        #transition = dict(
        #    duration=500,
        #    easing='cubic-in-out',
        #),
    )
    return fig

def fig_nuovi_positivi(df):
    # lista_input è una lista che contiene i nomi delle regioni da plottare
    # plot_number numero di grafici da plottare All o 10

    fig = go.Figure()
    my_dict={}
    my_dict["data"] = df["data"].unique()
    lista_keys_to_plot = ["nuovi_positivi"]

    for nome_key_to_plot in lista_keys_to_plot:
        my_dict[nome_key_to_plot] = list(df[nome_key_to_plot])

        xx = my_dict["data"]
        yy = my_dict[nome_key_to_plot]

        fig.add_trace(go.Scatter(
                x = xx,
                y = yy,
                #legendgroup=nome_regione,
                name=nome_key_to_plot,
                mode="lines+markers",
                showlegend=True,
                marker=dict(
                    symbol="circle",
                    size=6,
                ),
                hoverlabel=dict(namelength=-1),
                fill="tozeroy", # tonexty
                line=dict(
                    width=1,
                    #color="rgb(0,255,0)",
                    #dash="longdashdot"
                )
            ),
        )
        
    fig.update_layout(
        #title=dict(
        #    text ="Analisi Regionale" ,
            #y = 0.9,
            #x = 0.1, # 0.5 center
            #xanchor = "left",
            #yanchor = "top",
        #),
        legend=dict(
            orientation="h",
            y = 1.1,
            x = 0,
        ),
        xaxis = dict(
            title="data",
            gridcolor="cyan",
            #gridwidth=5,
            #color="red"
            #linecolor="red",
            zeroline=False,
        ),
        yaxis = dict(
            title="numero",
            gridcolor="cyan",
            #gridwidth=5,
            #linecolor = "red",
            zeroline=False,
            #zerolinecolor="cyan",
            fixedrange=True,
        ),
        font=dict(
        #    family="Courier New, monospace",
        #    size=20,
            color="white", #"#7f7f7f", 
        ),
        dragmode="pan", #Type: enumerated , one of ( "zoom" | "pan" | "select" | "lasso" | "orbit" | "turntable" | False
        hovermode='x',  #['x unified', 'y', 'closest', False]
        plot_bgcolor = "rgb(44,44,44)",
        paper_bgcolor="rgb(33, 33, 33)",
        margin={"t":50, "b": 10}
        #transition = dict(
        #    duration=500,
        #    easing='cubic-in-out',
        #),
    )
    return fig

def fig_regioni(df,lista_regioni_to_plot,lista_keys_to_plot,plot_style=None):
    # lista_input è una lista che contiene i nomi delle regioni da plottare
    # plot_number numero di grafici da plottare All o 10

    lista = []
    if isinstance(lista_regioni_to_plot, list)==False:
        lista.append(lista_regioni_to_plot)
    else:
        lista = lista_regioni_to_plot   

    
    '''
    lista_keys_to_plot = ['ricoverati_con_sintomi', 'terapia_intensiva', 'totale_ospedalizzati',
       'isolamento_domiciliare', 'totale_positivi',
       'variazione_totale_positivi', 'nuovi_positivi', 'dimessi_guariti',
       'deceduti', 'totale_casi', 'tamponi', 'casi_testati']
    '''
    #print(lista_keys_to_plot)

    fig_reg = go.Figure()
    my_dict={}
    my_dict["data"] = df["data"].unique()
    for nome_regione in lista:
        for nome_key_to_plot in lista_keys_to_plot:
            my_dict[nome_key_to_plot] = list(df[df["denominazione_regione"]==nome_regione][nome_key_to_plot])

            xx = my_dict["data"]
            yy = my_dict[nome_key_to_plot]
            
            if plot_style=="bar_plot":
                fig_reg.add_trace(go.Bar(
                        x = [xx[-1]],
                        y = [yy[-1]],
                        #legendgroup=nome_regione,
                        name=nome_regione + " (" +nome_key_to_plot + ")",
                        showlegend=True,
                        #marker=dict(
                        #    symbol="circle-dot",
                        #    size=6,
                        #),
                        hoverlabel=dict(namelength=-1),
                        #fill="tozeroy", # tonexty
                    ),
                )
            else:
                fig_reg.add_trace(go.Scatter(
                        x = xx,
                        y = yy,
                        #legendgroup=nome_regione,
                        name=nome_regione + " (" +nome_key_to_plot + ")",
                        mode="lines", #+markers",
                        showlegend=True,
                        #marker=dict(
                        #    symbol="circle-dot",
                        #    size=6,
                        #),
                        hoverlabel=dict(namelength=-1),
                        #fill="tozeroy", # tonexty
                        line=dict(
                            width=2,
                            #color="rgb(0,255,0)",
                            #dash="longdashdot"
                        )
                    ),
                )
        
    fig_reg.update_layout(
        #title=dict(
        #    text ="Analisi Regionale" ,
            #y = 0.9,
            #x = 0.1, # 0.5 center
            #xanchor = "left",
            #yanchor = "top",
        #),
        legend=dict(
            orientation="v",
            #traceorder="grouped",
            #y = 1.1,
            #x = 0,
        ),
        xaxis = dict(
            title="data",
            gridcolor="cyan",
            #gridwidth=5,
            #color="red"
            #linecolor="red",
            zeroline=False,
        ),
        yaxis = dict(
            title="numero",
            gridcolor="cyan",
            #gridwidth=5,
            #linecolor = "red",
            zeroline=False,
            #zerolinecolor="cyan",
            fixedrange=True,
        ),
        font=dict(
        #    family="Courier New, monospace",
        #    size=20,
            color="white", #"#7f7f7f", 
        ),
        dragmode="pan", #Type: enumerated , one of ( "zoom" | "pan" | "select" | "lasso" | "orbit" | "turntable" | False
        hovermode='x',  #['x unified', 'y', 'closest', False]
        plot_bgcolor = "rgb(44,44,44)",
        paper_bgcolor="rgb(33, 33, 33)",
        margin={"t":50, "b": 10},
        #transition = dict(
        #    duration=500,
        #    easing='cubic-in-out',
        #),
    )
    
    return fig_reg

def fig_mappa(df,data=None):
    # FONDAMENTALE: https://plotly.com/python/mapbox-layers/

    # EXTRAA
    # https://plotly.com/~EndlessRain/62.py
    # https://plotly.com/python/scattermapbox/
    # https://docs.mapbox.com/mapbox-gl-js/style-spec/
    # token = "pk.eyJ1IjoibWFudWVscnVjY2kiLCJhIjoiY2s5MDR4aXRzMDI0ZjNnbWxtbDhnYXFiaCJ9._Rqe5z-nLG3QhOh9P4ZqLw"
    if data==None:
        ultima_data_aggiornamento = list(df.tail(1)["data"])[-1]
    else:
        ultima_data_aggiornamento = data
    num_max = df["totale_casi"].max()
    temp_df = df[(df["data"]==ultima_data_aggiornamento) & (df["denominazione_provincia"]!="In fase di definizione/aggiornamento")]
    temp_df.sort_values(by="totale_casi",ascending=True, inplace=True)
    
    nomi_province = temp_df["denominazione_provincia"] #[-40:]
 
    fig = go.Figure()
    #scale = temp_df["totale_casi"].max()
    count = 1
    for nome in nomi_province:
        row = temp_df[temp_df["denominazione_provincia"]==nome]
        num_casi = row["totale_casi"].values[0]
        size=5
        if (num_casi*30)/num_max > 5: 
            size=(num_casi*50)/num_max +size

        fig.add_trace(go.Scattermapbox(
            lon = row['long'],
            lat = row['lat'],
            text = row["totale_casi"],
            name = str((len(nomi_province)+1 - count)) + ". " +  nome + " " + str(num_casi),
            hoverinfo='text',
            hovertext= str((len(nomi_province)+1 - count)) + ". " +  nome + ": " + str(num_casi),
            mode='markers',
            marker=go.scattermapbox.Marker(
                size= size,  # 20:num_max = x : val
                color="rgb(255,0,0)",
                opacity=0.8,
                ),
            )
        )
        count +=1

    # Senza tokenn
    # open-street-map", "carto-positron", "carto-darkmatter", "stamen-terrain", "stamen-toner" or "stamen-watercolor"
    # Con token
    # "basic", "streets", "outdoors", "light", "dark", "satellite", or "satellite-streets"   white-bg
    fig.update_layout(
        hovermode='closest',
        mapbox=dict(
            #accesstoken=token,
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=41,  # ROme
                lon=12
            ),
            pitch=0,
            zoom=4,
            style="carto-darkmatter",  
        ),
        legend_font_color = "white",
        legend_traceorder = "reversed",
        paper_bgcolor="rgb(33, 33, 33)",
        transition_duration=0,
        margin={"r":10,"t":30,"l":20,"b":30}
    )
    return fig

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
tb = table(df_nazionale)
fig_naz = fig_nazionale(df_nazionale)
fig_np = fig_nuovi_positivi(df_nazionale)
regione = "Emilia-Romagna"
default_lista  = ['deceduti', 'variazione_totale_positivi','terapia_intensiva']
fig_reg = fig_regioni(df_regioni,[regione],default_lista)
fig_map = fig_mappa(df_province)

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__) #, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.Div([
       
        html.Div([
              
                html.Div([
                    dcc.Markdown('''
                    ### Covid19 Dashboard Italia
                    ##### Progetto di fine corso [data-visualization](https://github.com/visiont3lab/data-visualization)
                    Dati forniti dalla [Protezione Civile](https://github.com/pcm-dpc/COVID-19")
                    '''),
                    html.P("Ultimo aggiornamento: " + ultima_data),
                    ],
                    id="info",
                    className="three_modified columns info_container "
                ),
              
                html.Div([
                    html.Div([   

                        #html.P("Table 1"),

                        dash_table.DataTable(
                            id='table_one',
                            columns=[{"name": "", "id": "tipo"},{"name": "", "id": "numero"}], #[{"name": i.replace("_"," "), "id": i} for i in list(df_nazionale.keys()[2:7])],
                            data=tb.loc[0:4].to_dict("records"),
                            style_as_list_view=False,
                            style_header={"display" : "none"},
                            style_cell={
                                'textAlign': 'center',
                                'backgroundColor': 'rgb(44, 44, 44)',
                                'color': 'white',
                            },  
                            style_data_conditional=[{
                                "if": {"row_index": 0},
                                "backgroundColor": "#3E1D2A",
                            },{ "if": {"row_index": 1},
                                "backgroundColor": "#3E1D2A",
                            }]
                        ),

                    ], id='table-one-layout', className="four columns info_container "),
                    
                    html.Div([   
                        
                        #html.P("Table 2"),

                        dash_table.DataTable(
                                id='table_two',
                                columns=[{"name": "", "id": "tipo"},{"name": "", "id": "numero"}], #[{"name": i.replace("_"," "), "id": i} for i in list(df_nazionale.keys()[2:7])],
                                data=tb.loc[6:].to_dict("records"),
                                style_as_list_view=False,
                                style_header={"display" : "none"},
                                style_cell={
                                    'textAlign': 'center',
                                    'backgroundColor': 'rgb(44, 44, 44)',
                                    'color': 'white',
                                },  
                                style_data_conditional=[{
                                    "if": {"row_index": 2},
                                    "backgroundColor": "#3E1D2A",
                                }]
                            ),

                        ], id='table-two-layout', className="four columns info_container "),
                    ],
                ),
            ], className="row"),

        html.Div([
                html.Div([
                    html.H3("Analisi Nazionale"),
                    dcc.Graph(id='fig-var-naz', figure=fig_naz),
                ], className="six columns pretty_container"),
                html.Div([
                    html.H3("Andamento Nuovi Totali Positivi"),
                    dcc.Graph(id="fig-np", figure=fig_np),
                ], className="six columns pretty_container"),
            ], className="row"),

        html.Div([
                html.Div([
                    html.H3("Analisi Regionale"),
                    dcc.Dropdown(
                        id="dropdown-regioni",
                        options=[{'label':nome, 'value':nome} for nome in get_nomi_regioni(df_province)],
                        value=regione,
                        searchable=True,
                        multi=True
                    ), 
                    dcc.RadioItems(
                        id = "radio-buttom-plot-style",
                        options=[
                            {'label': 'line plot', 'value': 'line_plot'},
                            {'label': 'bar plot', 'value': 'bar_plot'},
                        ],
                        value='line_plot',
                        labelStyle={'display': 'inline-block'}
                    ),     
                    dcc.Graph(id='fig-reg', figure=fig_reg),
                    dcc.Checklist(
                        id="checklist",
                        options=[{'label':  nome.replace("_"," "), 'value': nome} for nome in list(df_regioni.keys()[6:-2])],
                        value=default_lista, #['deceduti', 'variazione_totale_positivi','terapia_intensiva'],
                        labelStyle={'display': 'inline-block'}
                    ),  
                ],className="six columns pretty_container"),
                html.Div([
                    html.H3("Mappa"),
                    dcc.Graph(id='fig-map', figure=fig_map),
                    ], className="six columns pretty_container"),
            ], className="row"), 
        ])
        
    ],id="main")

@app.callback(dash.dependencies.Output('fig-reg', 'figure'),
    [dash.dependencies.Input('dropdown-regioni', 'value'),dash.dependencies.Input('checklist', 'value'),dash.dependencies.Input('radio-buttom-plot-style', 'value')])
def update_fig_reg(dropdown_regioni_value,checklist_value, plot_style_value):
    #print(checklist_value)
    fig_reg = fig_regioni(df_regioni, dropdown_regioni_value, checklist_value,plot_style_value)
    return fig_reg

if __name__ == '__main__':
    app.run_server(host="0.0.0.0") #,debug=True) #, host="0.0.0.0", port=8800)
