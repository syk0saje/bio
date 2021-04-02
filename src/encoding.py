from src.nucleobase import (
    NucleoBase,
    Adenine,
    Thymine,
    Cytosine,
    Guanine,
    Uracil
)

class Encoding():

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

    def get_complement(self, base: NucleoBase) -> NucleoBase:
        return self.complement_lookup[base]

    def validate(self, string):
        for base_char in string:
            assert NucleoBase.by_char(base_char) in self.complement_lookup, f"""
                Invalid character '{base_char}' for {self.name} encoding.
                Expected one of the following:
                {[base.char for base in self.complement_lookup.keys()]}
            """


DNA = Encoding("DNA", [[Adenine, Thymine], [Cytosine, Guanine]])
RNA = Encoding("RNA", [[Adenine, Uracil], [Cytosine, Guanine]])
