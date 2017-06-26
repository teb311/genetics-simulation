from collections import Counter
from symnome.sampled_consistent_overlap import SampledConsistentOverlapGenome

def test_reads_overlap_rate():
    '''
    The reads must have consistent overlapping and shape: the reads must be length
    2*overlap_size. the reads must each overlap with the read behind and ahead of it
    equally and in a length matching overlap_size.
    '''
    for length in [1000, 2000, 3000]:
        for overlap_size in [6, 10, 30]:
            sg = SampledConsistentOverlapGenome(length=length, overlap_size=overlap_size)
            base_genome = sg.true_genome()
            read_size = 2 * overlap_size

            # First and last have special rules specifically the very first
            # overlap_size and last overlap_size do not repeat in the genome
            first = True

            for read in sg.reads():
                if first:
                    first = False
                    first_ol_size = read[0:overlap_size]
                    assert first_ol_size == base_genome[0:overlap_size]

                    occurances = Counter()
                    second_ol_size = read[overlap_size:2 * overlap_size]
                    occurances.update([bp_pos for bp_pos in enumerate(second_ol_size)])
                    assert second_ol_size == base_genome[overlap_size:2 * overlap_size]
                else:
                    base_pairs_and_idx = enumerate(read)
                    occurances.update(bp_idx for bp_idx in base_pairs_and_idx)
                    assert read in base_genome
                    assert len(read) == read_size

            last_ol_size = read[-overlap_size:0]
            assert last_ol_size == base_genome[-overlap_size:0]

            second_last_ol_size = read[-2 * overlap_size:-overlap_size]
            assert second_ol_size == base_genome[-2 * overlap_size:-overlap_size]

            occurances.update([bp_pos for bp_pos in enumerate(second_last_ol_size)])
            for basepair_position in occurances:
                assert occurances[basepair_position] == 2

def test_reads_base_pair_count():
    '''
    Each base pair is represented exactly twice in the reads, except the
    first overlap_size and last overlap_size
    '''
