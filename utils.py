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


def get_info_about_dna_seq(dna_sequence):
    seq = Seq(dna_sequence)
    gc_content = gc_fraction(seq)
    mw = molecular_weight(seq)

    df = pd.DataFrame(
        {
            "GC Content": [f"{gc_content:.2f}%"],
            "Molecular Weight": [f"{mw:.2f} g/mol"],
            "Sequence Length": [len(seq)],
        }
    )

    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table


def is_dna(seq):
    seq = seq.upper()
    dna_pattern = re.compile("[^ATCG]")
    return False if re.search(dna_pattern, seq) else True


def dna_complement(seq):
    seq = seq.upper()
    complement_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complement_sequence = "".join(complement_dict[base] for base in seq)
    return complement_sequence


def reverse_complement_dna(seq):
    seq = seq.upper()
    complement_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    reverse_complement_sequence = "".join(complement_dict[base] for base in seq)
    return reverse_complement_sequence


def dna_to_amino_acids(dna_sequence):
    genetic_code = {
        "TTT": "F",
        "TTC": "F",
        "TTA": "L",
        "TTG": "L",
        "CTT": "L",
        "CTC": "L",
        "CTA": "L",
        "CTG": "L",
        "ATT": "I",
        "ATC": "I",
        "ATA": "I",
        "ATG": "M",
        "GTT": "V",
        "GTC": "V",
        "GTA": "V",
        "GTG": "V",
        "TCT": "S",
        "TCC": "S",
        "TCA": "S",
        "TCG": "S",
        "CCT": "P",
        "CCC": "P",
        "CCA": "P",
        "CCG": "P",
        "ACT": "T",
        "ACC": "T",
        "ACA": "T",
        "ACG": "T",
        "GCT": "A",
        "GCC": "A",
        "GCA": "A",
        "GCG": "A",
        "TAT": "Y",
        "TAC": "Y",
        "TAA": "*",
        "TAG": "*",
        "CAT": "H",
        "CAC": "H",
        "CAA": "Q",
        "CAG": "Q",
        "AAT": "N",
        "AAC": "N",
        "AAA": "K",
        "AAG": "K",
        "GAT": "D",
        "GAC": "D",
        "GAA": "E",
        "GAG": "E",
        "TGT": "C",
        "TGC": "C",
        "TGA": "*",
        "TGG": "W",
        "CGT": "R",
        "CGC": "R",
        "CGA": "R",
        "CGG": "R",
        "AGT": "S",
        "AGC": "S",
        "AGA": "R",
        "AGG": "R",
        "GGT": "G",
        "GGC": "G",
        "GGA": "G",
        "GGG": "G",
    }
    codons = [dna_sequence[i : i + 3] for i in range(0, len(dna_sequence), 3)]
    amino_acids = [genetic_code[codon] for codon in codons if len(codon) == 3]
    protein_sequence = "".join(amino_acids)
    return protein_sequence


def count_nucleotides(dna_sequence):
    count_a = dna_sequence.count("A")
    count_t = dna_sequence.count("T")
    count_g = dna_sequence.count("G")
    count_c = dna_sequence.count("C")
    return [count_a, count_t, count_g, count_c]
