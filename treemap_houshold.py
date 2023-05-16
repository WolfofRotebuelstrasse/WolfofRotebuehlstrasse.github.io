import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

# Load dataset
df_treemap = pd.read_csv("Clean_Dataset/clean_Share_of_housing_costs_in_disposable_household_income.csv")

# create list of all available country options, including "All"
country_options = [{'label': 'Alle', 'value': 'All'}] + [{'label': country, 'value': country} for country in df_treemap["geo"].unique()]
# create list of all available household options
household_options = [{'label': household, 'value': household} for household in df_treemap["incgrp"].unique()]

# Define function to filter the data for the selected countries and year
def filter_data_treemap(countries, year, household):
    filtered_df_treemap = df_treemap[df_treemap["TIME_PERIOD"] == year]
    filtered_df_treemap = filtered_df_treemap[filtered_df_treemap["incgrp"] == household]
    if 'All' not in countries:
        filtered_df_treemap = filtered_df_treemap[filtered_df_treemap["geo"].isin(countries)]
    return filtered_df_treemap

# create function to update the treemap
def update_treemap(countries, year, household):
    filtered_df_treemap = filter_data_treemap(countries, year, household)
    max_obs_value = filtered_df_treemap['OBS_VALUE'].max()
    fig_treemap = go.Figure(go.Treemap(
        labels=filtered_df_treemap["geo"],
        parents=["World"] * len(filtered_df_treemap["geo"]),
        values=filtered_df_treemap["OBS_VALUE"],
        textinfo="label+value",
        marker=dict(
            colors=filtered_df_treemap["OBS_VALUE"],
            colorscale='Bluered',
            reversescale=True,
            showscale=True,
            cmid=0,
            cmin=0,
            cmax=max_obs_value),
        hovertemplate='<b>%{label}</b><br>Value: %{value}'
    ))
    fig_treemap.update_layout(
        title="Treemap",
        margin=dict(l=10, r=10, t=40, b=10),
        height=700
    )
    return fig_treemap


# Define the app layout
layout = html.Div([
    dcc.Graph(id="treemap-graph"),
    dcc.Dropdown(id="country-dropdown", options=country_options, value=['All'], multi=True),
    dcc.Dropdown(id="household-dropdown", options=household_options, value='TOTAL'),
    dcc.Slider(id="year-slider", min=df_treemap["TIME_PERIOD"].min(), max=df_treemap["TIME_PERIOD"].max(),
               value=df_treemap["TIME_PERIOD"].max(), marks={str(year): str(year) for year in df_treemap["TIME_PERIOD"].unique()})
])

# creat figure
fig_treemap = go.Figure()

# callback function to update the treemap
@app.callback(
    Output("treemap-graph", "figure"),
    Input("country-dropdown", "value"),
    Input("year-slider", "value"),
    Input("household-dropdown", "value")
)
def update_figure_treemap(countries, year, household):
    return update_treemap(countries, year, household)

# create app layout
app.layout = layout

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, port = 6986)