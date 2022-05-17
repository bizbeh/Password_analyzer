# -*- coding: utf-8 -*-
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from password_strength import PasswordStats

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.I("Password analyzer by Ilia"),
        html.Br(),
        dcc.Input(id="input1", type="text", placeholder="Type your password", style={'marginRight':'10px'}),
        html.Div(id="output"),
    ]
)


@app.callback(
    Output("output", "children"),
    Input("input1", "value"),
)



def update_output(input1):
    input_val = "a"
    if input1 != "":
        input_val = input1
    stng = PasswordStats(input_val).strength()
    
    ratio = 2 * (stng - 0) 
    g = int(max(0, 255 * (ratio - 1)))
    r = int(max(0, 255 * (1 - ratio)))
    b = 255 - g - r
    #return u'password score is: {} '.format(stng)
    color = 'rgb(' + str(r) +',' + str(g) + ',' + str(b) + ')'
    return html.Div(u'password score is: {} '.format(stng), style={'color':color})


if __name__ == "__main__":
    app.run_server(debug=True)