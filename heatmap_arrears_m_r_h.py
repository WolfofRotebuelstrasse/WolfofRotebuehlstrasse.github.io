from dash import dcc, html
import dash
import pandas as pd
import json
from urllib.request import urlopen
import plotly.graph_objects as go
token = "pk.eyJ1Ijoid29sZm9mcm90ZWJ1ZWhsc3RyYXNzZSIsImEiOiJjbGZtbXJ2a2YwZGowNDNvM2docjQ5YWY4In0.oSQQHrCp69ppmsXVLPetYw"


with urlopen('https://raw.githubusercontent.com/amcharts/amcharts4/master/dist/geodata/es2015/json/region/world/europeUltra.json') as response:
    counties = json.load(response)


df = pd.read_csv(
    "Clean_Dataset/clean_Arrears_mortgage_or_rent_utility_bills_or_hire_purchase.csv", sep=",")

# Create a list of unique years in the TIME_PERIOD column
years = df['TIME_PERIOD'].unique()

# Create a dictionary to map the year to the corresponding data
data_dict = {year: df[df['TIME_PERIOD'] == year] for year in years}


app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='choropleth', style={'height': '90vh'}),
        html.Div([
            dcc.Interval(id='interval-component',
                         interval=1000, n_intervals=0),
            html.Button('Start', id='start-button', n_clicks=0),
            html.Button('Stop', id='stop-button', n_clicks=0),
        ], style={'textAlign': 'center'}),
    ]),
    html.Div([
        dcc.Slider(
            id='year-slider',
            min=years.min(),
            max=years.max(),
            value=years.min(),
            marks={str(year): str(year) for year in years},
            step=None
        ),
    ], style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top'}),
])


@app.callback(
    dash.dependencies.Output('choropleth', 'figure'),
    [dash.dependencies.Input('year-slider', 'value'),
     dash.dependencies.Input('interval-component', 'n_intervals'),
     dash.dependencies.Input('start-button', 'n_clicks'),
     dash.dependencies.Input('stop-button', 'n_clicks')])
def update_figure(selected_year, n_intervals, start_clicks, stop_clicks):
    if start_clicks > stop_clicks:
        selected_year = years[n_intervals % len(years)]
    selected_data = data_dict[selected_year]
    zmin = selected_data['OBS_VALUE'].min()
    zmax = selected_data['OBS_VALUE'].max()
    fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=selected_data['geo'],
                                        z=selected_data['OBS_VALUE'], colorscale="Viridis",
                                        zmin=zmin, zmax=zmax, marker_line_width=0))
    fig.update_layout(mapbox_style="light", mapbox_accesstoken=token,
                      title=f"Comparison of house price index by country and year ({selected_year})",
                      mapbox_zoom=2.5, mapbox_center={"lat": 54, "lon": 15})
    fig.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0})
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, port = 6984)
