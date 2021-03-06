from loguru import logger
from src.strand import mRNAStrand
from src.tRNA import tRNAStrand
from src.amino_acid import AminoAcid

STOP_CODONS = ["UAA", "UAG", "UGA"]


class Ribosome:

    mRNA: mRNAStrand = None
    current_index = None
    polypeptide: [AminoAcid] = None

    @property
    def current_codon(self):
        return self.mRNA.sequence[self.current_index:self.current_index + 3]

    def bind_mRNA(self, mRNA: mRNAStrand):
        assert not self.mRNA
        self.mRNA = mRNA
        self.current_index = 0
        self.polypeptide = []
        logger.success(f"Ribosome: Bound mRNA {mRNA}")

    def bind_tRNA(self, tRNA: tRNAStrand):
        """
        A Site compatibility check
        """
        logger.info(f"Ribosome: checking compatibility of tRNA {tRNA} with current codon {self.current_codon}...")
        if tRNA.anticodon.is_complementary(self.current_codon):
            logger.success("Compatible.")
            return self.synthesize(tRNA)
        else:
            logger.warning("Incompatible.!")

    def synthesize(self, tRNA: tRNAStrand):
        """
        P Site processing and E site ejection
        """
        amino_acid = tRNA.release_amino_acid()
        if not amino_acid:
            logger.error("No amino acid found in tRNA!")
            return False

        self.polypeptide.append(amino_acid)
        self.eject_tRNA()
        return self.advance_mRNA()

    @property
    def should_eject_mRNA(self):
        return (
            self.current_index >= len(self.mRNA.sequence)
            or self.current_codon in STOP_CODONS
        )

    def advance_mRNA(self):
        self.current_index += 3
        if self.should_eject_mRNA:
            return self.eject_mRNA()

    def eject_mRNA(self):
        polypeptide = self.polypeptide
        self.mRNA = None
        self.polypeptide = None
        return polypeptide

    def eject_tRNA(self):
        self.tRNA = None
