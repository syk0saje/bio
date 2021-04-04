from loguru import logger
from src.encoding import convert, DNA, RNA
from src.strand import DNAStrand, mRNAStrand
from src.tRNA import tRNAStrand
from src.amino_acid import AminoAcid
from src.molecules import ATP


class RNAPolymerase:

    def transcribe(self, dna: DNAStrand, promoter: int, end: int) -> mRNAStrand:
        assert promoter <= end
        rna_sequence = []
        for i in range(promoter, end + 1):
            dna_base = dna.sequence[i]
            rna_base = convert(dna_base, frm=DNA, to=RNA)
            rna_sequence.append(RNA.get_base_complement(rna_base))
        return mRNAStrand(rna_sequence[::-1])


class AminoacyltRNASynthetase:

    def charge(self, tRNA: tRNAStrand, amino_acid: AminoAcid, atp: ATP):

        if type(tRNA) != tRNAStrand:
            logger.error(f"Invalid tRNA provided: {tRNA}")
            return False

        if type(amino_acid) != AminoAcid:
            logger.error(f"Invalid amino_acid provided: {amino_acid}")
            return False

        if type(atp) != ATP:
            logger.error(f"Invalid ATP provided: {atp}")
            return False

        return tRNA.bind(amino_acid)
