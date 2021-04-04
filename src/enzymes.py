from src.encoding import convert, DNA, RNA
from src.strand import DNAStrand, mRNAStrand


class RNAPolymerase:

    def transcribe(self, dna: DNAStrand, promoter: int, end: int) -> mRNAStrand:
        assert promoter <= end
        rna_sequence = []
        for i in range(promoter, end + 1):
            dna_base = dna.sequence[i]
            rna_base = convert(dna_base, frm=DNA, to=RNA)
            rna_sequence.append(RNA.get_base_complement(rna_base))
        return mRNAStrand(rna_sequence[::-1])
