import numpy as np
from symnome.base_genome import BaseGenome

class RandomlySampledGenome(BaseGenome):
    '''
        A simulation of one difficulty in genome sequencing: repeated reads from
        the true genome. Here, a true base genome is constructed and several reads
        are generated from the original genome

        A MultiCopyGenome is based on a true genome (from the BaseGenome class)
        but sampled n_reads times with the specified read_size at random starting
        locations.
    '''

    def __init__(self, length=500, read_size=200, n_reads=16):
        '''
            length (int): the legnth of the base genome
            read_size (int): the minimum size of any individual repeated read
            n_reads (int): the maximum size of any individual repeated read
        '''
        super().__init__(length=length)

        base_genome = self.true_genome()
        genome_size = len(base_genome)
        max_idx = genome_size - read_size

        self._genome_samples = []
        for _ in range(n_reads):
            copy_location = np.random.randint(0, high=max_idx)
            read = base_genome[copy_location:copy_location + read_size]
            self._genome_samples.append(read)

    def reads(self):
        '''
            Iterator over the samples (b/c self_genome_samples is private)
        '''
        for read in self._genome_samples:
            yield read
