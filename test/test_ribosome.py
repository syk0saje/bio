from loguru import logger
from src.organelle import Ribosome
from src.strand import mRNAStrand
from src.tRNA import tRNAStrand
from src.enzyme import AminoacyltRNASynthetase
from src.molecules import ATP

AMINO_ACID_CODONS = {
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

CODON_TO_AMINO_ACID = {
    codon: amino_acid
    for amino_acid, codons in AMINO_ACID_CODONS.items()
    for codon in codons
}


def test_ribosome():
    r = Ribosome()
    charger = AminoacyltRNASynthetase()
    atp = ATP()
    for amino_acid, codons in AMINO_ACID_CODONS.items():
        for codon in codons:
            logger.info(f"Testing {codon} for {amino_acid}...")
            mRNA = mRNAStrand(codon)
            r.bind_mRNA(mRNA)
            anticodon = mRNA.get_seq_complement()
            tRNA = tRNAStrand(anticodon)
            charger.charge(tRNA, amino_acid, atp)
            polypeptide = r.bind_tRNA(tRNA)
            assert polypeptide == [amino_acid]
