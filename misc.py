# coding=utf-8

import math

def genr_sublist(org_list, slice_size):
    """
    >>> for temp_list in genr_sublist(range(20), 5):
            print temp_list

    [0, 1, 2, 3, 4]
    [5, 6, 7, 8, 9]
    [10, 11, 12, 13, 14]
    [15, 16, 17, 18, 19]
    """
    slice_count = int(math.ceil(len(org_list) / float(slice_size)))
    for i in xrange(slice_count):
        yield org_list[i * slice_size:(i + 1) * slice_size]
