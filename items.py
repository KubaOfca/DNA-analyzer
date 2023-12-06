import plotly.express as px
from dash import Dash, callback, Output, Input, dcc, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
from Bio.Seq import Seq
from Bio.SeqUtils import molecular_weight, gc_fraction
import plotly.graph_objects as go
from dash import html
import re
import utils

title = dmc.Center([dmc.Title("DNA analysis", color="blue", size="h3")])

dna_sequence_textarea = dmc.Center(
    dmc.TextInput(
        label="Enter DNA sequence",
        style={"width": 200},
        placeholder="Your DNA sequence",
        icon=DashIconify(icon="openmoji:dna"),
        id="dna",
    ),
)

analyse_button = dmc.Center(
    dmc.Button("Analyse", leftIcon=DashIconify(icon="mdi:play-outline"), id="button")
)

dna_image = dmc.Center(html.Img(src="/assets/dna3.gif", width=200))
in_silico_image = html.Img(src="/assets/logo.jpg", width=90, height=90)
in_silico_text = dmc.Text(
    "Koło Naukowe Studentów Bioinformatyki In Silico",
    weight=500,
    color="white",
    style={"margin": "30px"},
)

spacer = html.Div(style={"width": "20px", "height": "50px"})

footer_first_page = dmc.Footer(
    height=90,
    fixed=True,
    withBorder=True,
    children=[in_silico_image, in_silico_text],
    style={
        "bottom": 0,
        "width": "100%",
        "backgroundColor": "black",
        "display": "flex",
        "flexDirection": "row",
        "alignItems": "center",
        "borderTop": "1px solid white",
    },
)

divider = dmc.Divider(variant="solid")

first_page = [
    title,
    divider,
    spacer,
    dna_image,
    spacer,
    dna_sequence_textarea,
    analyse_button,
    footer_first_page,
]

# second page

reverse_complement_textarea = dmc.Textarea(
    label="Reverse Complement",
    value="",
    style={"width": 300},
    autosize=True,
    minRows=1,
    maxRows=1,
    id="reverse_complement",
)
copy1_function = dcc.Clipboard(id="copy1")
copy1_object = dmc.Center([copy1_function])

aminoacids_textarea = dmc.Textarea(
    label="Amino acid sequence",
    style={"width": 300},
    autosize=True,
    minRows=1,
    maxRows=1,
    id="Amino_acid",
)

copy2_function = dcc.Clipboard(id="copy2")
copy2_object = dmc.Center([copy2_function])

bar_plot = dcc.Graph(
    figure=px.bar(
        x=["A", "T", "G", "C"],
        y=[0, 0, 0, 0],
        color=["red", "green", "blue", "black"],
        title="Nucleotides content",
        labels={"x": "Nucleotides", "y": "Count"},
    ),
)

footer_second_page = dmc.Footer(
    height=80,
    fixed=True,
    withBorder=True,
    children=[in_silico_image, in_silico_text],
    style={
        "bottom": 0,
        "width": "100%",
        "backgroundColor": "black",
        "display": "flex",
        "flexDirection": "row",
        "alignItems": "center",
        "borderTop": "1px solid white",
    },
)
