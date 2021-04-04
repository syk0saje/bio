from src.nucleobase import (
    NucleoBase,
    Adenine,
    Thymine,
    Cytosine,
    Guanine,
    Uracil
)


class Encoding:
    """
    Genetic material (nucleic acids) read from 5' to 3'
    """

    def __init__(self, name, pairings: [[NucleoBase]]):
        self.name = name
        self.complement_lookup = self.generate_complement_lookup(pairings)

    @staticmethod
    def generate_complement_lookup(pairings):
        lookup = {}
        for pair in pairings:
            assert len(pair) == 2
            x, y = pair
            assert x not in lookup
            assert y not in lookup
            lookup[x] = y
            lookup[y] = x
        return lookup

    def get_base_complement(self, base: NucleoBase) -> NucleoBase:
        return self.complement_lookup.get(base)

    def get_seq_complement(self, seq: [NucleoBase]) -> [NucleoBase]:
        return [self.get_base_complement(base) for base in seq[::-1]]

    def validate(self, sequence):
        for base in sequence:
            assert base in self.complement_lookup, f"""
                Invalid base '{base}' for {self.name} encoding.
                Expected one of the following:
                {self.complement_lookup.keys()}
            """


DNA = Encoding("DNA", [[Adenine, Thymine], [Cytosine, Guanine]])
RNA = Encoding("RNA", [[Adenine, Uracil], [Cytosine, Guanine]])


def convert(base: NucleoBase, frm: Encoding, to: Encoding):
    if (frm == DNA) and (to == RNA):
        return {Thymine: Uracil}.get(base, base)
    else:
        raise Exception(f"Don't know how to convert {frm} to {to}.")
