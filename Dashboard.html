from dash import dcc, html
import dash
import json
from urllib.request import urlopen
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

##########################################################################################################################################################
# Linechart
##########################################################################################################################################################

# Load dataset
dataset_options = [{'label': 'House price evolution', 'value': 'Clean_Dataset/clean_House_price_index_annual.csv'},    {'label': 'Rent evolution',
                                                                                                                        'value': 'Clean_Dataset/clean_hicp.csv'},    {'label': 'Total inflation', 'value': 'Clean_Dataset/clean_hicp_inflation.csv'}]
selected_dataset = dataset_options[0]['value']
df_line = pd.read_csv(selected_dataset, sep=',')

# Create list of all available geo options, including "All Geo"
all_geo_options_line = [{"label": "All Countries", "value": "All Geo"}] + \
    [{"label": geo, "value": geo} for geo in df_line["geo"].unique()]

# Create initial list of selected geo options, excluding "All Geo"
selected_geo_options_line = [geo for geo in df_line["geo"].unique()]

# Initialize figure
fig_line = go.Figure()

# Create trace for each selected geo option
for geo in selected_geo_options_line:
    df_geo = df_line[df_line["geo"] == geo]
    fig_line.add_trace(
        go.Scatter(
            x=df_geo["TIME_PERIOD"],
            y=df_geo["OBS_VALUE"],
            name=geo,
            line=dict(width=2),
        )
    )

  # Update layout
    fig_line.update_layout(
        title="Evolution of house prices, rents and inflation in the eu by countries and years in %",
        xaxis_title="Years",
        yaxis_title="2015 = 100%",
        template="plotly_white",
    )
# update figure


def update_figure_line(selected_dataset, selected_options_line):

    # Load data from selected dataset
    df_line = pd.read_csv(selected_dataset, sep=',')

    # Clear all traces from figure
    fig_line.data = []

    # If "All Geo" is selected, add trace for each geo option
    if "All Geo" in selected_options_line:
        selected_options_line = [geo for geo in df_line["geo"].unique()]

    # Add trace for each selected geo option
    for geo in selected_options_line:
        df_geo = df_line[df_line["geo"] == geo]
        fig_line.add_trace(
            go.Scatter(
                x=df_geo["TIME_PERIOD"],
                y=df_geo["OBS_VALUE"],
                name=geo,
                line=dict(width=2),
            )
        )

    return fig_line


# Create dropdown menu
dropdown_line = dcc.Dropdown(
    id="geo-dropdown-line",
    options=all_geo_options_line,
    value=selected_geo_options_line,
    multi=True,
    style={"width": "400px"},
)
dataset_dropdown = dcc.Dropdown(
    id='dataset-dropdown',
    options=dataset_options,
    value=dataset_options[0]['value']
)


# Define callback function for updating figure when dropdown selection changes
@app.callback(
    Output("line-chart", "figure", allow_duplicate=True),
    Input("geo-dropdown-line", "value"),
    Input("dataset-dropdown", "value"),
    prevent_initial_call=True
)
def update_chart(selected_options_line, selected_dataset):
    update_figure_line(selected_dataset, selected_options_line)

    return fig_line


##################################################################################################################################################################################################
# bar chart
##################################################################################################################################################################################################

# Load dataset
df = pd.read_csv(
    "Clean_Dataset/clean_ppp.csv", sep=",")

# Create list of all available geo options, including "All Geo"
all_geo_options_bar = [{"label": "All Countries", "value": "All Geo"}] + \
    [{"label": geo, "value": geo} for geo in df["geo"].unique()]

# Create list of all available year options, including "All Years"
all_year_options_bar = [{"label": "All Years", "value": "All Years"}] + \
    [{"label": year, "value": year} for year in df["TIME_PERIOD"].unique()]

# Create list of all unique years
unique_years = list(set(df["TIME_PERIOD"].tolist()))

# Create a list of dictionaries with year as both the label and value
year_options = [{"label": year, "value": year} for year in unique_years]

# Replace all_year_options_bar with year_options
all_year_options_bar = [
    {"label": "All Years", "value": "All Years"}] + year_options


