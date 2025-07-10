# Import packages 

import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
# Load and filter the data
df = pd.read_csv('/Users/Marcy_Student/Desktop/marcy/DA2025_Lectures_Kevin/Mod2/data/sports.csv')
df = df[["sports", "rev_men", "rev_women"]].dropna()

# Pick 5 sports
top5 = ['Basketball', 'All Track Combined', 'Tennis', 'Golf', 'Soccer']
#Copying the dataframe to not overwrite the original 
df_5 = df[df["sports"].isin(top5)].copy()

# Create new column called Total_Revenue that adds up the men and women's revenue columns

df_5["Total_Revenue"] = df_5['rev_men'].sum() + df_5['rev_women'].sum()

# Make your pie or scatteplot using plotly 

fig = px.pie(df_5, values='Total_Revenue', names='sports', title='Total Revenue By Sport')


# Make the App -- DO NOT RUN THIS CELL YET It may give you a "port already in use error if you do"

app = dash.Dash(__name__)
app.title = 'Distribution of Sports Revenue'

app.layout = html.Div([
    html.H1("Revenue Analysis for 5 Sports", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)