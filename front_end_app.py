import dash
from datetime import date
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import json
import requests

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("North Medical Group", className="display-4"),
        html.Hr(),
       
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Appointments & Visits", href="/page-1", active="exact"),
                dbc.NavLink("Test Results", href="/page-3", active="exact"),
                dbc.NavLink("Message Center", href="/page-4", active="exact"),
                
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])




### CALL BACK FOR HOME PAGE #######
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_home_page(pathname):
    if pathname == "/":
        return [
                
            ##### HOME COMPONENT ###########

            html.Div([


                html.Div([
                    html.H6('Balance Due:     ', style={'display':'inline', "white-space": "pre-wrap"}),
                    html.H6('$280', style={'display':'inline'}),
                    html.Button('Pay Now', id='submit-val', style={'display':'inline',"margin-left": "28rem"}),
                    html.Br(),
                    html.Br(),
                    html.H6('Service Description:     ', style={'display':'inline', "white-space": "pre-wrap"}),
                    html.H6('Visit to physician (PCP)', style={'display':'inline'}),
                    html.Button('View Details', id='submit-val', style={'display':'inline',"margin-left": "16rem"}),
                ],
                style={
                "width": "800px",
                "height": "150px",
                "padding": "10px",
                "border": "5px solid gray",
                "margin-top": "100px",
                }),


                html.Div([
                    html.H6('Check out your Covid 19 Vaccine status , ', style={'display':'inline', "white-space": "pre-wrap"}),
                    html.Button('View Details', id='submit-val', style={'display':'inline',"margin-left": "38rem"}),
                    html.Br(),
                    
                    html.H6('Print vaccination card and more', style={'display':'inline'}),
                ],
                style={
                "width": "800px",
                "height": "150px",
                "padding": "10px",
                "border": "5px solid gray",
                "margin-top": "100px",
                }),


                html.Div([

                    html.H6('Hepatitis C:  ', style={'display':'inline', "white-space": "pre-wrap"}),
                    html.H6('Screening overdue', style={'display':'inline'}),
                    html.Button('View details', id='submit-val', style={'display':'inline',"margin-left": "24rem"}),
                ],
                style={
                "width": "800px",
                "height": "150px",
                "padding": "10px",
                "border": "5px solid gray",
                "margin-top": "100px",
                }),


                html.Div([
                    html.H6('Recent Visits:  ', style={'display':'inline', "white-space": "pre-wrap"}),
                    html.Br(),
                    html.Br(),
                    html.H6('  Visit to PCP', style={'display':'inline', "white-space": "pre-wrap"}),
                    html.Br(),
                    html.H6('  Doctor Radhika', style={'display':'inline', "white-space": "pre-wrap"}),
                    html.Br(),
                    html.H6('  Date : 9/19/2020', style={'display':'inline', "white-space": "pre-wrap"}),
                    html.Br(),
                    html.Br(),
                                    
                    html.Button('View details', id='submit-val', style={'display':'inline',"margin-left": "8rem"}),
                ],
                style={
                "width": "310px",
                "height": "650px",
                "padding": "10px",
                "border": "5px solid gray",
                "margin-top": "-41.5%",
                "margin-left": "65%"
                })

            ]) 
        ]

    elif pathname == "/page-1":
        return [
                ##### Appointments & Visits ###########

            html.Div([


                html.Div([

                    html.H6('Select Date: ', style={'display':'inline', "white-space": "pre-wrap"}),
                    html.H6('Select Faculty: ', style={'display':'inline', "white-space": "pre-wrap","margin-left": "15%"}),
                    html.H6('Select Physcian: ', style={'display':'inline', "white-space": "pre-wrap","margin-left": "40%"}),
                    html.Br(),
                    html.Br(),

                    html.Div([
                        html.Div([
                            dcc.DatePickerSingle(
                                id='my-date-picker-single',
                                min_date_allowed=date(1995, 8, 5),
                                max_date_allowed=date(2025, 9, 19),
                                initial_visible_month=date(2017, 8, 5)
                                
                            ),
                    ],style={"margin-top": "0%","width": "200px","height": "150px","display":"inline"}),


                html.Div([

                    dcc.Dropdown(
                        id='demo-dropdown1',
                        options=[
                        {'label': 'Montreal - Real Mountain View', 'value': 'facility1'},
                        {'label': 'New York', 'value': 'facility2'}
                        ],
                        value=[]
                    )
                ],style={ "margin-left": "20%","margin-top": "-3%", "width": "500px","height": "150px"}),
            

                html.Div([

                    dcc.Dropdown(
                        id='demo-dropdown2',
                        options=[
                        
                        ],
                        value=[] 
                    )
                ],style={ "margin-left": "67%","margin-top": "-10.5%", "width": "200px","height": "150px"}),



                ],style={"display":"inline"}),


                ],
                style={
                "width": "1500px",
                "height": "150px",
                "padding": "10px",
                "margin-top": "100px",
                }),

                html.Br(),
                html.H6('Available Time Slots:'),
                    
                html.Div([], id ="my-output",style={
                    "width": "800px",
                    "height": "550px",
                    "padding": "10px",
                    "border": "5px solid gray",
                    "margin-top": "2%",
        }),



        html.Div([
        ], id="rating-comp",
        style={
        "width": "310px",
        "height": "450px",
        "padding": "10px",
        "border": "5px solid gray",
        "margin-top": "-35%",
        "margin-left": "65%"
        }),

            ])
        
        ]
    elif pathname == "/page-3":
        return [
                
    html.Div([
        html.H1('Welcome to Awesome Medical Group')
        ], style={'padding': 10}
        ),

        html.Div([
            html.H5('We are now part of North Valley Health Group')
        ], style={'margin-left': 100,'margin-top': -30, }),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div([
        html.Div(children=[
            html.Label('News and Updates'),
            html.Br(),
            html.H2('News 1'),
            html.H2('News 2'),
            
        ], style={'padding': 10, 'flex': 1}),

        html.Div(children=[
            
            html.Br(),
            html.Label('Text Input : '),
            dcc.Input(value='MTL', type='text'),

            html.Br(),
            
            html.Br(),
            html.Label('Text Input : '),
            dcc.Input(value='', type='password'),

            html.Br(),
            html.Br(),
            html.Br(),
            html.Button('Submit', id='submit-val', n_clicks=0)
            

            ], style={'padding': 10, 'flex': 1})
        ], style={'display': 'flex', 'flex-direction': 'row'})



    ]

    elif pathname == "/page-4":
        return [
                html.H1('High School in Iran',
                        style={'textAlign':'center'}),
                # dcc.Graph(id='bargraph',
                #          figure=px.bar(df, barmode='group', x='Years',
                #          y=['Girls High School', 'Boys High School']))
                ]

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )




