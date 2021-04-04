from src.strand import RNAStrand
from src.amino_acid import AminoAcid

AMINO_ACID_ANTICODONS = {
    'A': ['AGC', 'CGC', 'GGC', 'UGC'],
    'C': ['ACA', 'GCA'],
    'D': ['AUC', 'GUC'],
    'E': ['CUC', 'UUC'],
    'F': ['AAA', 'GAA'],
    'G': ['ACC', 'CCC', 'GCC', 'UCC'],
    'H': ['AUG', 'GUG'],
    'I': ['AAU', 'GAU', 'UAU'],
    'K': ['CUU', 'UUU'],
    'L': ['AAG', 'CAA', 'CAG', 'GAG', 'UAA', 'UAG'],
    'M': ['CAU'],
    'N': ['AUU', 'GUU'],
    'P': ['AGG', 'CGG', 'GGG', 'UGG'],
    'Q': ['CUG', 'UUG'],
    'R': ['ACG', 'CCG', 'CCU', 'GCG', 'UCG', 'UCU'],
    'S': ['ACU', 'AGA', 'CGA', 'GCU', 'GGA', 'UGA'],
    'T': ['AGU', 'CGU', 'GGU', 'UGU'],
    'V': ['AAC', 'CAC', 'GAC', 'UAC'],
    'W': ['CCA'],
    'Y': ['AUA', 'GUA'],
}

ANTICODON_TO_AMINO_ACID = {
    anticodon: amino_acid
    for amino_acid, anticodons in AMINO_ACID_ANTICODONS.items()
    for anticodon in anticodons
}


class tRNAStrand:

    amino_acid: AminoAcid = None

    def __init__(self, anticodon: str):
        self.anticodon = RNAStrand(anticodon)

    def bind(self, amino_acid: AminoAcid):
        if amino_acid != ANTICODON_TO_AMINO_ACID[self.anticodon]:
            return False
        self.amino_acid = amino_acid
        return True

    def release_amino_acid(self):
        amino_acid = self.amino_acid
        self.amino_acid = None
        return amino_acid
