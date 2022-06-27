import numpy as np
from itertools import permutations


def accuracy(pred, truth):
    return np.sum(pred == truth) / len(pred) 


def replace_dict(arr1, arr2):
    unique1 = np.unique(arr1).tolist()
    unique2 = np.unique(arr2).tolist()
    if len(unique1) != len(unique2):
        return None, None
    perms1 = list(permutations(unique1))
    perms2 = list(permutations(unique2))
    results = []

    for perm1 in perms1:
        for perm2 in perms2:
            replace_dict = dict(zip(perm1, perm2))
            arr1_transformed = np.array([
                replace_dict[x] for x in arr1
            ])
            acc = accuracy(arr1_transformed, arr2)
            results.append((replace_dict, acc))

    return max(results, key=lambda x: x[1])


def replace(arr, repdict):
    return np.array([
        repdict[val] for val in arr
    ])