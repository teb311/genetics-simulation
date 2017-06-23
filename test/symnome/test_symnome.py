from symnome import symnome as sym

DNA_CHARSET = 'atcg'

def all_allowed(genome, charset):
    for c in genome:
        if c not in charset:
            return False

    return True


def test_simple_geneome():
    for cur_len in [4, 64, 256, 1024]:
        genome = sym.clean_dna_genome(length=cur_len)
        assert len(genome) == cur_len
        assert all_allowed(genome, DNA_CHARSET)
