def k_mers(string, k=16):
    '''
        Given a string and a k value, return an iterator over
        the strings k-mers.

        string (str): the string
        k (int): the value for k
    '''
    if k > len(string):
        raise ValueError('The length of the input string must be less than the provided k to k-merize.')

    idx = 0
    while idx < len(string) - k:
        yield ''.join(string[idx:idx + k])
        idx += 1
