import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg before importing pyplot
import matplotlib.pyplot as plt
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

def plot_dna_sequence(dna_sequence, output_file):
    # Create a Biopython Seq object
    seq = Seq(dna_sequence)

    # Calculate GC content
    gc_content = gc_fraction(seq)

    # Plot the DNA sequence
    plt.figure(figsize=(10, 2))
    plt.text(0.5, 0.5, f'DNA Sequence:\n{seq}\nGC Content: {gc_content:.2f}%', ha='center', va='center', fontsize=12)
    plt.axis('off')

    # Save the plot as a PNG file
    plt.savefig(output_file, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Get DNA sequence input from the user
    dna_sequence = input("Enter DNA sequence: ")

    # Specify the output file name
    output_file = "dna_sequence_plot.png"

    # Plot and save the DNA sequence
    plot_dna_sequence(dna_sequence, output_file)
