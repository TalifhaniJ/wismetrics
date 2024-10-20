# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 15:22:03 2024

@author: Talifhani Khomola
"""
import numpy as np
import pandas as pd
from Analytics import Monthly_revenue
import plotly.graph_objects as go

Monthly_revenue['Profit Margin'] = (Monthly_revenue['net profit']/Monthly_revenue['Revenue'])*100
Monthly_revenue['Total Costs'] = Monthly_revenue['Commission']+Monthly_revenue['Packages and Booking Fee']+Monthly_revenue['FixedExp']
Monthly_revenue['Cost Per Production Unit'] = Monthly_revenue['Total Costs']/Monthly_revenue['production']
Monthly_revenue['Revenue per Production Unit'] = Monthly_revenue['Revenue']/Monthly_revenue['production']
Monthly_revenue['variable costs'] = Monthly_revenue['Commission']+Monthly_revenue['Packages and Booking Fee']
Monthly_revenue['Break-even Units'] = Monthly_revenue['FixedExp']/(Monthly_revenue['Revenue per Production Unit']-Monthly_revenue['variable costs'])

def plot_breakeven():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Monthly_revenue['Break-even Units'], y=Monthly_revenue['Revenue'], mode='lines', name='Revenue', marker=dict(symbol='circle')))
    fig.add_trace(go.Scatter(x=Monthly_revenue['Break-even Units'], y=Monthly_revenue['Total Costs'], mode='lines', name='Total Costs', marker=dict(symbol='circle')))
    fig.add_trace(go.Scatter(x=Monthly_revenue['Break-even Units'], y=Monthly_revenue['FixedExp'], mode='lines', name='Fixed Expenditure', marker=dict(symbol='circle')))
    fig.update_layout(
        width =750,
        height=400,
        title= 'Break-even Analysis',
        title_x = 0.5,
        xaxis_title='production units',
        yaxis_title='Amount (R)',
        legend_title= 'Legend',
    )
    return fig
def plot_revenue():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Monthly_revenue['production'], y=Monthly_revenue['Cost Per Production Unit'], mode='markers', name='cost per production', marker=dict(symbol='diamond-dot')))
    fig.update_layout(
        width =750,
        height=400,
        title= 'total costs per production unit',
        title_x = 0.5,
        xaxis_title='production units',
        yaxis_title='Amount (R)',
        legend_title= 'Legend',
    ) 
    return fig
def plot_profit():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Monthly_revenue['Revenue'], y=Monthly_revenue['Profit Margin'], mode='markers', name='Profit Margin', marker=dict(symbol='diamond-dot')))
    fig.update_layout(
        width =750,
        height=400,
        title= 'Profit Margin',
        title_x = 0.5,
        xaxis_title='Revenue (R)',
        yaxis_title='Amount (%)',
        legend_title= 'Legend',
    )
    return fig

def plot_revunits():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Monthly_revenue['production'], y=Monthly_revenue['Revenue per Production Unit'], mode='markers', name='revenue per production', marker=dict(symbol='diamond-dot')))
    fig.update_layout(
        width =750,
        height=400,
        title= 'Revenue Per Production Units',
        title_x = 0.5,
        xaxis_title='production units',
        yaxis_title='Amount (R)',
        legend_title= 'Legend',
    )
    return fig