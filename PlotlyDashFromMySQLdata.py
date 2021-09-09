import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import cdata.mysql as mod
import plotly.graph_objs as go

cnxn = mod.connect("User=python;Password=Travail_Maturite2021;Database=statistiques;Server=localhost;Port=3306;")

#Execute SQL to MySQL
df = pd.read_sql("SELECT Total, SS FROM divorce", cnxn)

#Configure the Web App
app_name = 'dash-mysqledataplot'
 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Suisse Stats'

#Configure the Layout
trace = go.Bar(x=df.Total, y=df.SS, name='Total')
 
app.layout = html.Div(children=[html.H1("Suisse Stats", style={'textAlign': 'center'}),
dcc.Graph(
id='example-graph',
figure={
'data': [trace],
'layout':
go.Layout(title='Divorces', barmode='stack')
})
], className="container")

#Set the App to Run
if __name__ == '__main__':
    app.run_server(debug=True)

print('Successful!')
