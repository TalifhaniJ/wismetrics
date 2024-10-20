# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:45:33 2024

@author: Talifhani Khomola
"""

import pandas as pd
import re
import scipy
from scipy import signal
from scipy import interpolate
from datetime import datetime
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import plotly.graph_objects as go

bookings = pd.read_csv('bookings.csv', parse_dates=[1], index_col=[0])
Projects = pd.read_csv('Active Projects.csv')
bookings['dt'] = pd.to_datetime(bookings['dt'], format='%d/%m/%Y')
dailysales = bookings.groupby('dt')['Amount'].sum().reset_index()

monthlysales = bookings.set_index('dt')
monthly_sales = monthlysales['Amount'].resample('ME').sum()
monthly_sum = monthly_sales.sum()

daily_stats = dailysales.describe()
monthly_stats = monthly_sales.describe()
Monthly_revenue = monthly_sales.to_frame(name='Revenue')
Fixed_expenses = pd.read_csv('FixedExpenses.csv')
Monthly_revenue['Commission'] = Monthly_revenue['Revenue'] * 0.10
Monthly_revenue['Packages and Booking Fee'] = Monthly_revenue['Revenue'] * 0.40
Monthly_revenue['FixedExp'] = Fixed_expenses['Amount'].sum()
Monthly_revenue['net profit'] = Monthly_revenue['Revenue'] - (Monthly_revenue['Commission'] + Monthly_revenue['Packages and Booking Fee'] + Monthly_revenue['FixedExp'])
Monthly_revenue['production'] = monthlysales['Length of Stay'].resample('ME').sum()
def plot_function():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Monthly_revenue.index, y=Monthly_revenue['Revenue'], mode='lines+markers', name='Monthly Revenue', marker=dict(symbol='circle')))
    fig.add_trace(go.Scatter(x=Monthly_revenue.index, y=Monthly_revenue['Packages and Booking Fee'], mode='lines+markers', name='Operation Costs', marker=dict(symbol='diamond')))
    fig.add_trace(go.Scatter(x=Monthly_revenue.index, y=Monthly_revenue['Commission'], mode='lines+markers', name='Commission', marker=dict(symbol='x')))
    fig.add_trace(go.Scatter(x=Monthly_revenue.index, y=Monthly_revenue['net profit'], mode='lines+markers', name='Net Profit', marker=dict(symbol='star')))
    fig.add_trace(go.Scatter(x=Monthly_revenue.index, y=Monthly_revenue['FixedExp'], mode='lines+markers', name='Fixed Expenses', marker=dict(symbol='arrow')))
    fig.update_layout(
        title= 'Monthly Perfomance Dashboard',
        width=600,
        height=300,
        paper_bgcolor='rgba(0,0,0,0)',
        title_x = 0.8,
        xaxis_title='Time',
        yaxis_title='Amount (R)',
        legend_title= 'Legend',
    )
    return fig
    
