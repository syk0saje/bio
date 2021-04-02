from src.strand import DNAStrand
from src.enzymes import RNAPolymerase


def main():
    dna = DNAStrand("ACTGACTGGAGAGAGATTTCC")
    print(dna)
    rna = RNAPolymerase().transcribe(dna, 5, 12)
    print(rna)


if __name__ == "__main__":
    main()
