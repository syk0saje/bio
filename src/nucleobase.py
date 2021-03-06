class NB(type):

    def __repr__(self):
        return self.char


class NucleoBase(metaclass=NB):

    @property
    def char():
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
