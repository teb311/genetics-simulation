from assembly.utils import k_mers

def test_kmers_invalid_input():
    for n in range(10):
        string = 'a' * n
        k_mers(string, n) # Has to work...
        try:
            k_mers(string, n+1)
            assert False # Should raise an error,
        except:
            continue

def test_kmers():
    inputs = [
        'aaabbbcccdaaabbbcccd',
        '123456778912345677891234567789',
    ]

    for string in inputs:
        for k in [8, 9, 10]:
            left_idx = 0
            print(k, string)
            for k_mer in k_mers(string, k=k):
                assert len(k_mer) == k
                assert k_mer == string[left_idx:left_idx + k]
                left_idx += 1

            # k_mers add up to the original string
            assert left_idx == len(string) - k