## THIS CALLBACK IS RESPONISBLE TO GET LIST OF DOCTORS FOR EACH FACULTY ON THE SELECTED DATE
@app.callback(
    Output(component_id='demo-dropdown2', component_property='options'),
    [Input(component_id='demo-dropdown1', component_property='value') , Input('my-date-picker-single', 'date')] ,
    prevent_initial_call=False
)
def get_doctors(val_chosen1,choosen_date):
    print(val_chosen1,choosen_date)
    if len(val_chosen1) ==0 or choosen_date is None :
        return dash.no_update
    
    temp = {}

    temp['facilityID'] = val_chosen1
    temp['date'] = choosen_date
    temp['docID'] =''
    json_object = json.dumps(temp, indent = 4) 
    #print("This object is going",json_object)
    res = requests.post('http://localhost:6000', json=json_object)
    docs = (res.json())
    return docs




## THIS CALLBACK IS USED TO GET THE RATINGS AS WELL AS THE AVAILABLE TIME SLOTS FOR THE SELECTED DOCTOR
@app.callback(
    [ Output(component_id='my-output', component_property='children'), Output(component_id='rating-comp', component_property='children')],
    [Input(component_id='demo-dropdown1', component_property='value') , Input(component_id='demo-dropdown2', component_property='value'), Input('my-date-picker-single', 'date') ],
    prevent_initial_call=False
)
def get_ratings_and_timeslots(val_chosen1,val_chosen2,date_value):
    
    body = []
    try:
        print(val_chosen1[0],val_chosen2[0])
    except:
        return ['','']
    lines = [val_chosen1,val_chosen2]

    

    dictionary ={ "date":date_value, "facilityID":val_chosen1 , "docID": val_chosen2} 
    # Serializing json  
    json_object = json.dumps(dictionary, indent = 4) 
    print(json_object)
    
    res = requests.post('http://localhost:6000', json=json_object)

    result = (res.json())
    
    
    ## Sample object for Rating API II
    #mydict = { "Available_slots" : ['9 am -9:30 am','10 am -10:30 am'] , "Stars":"****" , "reviews":['good','excellent']}

    ## Checking if the requested API has send the stars parameter or not
    if len(result['Stars'])>=1:
        body.append(html.H6('Ratings:  ', style={'display':'inline', "white-space": "pre-wrap"}))
        body.append(html.Br())
        body.append(html.Br())
        body.append(html.H1(result['Stars'], style={'display':'inline', "white-space": "pre-wrap"}))
    
    body.append(html.Br())
    body.append(html.H6('  Reviews', style={'display':'inline', "white-space": "pre-wrap"}))
    body.append(html.Br())
    body.append( html.Ul([html.Li(x) for x in result['reviews']]))
    body.append(html.Br())
    body.append(html.Br())

    ## Checking if there is a flag in the API
    if 'Flag' in result:
        body.append(html.H4(result['Flag']))
        
    body.append(html.Br())
    body.append(html.Button('Book it', id='submit-val', style={'display':'inline',"margin-left": "4rem"}))

    body2 = []
    body2.append( html.Div(date_value))
    body2.append(  html.Ul([html.Li(x) for x in result['Available_slots']]))
    
    print(body2 , body)
    print("!!!")
    
    ## Returning UI of both components
    return body2 , body


if __name__=='__main__':
    app.config['suppress_callback_exceptions'] = True
    app.run_server(debug=True,host= '0.0.0.0', port=3000)
