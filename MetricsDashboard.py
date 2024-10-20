# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:04:25 2024

@author: Talifhani Khomola
"""

import dash
import pandas as pd
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
from dash import dash_table
from Analytics import Fixed_expenses
import Analytics
import econ
import ProjectA
import ProjectB
import ProjectC
import ProjectD
import ProjectE
from functions import Revenue_data, Profit_data

Overviewfig = Analytics.plot_function()
breakeven = econ.plot_breakeven()
revenue = econ.plot_revenue()
profit = econ.plot_profit()
revunits = econ.plot_revunits()
app = dash.Dash(__name__)
app.title = 'WIS Metrics'
app.layout = dbc.Container([
            html.Div([
                html.H1('Cashflow Analysis',
                        style={'color':'#0097a7', "margin-top":"-8px", "width":"1290px", "margin-left":"1px","height":"50px",  "border-radius":"15px",
                               "text-align":"center", "border":"90px solid #333333","border-top":"10px","border-bottom":"10px","background":"#333333"}),
                dcc.Tabs([
                    dcc.Tab(label="Overview", children=[
                        html.H2 ('Economic Models', style={'margin-left':'950px'}),
                        html.Ul([
                        dbc.Button(id="B1", children="Break even", n_clicks=0, color="primary", className="mt-4", style={'margin':'3px'}), 
                        dbc.Button(id="B2", children="Costs PU", n_clicks=0, color="primary", className="mt-4", style={'margin':'3px'}),
                        dbc.Button(id="B3", children="Profit Margin", n_clicks=0, color="primary", className="mt-4", style={'margin':'3px'}),
                        dbc.Button(id="B4", children="Revenue PU", n_clicks=0, color="primary", className="mt-4", style={'margin':'3px'})],style={'margin-left':'825px'}),
                        
                        dcc.Graph(id='graph2',
                              style={'width':'740px','margin-right':'50px', 'height':'390px', "flex":"1","float":"right","margin-top":"20px"}),
                        html.H2 ('Monthly Fixed Expenses', style={'margin-left':'200px',"margin-top":"-87px"}),
                        html.Ul([dash_table.DataTable(id='table', columns=[{'name':col, 'id':col} for col in Fixed_expenses.columns], data=Fixed_expenses.to_dict('records'), style_header={
                            'backgroundColor':'grey',"text-align":"center"},style_cell={'width':'1000px','whiteSpace':'normal'}, style_data={'height':'auto',"text-align":"left"})], style={'width':'400px','margin-left':'100px'}),
                        dcc.Graph(id='graph1',
                                  figure = Overviewfig,style={"margin-top":"-8px"}),
                        
                        ]),
                    dcc.Tab(label="Active Projects", children=[
                        html.Iframe(id='projects-map', srcDoc=open('projects.html', 'r').read(), style={"width":"45%", "height":"600px", "flex":"1","float":"left"}),
                        dcc.Graph(id='graph', style={'width':'650px', 'height':'400px','margin-left':'660px'}),
                                    dbc.Button(id="Pr-A", children="Project A", n_clicks=0, color="primary", className="mt-4", style={'margin':'3px'}), 
                                    dbc.Button(id="Pr-B", children="Project B", n_clicks=0, color="primary", className="mt-4", style={'margin':'3px'}),
                                    dbc.Button(id="Pr-C", children="Project C", n_clicks=0, color="primary", className="mt-4", style={'margin':'3px'}),
                                    dbc.Button(id="Pr-D", children="Project D", n_clicks=0, color="primary", className="mt-4", style={'margin':'3px'}),
                                    dbc.Button(id="Pr-E", children="Project E", n_clicks=0, color="primary", className="mt-4", style={'margin':'3px'}),
                                        html.H2 ('Project Financial Breakdown'),
                                        html.Div(id="Rev1"),
                                        html.Div(id="Profit")
                        
                        
                        ], style={"width": "50%","flex":"1", "display": "inline-block", "horizontal-align":"top","float":"left"})
                    ], style={"border-style":"solid","margin-left":"35%", "border-color":"grey","width":"35%","margin-top":"-15px"}),
                    ]),

], style={"backgroundColor":"#e5ecf6", "border-radius":"5px"})
@app.callback(
    Output('graph2', 'figure'),
    [Input('B1', 'n_clicks'),
     Input('B2', 'n_clicks'),
     Input('B3', 'n_clicks'),
     Input('B4', 'n_clicks')]
    )
def update_graph1(n_clicks1, n_clicks2, n_clicks3, n_clicks4):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'B4'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'B1':
        fig = econ.plot_breakeven()
    elif button_id == 'B2':
        fig = econ.plot_revenue()
    elif button_id == 'B3':
        fig = econ.plot_profit()
    elif button_id == 'B4':
        fig = econ.plot_revunits()
    return fig
@app.callback(
    Output('graph', 'figure'),
    Output('Rev1', 'children'),
    Output('Profit', 'children'),
    [
     Input('Pr-A', 'n_clicks'),
     Input('Pr-B', 'n_clicks'),
     Input('Pr-C', 'n_clicks'),
     Input('Pr-D', 'n_clicks'),
     Input('Pr-E', 'n_clicks')]
    )
def update_graph(n_clicks5, n_clicks6, n_clicks7, n_clicks8, n_clicks9):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'Pr-A'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'Pr-A':
        fig = ProjectA.plot_function()
    elif button_id == 'Pr-B':
        fig = ProjectB.plot_function()
    elif button_id == 'Pr-C':
        fig =  ProjectC.plot_function()
    elif button_id == 'Pr-D':
        fig = ProjectD.plot_function()
    elif button_id == 'Pr-E':
        fig = ProjectE.plot_function()
    Revtext = f"Revenue for this project is R{Revenue_data[button_id]}"  
    Proftext = f"Profit modelled for this project is R{Profit_data[button_id]}" 
    return fig, Revtext, Proftext
   
if __name__ == '__main__':
    app.run_server()
    
