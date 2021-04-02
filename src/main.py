class NucleoBase:

    @property
    def symbol():
        raise NotImplementedError

    @staticmethod
    def by_char(char):
        for cls in NucleoBase.__subclasses__():
            if cls.char == char:
                return cls


class Adenine(NucleoBase):
    char = "A"


class Guanine(NucleoBase):
    char = "G"


class Cytosine(NucleoBase):
    char = "C"


class Thymine(NucleoBase):
    char = "T"


class Uracil(NucleoBase):
    char = "U"


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


class Strand:

    def __init__(self, string, encoding: Encoding = DNA):
        encoding.validate(string)
        self.string = string
        self.encoding = encoding


def main():
    x = Strand("ACTG")
    x = Strand("ACUG", RNA)


if __name__ == "__main__":
    main()
