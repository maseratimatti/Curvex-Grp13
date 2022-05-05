import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import dash_table
import pandas as pd
import plotly_express as px
import plotly.offline as pyo

githubpath = './data/'

df = pd.read_excel(githubpath + "Curvexdashdata.xlsx")

app = dash.Dash()

app.layout = html.Div([ 

fig = px.line(df, x="Tidspunkt", y="Måling", title="Stress") 
fig.show()
])

if __name__ == '__main__':
    app.run_server()
