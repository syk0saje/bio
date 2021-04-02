from src.strand import mRNAStrand, tRNAStrand

STOP_CODONS = []


class Ribosome:

    mRNA = None
    current_index = None

    @property
    def current_codon(self):
        return self.mRNA[self.current_index:self.current_index + 3]

    def bind_mRNA(self, mRNA: mRNAStrand):
        assert not self.mRNA
        self.mRNA = mRNA

    def bind_tRNA(self, tRNA: tRNAStrand):
        """
        A Site compatibility check
        """
        anticodon = tRNA.sequence
        if self.match(self.current_codon, anticodon):
            self.synthesize(tRNA)

    def synthesize(self, tRNA: tRNAStrand):
        """
        P Site processing and E site ejection
        """
        pass

    @property
    def should_eject_mRNA(self):
        return (
            self.current_index >= len(self.mRNA.sequence)
            or self.current_codon in STOP_CODONS
        )

    def advance_mRNA(self):
        self.current_index += 3
        if self.should_eject_mRNA:
            self.eject_mRNA()

    def eject_mRNA(self):
        self.mRNA = None
