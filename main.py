import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('sales_data.csv')

sales_data = df.groupby(['Product'])['Sales'].sum()

fig = go.Figure([go.Bar(x=sales_data.index, y=sales_data.values)])

fig.update_layout(
    title='Total Sales by Product',
    xaxis_title='Product',
    yaxis_title='Sales'
)
fig.show()
