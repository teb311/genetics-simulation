from symnome.base_genome import BaseGenome

def test_genome_charset():
    assert BaseGenome.DNA_CHARSET == 'atcg'


def test_whole_genome():
    for genome_size in [4, 64, 256, 1024]:
        genome = BaseGenome(length=genome_size)
        genome_str = genome.true_genome()
        assert isinstance(genome_str, str)
        assert len(genome_str) == genome_size
        assert all_allowed(genome_str, BaseGenome.DNA_CHARSET)


def all_allowed(genome, charset):
    for c in genome:
        if c not in BaseGenome.DNA_CHARSET:
            return False

    return True
