from src.encoding import Encoding, DNA, RNA


class Strand:
    """
    Genetic material with a phosphate backbone
    """

    def __init__(self, string, encoding: Encoding = DNA):
        encoding.validate(string)
        self.string = string
        self.encoding = encoding


def main():
    x = Strand("ACTG")
    x = Strand("ACUG", RNA)


if __name__ == "__main__":
    main()
