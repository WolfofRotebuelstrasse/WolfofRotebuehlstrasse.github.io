import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

# Load dataset
df_bar_deg = pd.read_csv("Clean_Dataset/clean_Housing_cost_overburden_rate_by_degree_of_urbanisation.csv", sep=",")

# Create list of all available geo options, including "All Geo"
all_geo_options_bar_deg = [{"label": "All countries", "value": "All Geo"}] + \
                  [{"label": geo, "value": geo} for geo in df_bar_deg["geo"].unique()]

# Create list of all available year options, including "All Years"
all_year_options_bar_deg = [{"label": "All years", "value": "All Years"}] + \
                   [{"label": year, "value": year} for year in df_bar_deg["TIME_PERIOD"].unique()]

# Create list of all available deg options
all_deg_options = [{"label": "Cities", "value": "DEG1"}, {"label": "Rural areas", "value": "DEG3"}]

# Create initial list of selected geo options, excluding "All Geo"
selected_geo_options_bar_deg = [geo for geo in df_bar_deg["geo"].unique()]

# Create initial list of selected year options, excluding "All Years"
selected_year_options_bar_deg = [year for year in df_bar_deg["TIME_PERIOD"].unique()]

# Create initial list of selected DEG options
selected_deg_options = ["DEG1", "DEG3"]

# Initialize figure
fig_bar_deg = go.Figure()



# Create dropdown menus
dropdowns = html.Div([
    html.Label("Select Country:"),
    dcc.Dropdown(
        id="geo-dropdown-bar-deg",
        options=all_geo_options_bar_deg,
        value=selected_geo_options_bar_deg,
        multi=True
    ),
    html.Br(),
    html.Label("Select Year:"),
    dcc.Dropdown(
        id="year-dropdown-bar-deg",
        options=all_year_options_bar_deg,
        value=selected_year_options_bar_deg,
        multi=True
    ),
    html.Br(),
    html.Label("Select Household:"),
    dcc.Dropdown(
id="deg-dropdown",
options=all_deg_options,
value=selected_deg_options,
multi=True
),
html.Br()
])

#Define app layout
app.layout = html.Div([
dropdowns,
dcc.Graph(id="bar-chart")
])

#Define callback function
@app.callback(
Output("bar-chart", "figure"),
[Input("geo-dropdown-bar-deg", "value"),
Input("year-dropdown-bar-deg", "value"),
Input("deg-dropdown", "value")])

def update_bar_chart(geo_dropdown_value, year_dropdown_value, deg_dropdown_value):
    
# Filter dataframe based on selected geo options, year options, and deg options
    df_filtered = df_bar_deg[df_bar_deg["geo"].isin(geo_dropdown_value) & df_bar_deg["TIME_PERIOD"].isin(year_dropdown_value) & df_bar_deg["deg_urb"].isin(deg_dropdown_value)]

# Initialize figure
    fig_bar_deg = go.Figure()
    
    # Filter dataframe based on selected geo options, year options, and deg options
    if "All Geo" in geo_dropdown_value:
        df_filtered = df_bar_deg.copy()
    else:
        df_filtered = df_bar_deg[df_bar_deg["geo"].isin(geo_dropdown_value)]

    if "All Years" in year_dropdown_value:
        df_filtered = df_filtered.copy()
    else:
        df_filtered = df_filtered[df_filtered["TIME_PERIOD"].isin(
            year_dropdown_value)]
        
    # Create trace for each selected deg option
    for deg in deg_dropdown_value:
        if deg == "All DEG":
            df_deg = df_filtered[df_filtered["deg_urb"].isin(["DEG1", "DEG3"])]
            fig_bar_deg.add_trace(
                go.Bar(
                    x=df_deg["geo"] + " " + df_deg["TIME_PERIOD"].astype(str),
                    y=df_deg["OBS_VALUE"],
                    name=deg
                )
            )
        else:
            df_deg = df_filtered[df_filtered["deg_urb"] == deg]
            fig_bar_deg.add_trace(
                go.Bar(
                    x=df_deg["geo"] + " " + df_deg["TIME_PERIOD"].astype(str),
                    y=df_deg["OBS_VALUE"],
                    name=deg
                )
            )

    # Update figure layout
    fig_bar_deg.update_layout(
        title="Housing cost overburden: cities or rural area in %",
        xaxis_title="Years",
        yaxis_title="Housing costs in %"
    )

    return fig_bar_deg

# Run app
allow_duplicate = True
if __name__ == '__main__':
    app.run_server(debug=True, port = 6982)