# Create initial list of selected geo options, excluding "All Geo"
selected_geo_options_bar = [geo for geo in df["geo"].unique()]

# Create initial list of selected year options, excluding "All Years"
selected_year_options_bar = [year for year in df["TIME_PERIOD"].unique()]

# Initialize figure
fig_bar = go.Figure()
# Create trace for each selected geo option and year option
for geo in selected_geo_options_bar:
    for year in selected_year_options_bar:
        df_geo_year = df[(df["geo"] == geo) & (df["TIME_PERIOD"] == year)]
        fig_bar.add_trace(
            go.Bar(
                x=[str(geo) + " " + str(year)],

                y=df_geo_year["OBS_VALUE"],
                name=geo + " " + str(year)

            )
        )
# Update layout
    fig_bar.update_layout(
        title="Price levels for housing in % <br><sup>Housing includes water, electricity, gas and other fuels</sup> ",
        xaxis_title="Country and year",
        yaxis_title="Price index EU = 100%"
    )
# Define callback function for updating figure based on dropdown selection


@app.callback(
    Output("bar-chart", "figure"),
    Input("geo-dropdown-bar", "value"),
    Input("year-dropdown-bar", "value"),
    allow_duplicate=True,
    prevent_initial_call=True
)
def update_figure_bar(selected_geo_options_bar, selected_year_options_bar):
    # Initialize figure
    fig_bar = go.Figure()

    # If "All Geo" is selected, add trace for each geo option
    if "All Geo" in selected_geo_options_bar:
        selected_geo_options_bar = [geo for geo in df["geo"].unique()]

    # If "All Years" is selected, add trace for each year option
    if "All Years" in selected_year_options_bar:
        selected_year_options_bar = [
            year for year in df["TIME_PERIOD"].unique()]
    # Update layout again because it gets reset when traces are removed
    fig_bar.update_layout(
        title="Price levels for housing <br><sup>Housing includes water, electricity, gas and other fuels</sup> ",
        xaxis_title="Country and year",
        yaxis_title="Price index EU = 100"
    )
    # Add trace for each selected geo option and year option
    for geo in selected_geo_options_bar:
        for year in selected_year_options_bar:
            df_geo_year = df[(df["geo"] == geo) & (df["TIME_PERIOD"] == year)]
            fig_bar.add_trace(
                go.Bar(
                    x=[str(geo) + " " + str(year)],
                    y=df_geo_year["OBS_VALUE"],
                    name=geo + " " + str(year)
                )
            )

    # Return the updated figure
    return fig_bar


###################################################################################################################################################################################################
# bar chart deg
###################################################################################################################################################################################################

# Load dataset
df_bar_deg = pd.read_csv(
    "Clean_Dataset/clean_Housing_cost_overburden_rate_by_degree_of_urbanisation.csv", sep=",")

# Create list of all available geo options, including "All Geo"
all_geo_options_bar_deg = [{"label": "All Countries", "value": "All Geo"}] + \
    [{"label": geo, "value": geo} for geo in df_bar_deg["geo"].unique()]

# Create list of all available year options, including "All Years"
all_year_options_bar_deg = [{"label": "All Years", "value": "All Years"}] + \
    [{"label": year, "value": year}
        for year in df_bar_deg["TIME_PERIOD"].unique()]

# Create list of all available DEG options, including "DEG1" and "DEG3"
all_deg_options = [
    {"label": "Cities", "value": "DEG1"},
    {"label": "Rural areas", "value": "DEG3"}
]

# Create initial list of selected geo options, excluding "All Geo"
selected_geo_options_bar_deg = [geo for geo in df_bar_deg["geo"].unique()]

# Create initial list of selected year options, excluding "All Years"
selected_year_options_bar_deg = [
    year for year in df_bar_deg["TIME_PERIOD"].unique()]

# Create initial list of selected DEG options
selected_deg_options = ["DEG1", "DEG3"]

# Initialize figure
fig_bar_deg = go.Figure()

# Define callback function


@app.callback(
    Output("bar-chart-deg", "figure"),
    [Input("geo-dropdown-bar-deg", "value"),
     Input("year-dropdown-bar-deg", "value"),
     Input("deg-dropdown", "value")])
