import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

# Load dataset
dataset_options = [{'label': 'House price evolution', 'value': 'Clean_Dataset/clean_House_price_index_annual.csv'},    {'label': 'Rent evolution','value': 'Clean_Dataset/clean_hicp.csv'},    {'label': 'Total inflation', 'value': 'Clean_Dataset/clean_hicp_inflation.csv'}]

selected_dataset = dataset_options[0]['value']

df = pd.read_csv(selected_dataset, sep=',')

# Create list of all available geo options, including "All Geo"
all_geo_options = [{"label": "All Geo", "value": "All Geo"}] + \
                  [{"label": geo, "value": geo} for geo in df["geo"].unique()]

# Create initial list of selected geo options, excluding "All Geo"
selected_geo_options = [geo for geo in df["geo"].unique()]

# Initialize figure
fig = go.Figure()

# Create trace for each selected geo option
for geo in selected_geo_options:
    df_geo = df[df["geo"] == geo]
    fig.add_trace(
        go.Scatter(
            x=df_geo["TIME_PERIOD"],
            y=df_geo["OBS_VALUE"],
            name=geo,
            line=dict(width=2),
        )
    )



def update_figure(selected_dataset, selected_options):
    # Load data from selected dataset
    df = pd.read_csv(selected_dataset, sep=',')

    # Clear all traces from figure
    fig.data = []

    # If "All Geo" is selected, add trace for each geo option
    if "All Geo" in selected_options:
        selected_options = [geo for geo in df["geo"].unique()]

    # Add trace for each selected geo option
    for geo in selected_options:
        df_geo = df[df["geo"] == geo]
        fig.add_trace(
            go.Scatter(
                x=df_geo["TIME_PERIOD"],
                y=df_geo["OBS_VALUE"],
                name=geo,
                line=dict(width=2),
            )
        )

    # Update layout
    fig.update_layout(
        title="Evolution of house prices, rents and inflation in the eu by country and year",
        xaxis_title="Years",
        yaxis_title="2015 = 100",
        template="plotly_white",
    )
    return fig


# Create dropdown menu
dropdown = dcc.Dropdown(
    id="geo-dropdown",
    options=all_geo_options,
    value=selected_geo_options,
    multi=True,
    style={"width": "400px"},
)
dataset_dropdown = dcc.Dropdown(
    id='dataset-dropdown',
    options=dataset_options,
    value=dataset_options[0]['value']
)

# Create selected options indicator
selected_options_indicator = html.P(
    id="selected-options-indicator",
    children="Selected options: {}".format(", ".join(selected_geo_options)),
)

# Define callback function for updating selected options indicator


@app.callback(
    Output("selected-options-indicator", "children"),
    Input("geo-dropdown", "value"),
    prevent_initial_call=True
)
def update_selected_options_indicator(selected_options):
    return "Selected options: {}".format(", ".join(selected_options))

# Define callback function for updating figure when dropdown selection changes


@app.callback(
    Output("line-chart", "figure", allow_duplicate=True),
    Input("geo-dropdown", "value"),
    Input("dataset-dropdown", "value"),
    prevent_initial_call=True
)
def update_chart(selected_options, selected_dataset):
    update_figure(selected_dataset, selected_options)
    return fig


# Create layout with dropdown menu, selected options indicator, chart, and reset button
app.layout = html.Div(
    [html.H1("Evolution of house prices, rents and inflation in the eu by country and year"),
        html.Div([dropdown, selected_options_indicator]
                 ), html.Div([dataset_dropdown]),

        html.Div([dcc.Graph(id="line-chart", figure=fig)])]
)

# Run app
allow_duplicate = True
if __name__ == '__main__':
    app.run_server(debug=True, port = 6985)
