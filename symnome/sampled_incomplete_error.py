import numpy as np
from symnome.base_genome import BaseGenome

class SampledIncompleteGenome(BaseGenome):
    '''
        A simulation of one difficulty in genome sequencing: repeated reads from
        the true genome. Here, a true base genome is constructed and several reads
        are generated from the original genome. These strictly will not provided
        complete coverage of the genome. Some data from the true genome will be
        ommitted from the reads iterator.

        Omissions from the original dataset wil be spaced as evenly as possible.
        Reads will never contain base pairs from both the left and right of an
        ommission. Within the remaining contigs the overlap will be consistent,
        containing each base pair exactly 2 times.
    '''
    def __init__(self, length=500, overlap_size=6, omission_size=3, omissions=10):
        '''
            length (int): the length of the base genome
            overlap_size (int): the length of the overlapping reigons
        '''
        super().__init__(length=length)
        self._contigs = []
        self._omissions = []
        self._genome_samples = [];

        base_genome = self.true_genome()
        genome_size = len(base_genome)
        read_size = overlap_size * 2

        total_omission_size = omissions * omission_size
        contig_size = (length - total_omission_size) / (omissions + 1)
        chunk_size = contig_size + omission_size

        for contig_idx in range(0, length, chunk_size):
            omission_idx = contig_idx + contig_size
            self._contigs.append(base_genome[contig_idx:omission_idx])
            self._omissions.append(base_genome[omission_idx:omission_idx + omission_size])

        for contig in self._contigs:
            for read_index in range(0, len(contig), overlap_size):
                read = base_genome[read_index:read_index + read_size]
                self._genome_samples.append(read)

    def reads(self):
        '''
            Iterator over the samples (b/c self_genome_samples is private)
        '''
        for read in self._genome_samples:
            yield read