def update_bar_chart(geo_dropdown_value, year_dropdown_value, deg_dropdown_value):

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

    # Initialize figure
    fig_bar_deg = go.Figure()

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
        title="Housing cost overburden: cities or rural areas in %",
        xaxis_title="Years",
        yaxis_title="Housing costs in %"
    )

    return fig_bar_deg


###################################################################################################################################################################################################
# treemap
###################################################################################################################################################################################################

# Load dataset
df_treemap = pd.read_csv(
    "Clean_Dataset/clean_Share_of_housing_costs_in_disposable_household_income.csv", sep=",")

# Create dropdown options for country and household
country_options = [{'label': 'All Countries', 'value': 'All'}] + \
    [{'label': country, 'value': country}
        for country in df_treemap["geo"].unique()]

household_options = [{'label': household, 'value': household}
                     for household in df_treemap["incgrp"].unique()]

# Define initial country and household selections
def filter_data_treemap(countries, year, household):
    filtered_df_treemap = df_treemap[df_treemap["TIME_PERIOD"] == year]
    filtered_df_treemap = filtered_df_treemap[filtered_df_treemap["incgrp"] == household]
    if 'All' not in countries:
        filtered_df_treemap = filtered_df_treemap[filtered_df_treemap["geo"].isin(
            countries)]
    return filtered_df_treemap

# Create function for updating figure based on dropdown selections
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
    
    # I want to add the title: "Housing costs in disposable income in % by year %(year)s" % {"year": year}, to the figure, but I get an error. So I separated the title from the figure in two strings.
    fig_treemap.update_layout(
        title="Housing costs in disposable income in %" + " by year %(year)s" % {
            "year": year},
        margin=dict(l=10, r=10, t=40, b=10),
        height=700
    )

    return fig_treemap


# Create figure
fig_treemap = go.Figure()

# Callback function
@app.callback(
    Output("treemap-graph", "figure"),
    Input("country-dropdown", "value"),
    Input("year-slider-treemap", "value"),
    Input("household-dropdown", "value")
)
def update_figure_treemap(countries, year, household):
    return update_treemap(countries, year, household)


###################################################################################################################################################################################################
# map
###################################################################################################################################################################################################

token = "pk.eyJ1Ijoid29sZm9mcm90ZWJ1ZWhsc3RyYXNzZSIsImEiOiJjbGZtbXJ2a2YwZGowNDNvM2docjQ5YWY4In0.oSQQHrCp69ppmsXVLPetYw"

# I tried a geojson from EUROSTAT but it didn't work, so I used this json from Github user: amcharts
with urlopen('https://raw.githubusercontent.com/amcharts/amcharts4/master/dist/geodata/es2015/json/region/world/europeUltra.json') as response:
    counties = json.load(response)
    
# load dataset
df_map = pd.read_csv(
    "Clean_Dataset/clean_Arrears_mortgage_or_rent_utility_bills_or_hire_purchase.csv", sep=",")

# Create a list of unique years in the TIME_PERIOD column
years = df_map['TIME_PERIOD'].unique()

# Create a dictionary to map the year to the corresponding data
data_dict = {year: df_map[df_map['TIME_PERIOD'] == year] for year in years}

# Callback function
@app.callback(
    dash.dependencies.Output('choropleth', 'figure'),
    [dash.dependencies.Input('year-slider', 'value'),
     dash.dependencies.Input('interval-component', 'n_intervals'),
     dash.dependencies.Input('start-button', 'n_clicks'),
     dash.dependencies.Input('stop-button', 'n_clicks')])

# Create function for updating figure based on dropdown selections
def update_fig_map(selected_year, n_intervals, start_clicks, stop_clicks):
    if start_clicks > stop_clicks:
        selected_year = years[n_intervals % len(years)]
    selected_data = data_dict[selected_year]
    zmin = selected_data['OBS_VALUE'].min()
    zmax = selected_data['OBS_VALUE'].max()
    fig_map = go.Figure(go.Choroplethmapbox(geojson=counties, locations=selected_data['geo'],
                                            z=selected_data['OBS_VALUE'], colorscale="Viridis",
                                            zmin=zmin, zmax=zmax, marker_line_width=0))
    fig_map.update_layout(mapbox_style="light", mapbox_accesstoken=token,
                          title=f"Share of people living in households with arrears on mortgage, rent or utility bills in % by year ({selected_year})",
                          mapbox_zoom=2.5, mapbox_center={"lat": 54, "lon": 15})
    fig_map.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0})

    return fig_map


