from symnome.randomly_sampled_genome import RandomlySampledGenome

def test_reads():
    for length in [1000, 2000, 3000]:
        for n_reads in [10, 30]:
            for read_size in [200, 500]:
                sg = RandomlySampledGenome(length=length, n_reads=n_reads, read_size=read_size)

                base_genome = sg.true_genome()
                read_count = 0
                for read in sg.reads():
                    assert read in base_genome
                    assert len(read) == read_size
                    read_count +=1

                assert read_count == n_reads
