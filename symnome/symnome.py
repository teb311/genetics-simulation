import random
DNA_CHARSET = 'atcg'

def clean_dna_genome(length=64):
    '''
        Given an integer return a random string containing only the
        characters atcg

        length (int): the length of the string
    '''
    genome = [random.choice(DNA_CHARSET) for _ in range(length)]
    return ''.join(genome)
