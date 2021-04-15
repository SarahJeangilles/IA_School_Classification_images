#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output, State
from functions import *
from app import app
from skimage.io import imread
import numpy as np
from skimage.transform import resize
import io
from urllib.request import urlopen
from layouts import lib, modal
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


@app.callback(
    Output("modal", "is_open"),
    [Input("read-instructions", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


def img_predict(src, content):#, label_prd):
    model = pickle.load(open('best_model.pkl', 'rb'))
    return html.Div([
        dbc.Toast([
            dbc.Row([html.Img(src=src,height='190px')], justify='center'),
            dbc.Row([
                html.P(lib[(model.predict([content])[0])], style={'margin-top':20, 'margin-left':20,'margin-right':10 }),
                html.A('Learn more about {}'.format(model.predict([content])[0]),href = 'https://en.wikipedia.org/wiki/'+str(model.predict([content])[0]), style={'margin-left':20,'margin-right':10 })
                ])
            ],
    header="It's a {}!".format(model.predict([content])[0]),
    icon="primary",
    dismissable=True,
    style={'overflowY': 'scroll','overflowX': 'hidden', "position": "fixed", "top": 120, "right": 450, "width": 500, "height":300, 'text-align':'justify'})
    ])

@app.callback(Output('input-img', 'value'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'))
def update_output(content, name):
    if content is not None:
        return content


        
@app.callback(Output('img-toast', 'children'),
              Input('guess-button', 'n_clicks'),
              State('input-img','value'))
def open_url_toast(n, value):
    if value is not None:
            im = np.asarray(imread(io.BytesIO(urlopen(value).read())))
            im = resize(im,(80,80))
            children=[img_predict(value,im)]
            return children


