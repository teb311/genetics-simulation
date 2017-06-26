import numpy as np
from symnome.base_genome import BaseGenome

class SampledConsistentOverlapGenome(BaseGenome):
    '''
        A simulation of near ideal data: reads from the true genome overlap consistently.
        Here, a true base genome is constructed and several reads are generated from the
        original genome such that every read overlaps with the reads on either side of it.
        Overlap lengths are always as specified, and the writer cause every base pair to
        be represented exactly 2 times with the exception of the first and last overlap_size
        base pairs.

        Say the original was 'aaaattttccccggggaaaattttccccggggaaaattttccccgggg'
        and the ovelap size is 6 the following reads are created:

        aaaattttccccggggaaaattttccccggggaaaattttccccgggg =>
        aaaattttcccc
              ttccccggggaa
                    ggggaaaatttt
                          aattttccccgg
                                ccccggggaaaa
                                        aaaattttccc
                                              ttccccgggg

        A MultiCopyGenome is based on a true genome (from the BaseGenome class)
        but sampled n_reads times with the specified read_size at random starting
        locations.
    '''

    def __init__(self, length=500, overlap_size=6):
        '''
            length (int): the length of the base genome
            overlap_size (int): the length of the overlapping reigons
        '''
        super().__init__(length=length)

        base_genome = self.true_genome()
        genome_size = len(base_genome)
        read_size = overlap_size * 2

        self._genome_samples = []
        for read_index in range(0, length, overlap_size):
            read = base_genome[read_index:read_index + read_size]
            self._genome_samples.append(read)

    def reads(self):
        '''
            Iterator over the samples (b/c self_genome_samples is private)
        '''
        for read in self._genome_samples:
            yield read
