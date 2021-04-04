from src.tRNA import tRNA
from src.enzymes import Ribosome

amino_acid_codons = {
    'A': ['GCA', 'GCC', 'GCG', 'GCU'],
    'C': ['UGC', 'UGU'],
    'D': ['GAC', 'GAU'],
    'E': ['GAA', 'GAG'],
    'F': ['UUC', 'UUU'],
    'G': ['GGA', 'GGC', 'GGG', 'GGU'],
    'H': ['CAC', 'CAU'],
    'I': ['AUA', 'AUC', 'AUU'],
    'K': ['AAA', 'AAG'],
    'L': ['CUA', 'CUC', 'CUG', 'CUU', 'UUA', 'UUG'],
    'M': ['AUG'],
    'N': ['AAC', 'AAU'],
    'P': ['CCA', 'CCC', 'CCG', 'CCU'],
    'Q': ['CAA', 'CAG'],
    'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGU'],
    'S': ['AGC', 'AGU', 'UCA', 'UCC', 'UCG', 'UCU'],
    'T': ['ACA', 'ACC', 'ACG', 'ACU'],
    'V': ['GUA', 'GUC', 'GUG', 'GUU'],
    'W': ['UGG'],
    'Y': ['UAC', 'UAU'],
}

codon_to_amino_acid = {
    codon: amino_acid
    for amino_acid, codons in AMINO_ACID_CODONS.items()
    for codon in codons
}

def test_ribosome():
    r = Ribosome()
    for amino_acid, codons in amino_acid_codons:
        for codon in codons:
            anticodoon