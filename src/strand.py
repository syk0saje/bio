from src.nucleobase import NucleoBase
from src.encoding import Encoding, DNA, RNA


class Strand:
    """
    A strand of nucleic acid
    """

    @property
    def encoding() -> Encoding:
        raise NotImplementedError

    def __init__(self, sequence):
        if type(sequence) == str:
            sequence = [NucleoBase.by_char(char) for char in sequence]
        self.encoding.validate(sequence)
        self.sequence = sequence

    def __repr__(self):
        return f"{self.encoding.name}:{self.sequence}"

    def get_seq_complement(self):
        return self.encoding.get_seq_complement(self.sequence)

    def is_complementary(self, sequence):
        return self.get_seq_complement() == sequence


class DNAStrand(Strand):
    encoding = DNA


class RNAStrand(Strand):
    encoding = RNA


class mRNAStrand(RNAStrand):
    pass
