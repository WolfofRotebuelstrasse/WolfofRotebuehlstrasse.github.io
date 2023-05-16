import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

# Load dataset
df = pd.read_csv(
    "Clean_Dataset/clean_ppp.csv", sep=",")

# Create list of all available geo options, including "All Geo"
all_geo_options = [{"label": "All Geo", "value": "All Geo"}] + \
                  [{"label": geo, "value": geo} for geo in df["geo"].unique()]

# Create list of all available year options, including "All Years"
all_year_options = [{"label": "All Years", "value": "All Years"}] + \
                   [{"label": year, "value": year}
                       for year in df["TIME_PERIOD"].unique()]

# Create list of all unique years
unique_years = list(set(df["TIME_PERIOD"].tolist()))

# Create a list of dictionaries with year as both the label and value
year_options = [{"label": year, "value": year} for year in unique_years]

# Replace all_year_options with year_options
all_year_options = [{"label": "All Years",
                     "value": "All Years"}] + year_options


# Create initial list of selected geo options, excluding "All Geo"
selected_geo_options = [geo for geo in df["geo"].unique()]

# Create initial list of selected year options, excluding "All Years"
selected_year_options = [year for year in df["TIME_PERIOD"].unique()]

# Initialize figure
fig = go.Figure()

# Create trace for each selected geo option and year option
for geo in selected_geo_options:
    for year in selected_year_options:
        df_geo_year = df[(df["geo"] == geo) & (df["TIME_PERIOD"] == year)]
        fig.add_trace(
            go.Bar(
                x=[str(geo) + " " + str(year)],

                y=df_geo_year["OBS_VALUE"],
                name=geo + " " + str(year)

            )
        )
# Create dropdown menu
dropdown = dcc.Dropdown(
    id="geo-dropdown",
    options=all_geo_options,
    value=selected_geo_options,
    multi=True,
    style={"width": "400px"},
)


# Define callback function for updating figure based on dropdown selection


@app.callback(
    Output("bar-chart", "figure"),
    Input("geo-dropdown", "value"),
    Input("year-dropdown", "value"),
    allow_duplicate=True,
    prevent_initial_call=True
)
def update_figure(selected_geo_options, selected_year_options):
    # Initialize figure
    fig = go.Figure()

    # If "All Geo" is selected, add trace for each geo option
    if "All Geo" in selected_geo_options:
        selected_geo_options = [geo for geo in df["geo"].unique()]

    # If "All Years" is selected, add trace for each year option
    if "All Years" in selected_year_options:
        selected_year_options = [year
                                 for year in df["TIME_PERIOD"].unique()]

    # Add trace for each selected geo option and year option
    for geo in selected_geo_options:
        for year in selected_year_options:
            df_geo_year = df[(df["geo"] == geo) & (df["TIME_PERIOD"] == year)]
            fig.add_trace(
                go.Bar(
                    x=[str(geo) + " " + str(year)],
                    y=df_geo_year["OBS_VALUE"],
                    name=geo + " " + str(year)
                )
            )

    # Update layout
    fig.update_layout(
        title="Housing includes water, electricity, gas and other fuels.",
        xaxis_title="Country and year",
        yaxis_title="Price index EU = 100"
    )

    # Return the updated figure
    return fig

# Define app layout
app.layout = html.Div([
    html.H1("Price levels for housing"),
    html.Div([
        html.Label("Select country"),
        dcc.Dropdown(
            id="geo-dropdown",
            options=all_geo_options,
            value=selected_geo_options,
            multi=True
        )
    ]),
    html.Div([
        html.Label("Select year"),
        dcc.Dropdown(
            id="year-dropdown",
            options=all_year_options,
            value=selected_year_options,
            multi=True
        )
    ]),
  

    html.Div([
        dcc.Graph(
            id="bar-chart",
            figure=fig

        )
    ]),



])

# Run app
allow_duplicate = True
if __name__ == '__main__':
    app.run_server(debug=True, port = 6983)
