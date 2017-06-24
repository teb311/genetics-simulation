from symnome.clean_genome import CleanGenome

def test_genome_charset():
    assert CleanGenome.DNA_CHARSET == 'atcg'


def test_whole_genome():
    for genome_size in [4, 64, 256, 1024]:
        genome = CleanGenome(length=genome_size)
        genome_str = genome.whole_genome()
        assert isinstance(genome_str, str)
        assert len(genome_str) == genome_size
        assert all_allowed(genome_str, CleanGenome.DNA_CHARSET)


def test_kmers():
    for genome_size in [256, 512, 1024, 2048]:
        genome = CleanGenome(length=genome_size)
        whole_genome = genome.whole_genome()

        for k in [8, 16, 32, 64]:
            left_idx = 0

            for k_mer in genome.k_mers(k=k):
                assert len(k_mer) == k
                print(left_idx, whole_genome)
                assert k_mer == whole_genome[left_idx:left_idx + k]
                left_idx += 1

            # k_mers add up to whole_genome
            assert left_idx == len(whole_genome) - k


def all_allowed(genome, charset):
    for c in genome:
        if c not in CleanGenome.DNA_CHARSET:
            return False

    return True
