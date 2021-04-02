from src.nucleobase import Thymine, Uracil
from src.encoding import RNA
from src.strand import DNAStrand, mRNAStrand


class RNAPolymerase:

    def transcribe(self, dna: DNAStrand, promoter: int, end: int) -> mRNAStrand:
        assert promoter <= end
        rna_sequence = []
        for i in range(promoter, end + 1):
            dna_base = dna.sequence[i]
            rna_base = {Thymine: Uracil}.get(dna_base, dna_base)
            rna_sequence.append(RNA.get_complement(rna_base))
        return mRNAStrand(rna_sequence[::-1])
