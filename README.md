# Data visualization Course Final Project

Dashboard realizzata usando la libreria Dash Plotly 
* [Heroku Websiste]()
* [Github Link page (Readme.md)](https://visiont3lab.github.io/data-visualization-final-project/)
* Il materiale del corso di data visualization si trova nel repositorio [data-visualization](https://github.com/visiont3lab/data-visualization)
* Cliccare questo link per provare e modicare la dashboard 
[![Run on Repl.it](https://repl.it/badge/github/visiont3lab/covid19-dash-plotly)](https://repl.it/github/visiont3lab/data-visualization-final-project)
* [plotly-dash-boilerplate](https://github.com/visiont3lab/plotly-dash-boilerplate) è un boilerplate project disegnato per iniziare a programmare usando plotly e dash


Dati della protezione civile disponibili qui:

* [Dati COVID-19 Italia](https://github.com/pcm-dpc/COVID-19)
* [Covid World Data](https://github.com/open-covid-19/data)

## Installazzione

*   Python setup

    [Reference Dash Deploy](https://dash.plotly.com/deployment)
    
    ```
    cd data-visualization-final-project
    virtualenv env # creates a virtualenv called "env"
    source env/bin/activate # uses the virtualenv
    pip install -r requirements.txt
    ```

## Applicazione

* L'applicazione finale si trova nel file python **app.py**. Quest'ultima sarà quella che verrà esposta affinchè tutti possano vederla. 
* Al fine di svilupparla abbiamo diviso l'applicato in 5 parti.
    * **step1.py** : layout initiziale (css) e dcc.Markdown() componente 
    * **step2.py** : dash_table.DataTable() e dcc.Graph() componenti (line and area plot)
    * **step3.py** : dcc.Dropdown() e concetto di callback applicato al dcc.Graph() (line e bar plot)
    * **step4.py** : dcc.RadioItems(), dcc.CheckLists() che interagisco mediante una callback con un dcc.Graph()
    * **step5.py** : utilizziamo plotly go.Scattermapbox() per realizzare una mappa con cui possiamo interagire
    * **app.py** : applicazione finale pronta per il deploy (essere fatta vedere a tutti)
     
## File Importanti

* **Applicazione**
    * **assets** : cartella che contiene i file di css (layout) utilizzati per sviluppare la dashboard
    * **requirements.txt** : dipendenze python necessarie per la nostra dashboard (specifiche per il **pip** package manager)
    * **app.py** : applicazione finale 
* [**replit**](https://repl.it/)
    * **.replit** : file associato al **RUN** button in replit
    * **pyproject.toml** :  dipendenze python necessarie per la nostra dashboard (specifiche per il **poetry** package manager che utilizza replit)
    * **runtime.txt** : specifica la versione di python da utilizzare in replit
* [**Heroku**](https://www.heroku.com/)
    * **Procfile** : file necessario a heroku per capire quale file python utilizzare. Nel nostro caso **app.py**

## References

* [dash components e tutorial](https://dash.plotly.com/)
* [dash-heroku-template](https://github.com/plotly/dash-heroku-template)
* [plotly figure reference](https://plotly.com/python/reference/)
* [dash data_table](https://dash.plotly.com/datatable)
* [Maps Plotly](https://plotly.com/python/maps/), [Mapbox Map Layers](https://plotly.com/python/mapbox-layers/)
* [heroku cli](https://devcenter.heroku.com/articles/heroku-cli), [heroku cli Logs](https://devcenter.heroku.com/articles/logging#view-logs)
* [Color Palette Selector Adobe online ](https://coolors.co/1c5253-388659-00ce7f-33658a-86bbd8)
* [How to build an app with Dash Plotly](https://www.statworx.com/de/blog/how-to-build-a-dashboard-in-python-plotly-dash-step-by-step-tutorial/)
