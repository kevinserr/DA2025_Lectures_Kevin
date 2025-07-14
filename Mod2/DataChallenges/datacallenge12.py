import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load and clean data
df = pd.read_csv('/Users/Marcy_Student/Desktop/marcy/DA2025_Lectures_Kevin/Mod2/data/indian_food.csv').dropna()


# Create app
app = dash.Dash(__name__)
app.title = "Indian Food"

fig = px.scatter(df, x='prep_time', y='cook_time',color='course',
                 title='Prep Time vs Cook Time by Course',
                 hover_data=['name'])


app.layout = html.Div([
    html.H1("Indian Food Visual Storytelling"),
    html.Div([
        dcc.Dropdown(
            id='course-filter',
            options=[{'label': r, 'value': r} for r in sorted(df['course'].unique())],
            placeholder="Select a course",
            style={'width': '50%'},
        )
    ], style={'display': 'flex', 'justifyContent': 'center', 'marginBottom': '20px'}),
    dcc.Graph(id ='scatter_plot', figure=fig),
])

@app.callback(
    Output('scatter_plot', 'figure'),
    Input('course-filter', 'value')
)
def update_chart(course):
    filtered = df[df['course']==course] if course else df
    fig2 = px.scatter(filtered, x = 'prep_time', y='cook_time', color='course',
                     title='Prep Time Vs Cook Time by Course', hover_data=['name'])
    return fig2

if __name__ == "__main__":
    app.run(debug=True)
