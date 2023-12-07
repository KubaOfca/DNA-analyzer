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
from items import *


external_stylesheets = [dmc.theme.DEFAULT_COLORS]

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
    use_pages=False,
)

app.layout = dmc.Container(children=first_page, id="app")


# callbacks and functions
@callback(
    Output("app", "children"),
    Input("button", "n_clicks"),
    State("dna", "value"),
)
def analyse_dna(n, dna_seq):
    if dna_seq is None:
        return first_page
    if not utils.is_dna(dna_seq):
        return first_page
    second_page = prepare_second_page(dna_seq)
    return second_page


@callback(
    Output("copy1", "content"),
    Input("copy1", "n_clicks"),
    State("Amino_acid", "value"),
)
def copy1(n, text):
    if text is None:
        return "No text"
    return text


def prepare_second_page(dna_seq):
    reverse_complement_textarea.value = utils.reverse_complement_dna(dna_seq)
    aminoacids_textarea.value = utils.dna_to_amino_acids(dna_seq)
    fig = px.bar(
        x=["A", "T", "G", "C"],
        y=utils.count_nucleotides(dna_seq),
        color=["A", "T", "G", "C"],
        title="Title",
        labels={"x": "X", "y": "Y"},
    )
    #pie chart function
    def create_pie_chart(dna_seq):
        nucleotide_counts = utils.count_nucleotides(dna_seq)
        fig = px.pie(
            names=["A", "T", "G", "C"],
            values=nucleotide_counts,
            title="Nucleotide Distribution"
        )
        return fig

    table_ = utils.get_info_about_dna_seq(dna_seq)
    table = dmc.Table(
        verticalSpacing="sm",
        horizontalSpacing=10,
        children=table_,
    )
    bar = dcc.Graph(figure=fig)
    pie = dcc.Graph(figure=create_pie_chart(dna_seq))
    return [
        dmc.Center([reverse_complement_textarea, copy1_object]),
        dmc.Center([aminoacids_textarea]),
        spacer,
        table,
        spacer,
        bar,
        spacer,
        pie
    ]


if __name__ == "__main__":
    app.run(debug=True)
