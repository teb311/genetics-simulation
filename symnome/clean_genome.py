import random


class CleanGenome:
    DNA_CHARSET = 'atcg'

    def __init__(self, length=64):
        '''
            Given an integer return an array of random single characters
            containing only the characters atcg (specified by the class variable
            DNA_CHARSET)

            length (int): the length of the genome
        '''
        self._genome = [random.choice(CleanGenome.DNA_CHARSET) for _ in range(length)]

    def whole_genome(self):
        return ''.join(self._genome)

    def k_mers(self, k=16):
        '''
            Given k, return an iterator that yields each k-mer for this CleanGenome.

            k (int): the size of each k-mer yielded by the iterator
        '''
        idx = 0
        while idx < len(self._genome) - k:
            yield ''.join(self._genome[idx:idx + k])
            idx += 1
