# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:54:24 2024

@author: Talifhani Khomola
"""
import plotly.graph_objects as go
import pandas as pd
Projects = pd.read_csv('Active Projects.csv')
Projects['Project Profit'] = (Projects['Revenue']/Projects['Revenue'].sum())*8947029#net profit from end of october to date
Projects['Scheduled Payment(2weeks)'] = (Projects['Revenue']/Projects['scheduled weeks'])*2
Projects['Scheduled Profit(2weeks)'] = Projects['Project Profit']/(Projects['scheduled weeks']/2)
Projects['Scheduled Expenditure(2weeks)'] = Projects['Scheduled Payment(2weeks)'] - Projects['Scheduled Profit(2weeks)']
ProjectD_data = Projects.iloc[[3]]
weeks = 16
revenue = 762500
expenditure = 529775
cumulative_revenue = []
cumulative_expenditure = []

for week in range(2, weeks + 1, 2):
    if cumulative_revenue:
        cumulative_revenue.append(cumulative_revenue[-1]+revenue)
        cumulative_expenditure.append(cumulative_expenditure[-1]+expenditure)
    else:
        cumulative_revenue.append(revenue)
        cumulative_expenditure.append(expenditure)
periods = list(range(2, weeks + 1,2))
def plot_function():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=periods, y=cumulative_revenue, mode='lines+markers', name='cumulative revenue', marker=dict(symbol='circle')))
    fig.add_trace(go.Scatter(x=periods, y=cumulative_expenditure, mode='lines+markers', name='cumulative expenditure', marker=dict(symbol='x')))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        title= 'Cumulative Revenue and Expenditure Over Time For Project D',
        xaxis_title='weeks',
        yaxis_title='Cumulative Amount (R)',
        legend_title= 'Legend',
    )
    return fig