###################################################################################################################################################################################################
# layout
###################################################################################################################################################################################################

# Define app layout and create layout
app.layout = html.Div(children=[
    html.H1(children="Is housing affordabel in the eu? ", style={
            "textAlign": "center", "fontFamily": "Arial", "color": "black"}),
    html.Div(children="Data analysis by Niklas Denz", style={
             "textAlign": "center", "fontFamily": "Arial", "color": "black"}),

    html.Hr(),

    html.H2("House Prices in the EU"),
    html.P("House prices in the EU rose by 37% from 2010 to 2021. The upward trend began in 2013, with significant increases from 2015 to 2021. 23 Member States experienced price increases, while three saw decreases (Greece data unavailable). The largest increases were in Estonia (+139%), Hungary (+122%), Luxembourg (+115%), Latvia (+101%), and Austria (+100%). Italy (-13%), Cyprus (-8%), and Spain (-2%) experienced decreases."),

    html.H2("Rents in the EU"),
    html.P("Rents in the EU increased by 16% from 2010 to 2021. 25 Member States had increases, while two had decreases. The largest increases were in Estonia (+154%), Lithuania (+110%), and Ireland (+68%), while Greece (-25%) and Cyprus (-3%) had decreases."),

    html.H2("Inflation in the EU"),
    html.P("Inflation in the EU rose by 17% from 2010 to 2021. All Member States experienced inflation, with Hungary (+33%), Romania (+31%), Estonia (+30%), and Lithuania (+25%) having the highest increases. Greece (+2%), Cyprus (+7%), and Ireland (+8%) had the lowest increases."),
    html.Br(),
    html.Div(
        children=[
            html.Label("Select Country:"),
            dcc.Dropdown(
                id="geo-dropdown-line",
                options=all_geo_options_line,
                value=selected_geo_options_line,
                multi=True,
            ),
            html.Label("Select Dataset:"),
            dcc.Dropdown(
                id='dataset-dropdown',
                options=dataset_options,
                value=dataset_options[0]['value']
            ),
            dcc.Graph(id="line-chart", figure=fig_line),

        ]
    ),
    html.Hr(),

    html.H2("Housing costs vary from 64% below to 94% above EU average"),
    html.P("Housing costs in the EU vary significantly compared to the average. In 2021, the highest costs were in Ireland (94% above average), Luxembourg (87% above), and Denmark (78% above). The lowest costs were in Bulgaria (64% below) and Poland (62% below)."),
    html.H2("Housing prices fluctuate in EU member states from 2010 to 2021"),
    html.P("From 2010 to 2021, housing prices compared to the EU average increased in 16 Member States and decreased in 11. The largest increases were in Ireland (from 17% above to 94% above average) and Slovakia (from 44% below to 1% below average). The largest decreases were in Greece (from 8% below to 30% below average) and Cyprus (from 8% below to 26% below)."),
    html.Br(),
    html.Div(
        children=[
            html.Label("Select Country:"),
            dcc.Dropdown(
                id="geo-dropdown-bar",
                options=all_geo_options_bar,
                value=selected_geo_options_bar,
                multi=True
            ),
            html.Label("Select Year:"),
            dcc.Dropdown(
                id="year-dropdown-bar",
                options=all_year_options_bar,
                value=selected_year_options_bar,
                multi=True
            ),

            dcc.Graph(
                id="bar-chart",
                figure=fig_bar
            ),

        ]
    ),

    html.Hr(),
    html.H2("Housing Cost Overburden More Prevalent in Cities"),
    html.P("As house prices and rents continue to rise, the affordability of housing becomes a significant concern. One way to measure this is through the housing cost overburden rate, which indicates the percentage of the population residing in households where housing costs exceed 40% of disposable income. In 2021, 10.4% of the urban population in the EU lived in such households, compared to 6.2% in rural areas. Across all Member States, except Romania, Bulgaria, Lithuania, Croatia, and Latvia, housing cost overburden was higher in cities than in rural areas."),
    html.H2("Housing Cost Overburden Rates are High in Cities for Greece, Denmark, and the Netherlands"),
    html.P("Greece (32.4%), Denmark (21.9%), and the Netherlands (15.3%) had the highest housing cost overburden rates in cities, while in rural areas, Greece (22.0%), Bulgaria (13.3%), and Romania (10.8%) had the highest rates."),
    html.Br(),

    html.Div(children=[
        html.Div([
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
            html.Label("Select Household (DEG1 = Cities / DEG3: Rural areas):"),
            dcc.Dropdown(
                id="deg-dropdown",
                options=all_deg_options,
                value=selected_deg_options,
                multi=True
            ), dcc.Graph(
                id="bar-chart-deg",
                figure=fig_bar
            ),

        ]
        ),
        html.Hr(),

        html.H2("Housing Costs: Almost a Fifth of Disposable Income Dedicated"),
        html.P("Examining housing affordability through the proportion of housing costs in total disposable income provides valuable insights. On average, in the EU in 2021, housing costs accounted for 18.9% of disposable income. However, there were variations among Member States, with the highest shares in Greece (34.2%), Denmark (26.3%), and the Netherlands (23.9%)."),
        html.H2(
            "Housing Cost Burden: Impact on Individuals at Risk of Poverty and Higher Incomes"),
        html.P("For individuals with disposable income below 60% of the national median income, who are at risk of poverty, housing costs represented an average of 37.7% of their disposable income in the EU. Conversely, for individuals with disposable income above 60% of the median income, the share decreased to 15.2%."),
        html.Br(),

        html.Div([
            dcc.Graph(id="treemap-graph"),
            html.Label("Select Country:"),
            dcc.Dropdown(id="country-dropdown",
                         options=country_options, value=['All'], multi=True),
            html.Label("Select Household:"),
            dcc.Dropdown(id="household-dropdown",
                         options=household_options, value='TOTAL'),
            html.Label("Select Year:"),
            dcc.Slider(id="year-slider-treemap", min=df_treemap["TIME_PERIOD"].min(), max=df_treemap["TIME_PERIOD"].max(),
                       value=df_treemap["TIME_PERIOD"].max(), marks={str(year): str(year) for year in df_treemap["TIME_PERIOD"].unique()})
        ]),
        html.Hr(),

        html.Br(),

        html.H2("Improvement in Household Arrears on Housing Payments in the EU"),
        html.P("Arrears on mortgage, rent, or utility bills serve as an indicator of potentially excessive housing costs. Despite the overall increase in house prices and rents between 2010 and 2021, the percentage of people living in households with such arrears in the EU has actually decreased from 12.4% in 2010 to 9.1% in 2021. This decrease was observed in 20 Member States, while five experienced an increase, and the figures remained the same in Malta (2021 data for Slovakia not available). In 2021, the highest percentages were observed in Greece (36.4%), Bulgaria (20.4%), Cyprus (17.3%), Croatia (16.6%), and Ireland (13.6%), while the lowest were in Czechia (2.4%), the Netherlands (2.6%), Belgium (4.2%), and Austria (4.8%)."),
        html.Br(),
        html.Div(children=[
            dcc.Graph(id='choropleth', style={'height': '90vh'}),
            html.Div([
                dcc.Interval(id='interval-component',
                             interval=1000, n_intervals=0),
                html.Button('Start', id='start-button', n_clicks=0),
                html.Button('Stop', id='stop-button', n_clicks=0),
            ], style={'textAlign': 'center'}),
        ]),
        html.Div([
            html.Label("Select Year:"),
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
])


# Run app and I have set the port to 6987 to be able to display all plot files at the same time
if __name__ == '__main__':
    # I set debug to true so that I can see the changes I make in the browser 
    app.run_server(debug=True, port=6987)
