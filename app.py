
from dash_extensions import Purify, DeferScript
from dash import html
from dash.dependencies import ClientsideFunction
from dash import html, dcc
import json
from dash_extensions.enrich import DashProxy, Input, Output, State, callback

from dash import Dash, html, dcc, Input, Output, State
from flask import jsonify
from dash import Dash, html, dcc, Input, Output, State, callback, no_update
import json
# Get the MongoDB URI
import os
mongo_uri = os.getenv('MONGO_CLIENT')

import json
from pymongo.mongo_client import MongoClient

# Connect to MongoDB (change the URI if using MongoDB Atlas with your credentials)

client = MongoClient(mongo_uri)
# Access the database
db = client["motorent"]

# Access the collection where you want to insert the event
events_collection = db["reservations-calendar"]

# db = client["motorent"]
# events_collection = db["reservations-calendar"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


app = Dash(__name__, assets_folder='assets')

app.layout = html.Div([
    html.Div([
        html.Div(id='dummy-div', style={'display': 'none'}),
        html.Div(id="calendar"),  # Calendar will be initialized here by FullCalendar JS
    ], className="card card-calendar", style={"height": "100%"}),

    html.Div([
        dcc.Input(id='input-title', type='text', placeholder='Event Title'),
        dcc.Input(id='input-start', type='text', placeholder='Start Date (YYYY-MM-DD)'),
        dcc.Input(id='input-end', type='text', placeholder='End Date (YYYY-MM-DD)', value=''),
        dcc.Dropdown(
            id='input-classname',
            options=[
                {'label': 'Danger', 'value': 'bg-gradient-danger'},
                {'label': 'Warning', 'value': 'bg-gradient-warning'},
                {'label': 'Success', 'value': 'bg-gradient-success'},
                {'label': 'Info', 'value': 'bg-gradient-info'},
                {'label': 'Primary', 'value': 'bg-gradient-primary'}
            ],
            placeholder='Select Event Type'
        ),
        html.Button('Add Event', id='submit-button', n_clicks=0),
    ], style={'padding': '20px'}),
])

app.clientside_callback(
    """
    function(n_clicks, title, start, end, classname) {
        return dash_clientside.clientside.addEvent(n_clicks, title, start, end, classname);
    }
    """,
    Output('dummy-div', 'children'),  # This output can be an invisible div just to trigger callback
    [Input('submit-button', 'n_clicks')],
    [State('input-title', 'value'),
     State('input-start', 'value'),
     State('input-end', 'value'),
     State('input-classname', 'value')]
)

if __name__ == "__main__":
    app.run_server(debug=True)

