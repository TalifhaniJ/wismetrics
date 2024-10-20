import pandas as pd
Projects = pd.read_csv('Active Projects.csv')
Projects['Project Profit'] = (Projects['Revenue']/Projects['Revenue'].sum())*8947029#net profit from end of october to date
Projects['Scheduled Payment(2weeks)'] = (Projects['Revenue']/Projects['scheduled weeks'])*2
Projects['Scheduled Profit(2weeks)'] = Projects['Project Profit']/(Projects['scheduled weeks']/2)
Projects['Scheduled Expenditure(2weeks)'] = Projects['Scheduled Payment(2weeks)'] - Projects['Scheduled Profit(2weeks)']
ProjectA_data = Projects.iloc[[0]]

ID1 = {
      'ids_column': ['Pr-A', 'Pr-B','Pr-C','Pr-D','Pr-E'],
      'Values': Projects['Revenue']}

df1 = pd.DataFrame(ID1)
Revenue_data = dict(zip(df1['ids_column'], df1['Values']))

ID2 = {
      'ids_column': ['Pr-A', 'Pr-B','Pr-C','Pr-D','Pr-E'],
      'Values': Projects['Project Profit']}

df2 = pd.DataFrame(ID2)
Profit_data = dict(zip(df2['ids_column'], df2['Values']))