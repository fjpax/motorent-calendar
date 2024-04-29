from dash import *
import dash_mantine_components as dmc


app = Dash(__name__, external_scripts=['https://cdn.jsdelivr.net/npm/fullcalendar/index.global.min.js'])
app.layout = dmc.MantineProvider(html.Div([
                html.Div(className="card card-calendar", style={"height": "100%"}, children=[
                        html.Div(className="card-body p-3", children=[
                            html.Div(id="calendar", **{"data-bs-toggle": "calendar"})
                        ])
                    ]),
   dmc.Modal(id='modal'),
    dmc.Modal(id='add_modal', children=[dcc.Input(id='add_modal_date')])
])) 

app.clientside_callback(
    """(id) => {setTimeout(() => {createCalendar(id)}, 1000); return dash_clientside.no_update}""",
    Output('calendar', 'id'), Input('calendar', 'id')
)

if __name__ == "__main__":
    app.run(debug=False)
