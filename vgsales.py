import dash 
import plotly.express as px 
import pandas as pd 
import dash_html_components as html
import dash_core_components as dcc 
from dash.dependencies import Output, Input

# Data Exploration  With Pandas 
# ------------------------------------------------------------------

df = pd.read_csv("vgsales.csv")

#print(df[:5])
#print(df.iloc[:5, [1,3,4,7,8,10]])
#print(df.loc[:5,["NA_Sales"]])

#print(df.Genre.nunique())
#print(df.Genre.unique())
#print(sorted(df.Year.unique()))

# Data Visualization With Plotly 
# ------------------------------------------------------------------

#fig_pie = px.pie(df, 'Genre','Global_Sales')
#fig_pie.show()

#fig_bar = px.bar(df, x = 'Genre',y='Global_Sales')
#fig_bar.show()

#fig_hist = px.histogram(df, x = 'Year',y='Global_Sales')
#fig_hist.show()

# Interactive Graphing With Dash 
# ------------------------------------------------------------------

#app = dash.Dash(__name__)

#app.layout = html.Div([
#    html.H1("Graph Analysis With Israa"),
#     dcc.Dropdown(id = 'genre-choice',
#                 options = [{'label':x, 'value':x}
#                             for x in sorted(df.Genre.unique())],
#                  value = 'Action',
#                  style = {'width':'50%'}
#                  ),
#    dcc.Dropdown(id ='platform-choice',
#                  options = [{'label':x, 'value':x}
#                             for x in sorted(df.Platform.unique())],
#                  value='PS4',
#                  style={'width':'50%'}
#                  ),
#    dcc.Graph(id='my-graph',
#              figure={}),            
#])
#@app.callback(
#    Output(component_id='my-graph', component_property='figure'),
#    Input(component_id='genre-choice', component_property='value'),
#    Input(component_id='platform-choice', component_property='value')
#)
#def interactive_graphs(value_genre, value_platform):
#    dff = df[df.Genre==value_genre]
#    dff = dff[dff.Platform==value_platform]
#    fig = px.bar(data_frame=dff, x = 'Year',y='Global_Sales')
#    return fig   

#if __name__ =='__main__':
#    app.run_server()