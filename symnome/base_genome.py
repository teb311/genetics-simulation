import random

class BaseGenome:
    '''
        The BaseGenome contains methods for things that every genome must do. BaseGenome
        creates the master genome array, and exposes methods for examining the clean
        (error free) genome data.
    '''
    DNA_CHARSET = 'atcg'

    def __init__(self, length=64):
        '''
            Given an integer return an array of random single characters
            containing only the characters atcg (specified by the class variable
            DNA_CHARSET)

            length (int): the length of the genome
        '''
        self._genome = [random.choice(BaseGenome.DNA_CHARSET) for _ in range(length)]

    def true_genome(self):
        return ''.join(self._genome)
