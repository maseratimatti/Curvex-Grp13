import dash
from dash import html
from dash import dcc 
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


githubpath = './data/'

df = pd.read_excel(githubpath + "Curvexdashdata.xlsx")

app = dash.Dash()

app.layout = html.Div([ 
])

fig = px.line(df, x="Tidspunkt", y="Måling", title="Stress") 
fig.show()

if __name__ == '__main__':
    app.run_server()
