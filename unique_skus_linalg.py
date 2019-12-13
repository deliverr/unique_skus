from typing import Dict, List, Tuple
import numpy as np
from numpy import linalg
from collections import defaultdict


# Reject anybody that implements an algorithm like this in an interview!
# They're certain to mess things up by implementing unnecessarily complex
# mathematical nonesense for the fun of it ;-)


def unique_skus(skus: List[int], equal_pairs: List[Tuple[int, int]]):
    sku_to_index = {sku: idx for idx, sku in enumerate(skus)}

    updated_pairs = list(equal_pairs)
    updated_pairs.extend((b, a) for a, b in equal_pairs)  # make symmetric
    updated_pairs.extend((a, a) for a in skus)

    # give every node the same degree
    sku_to_degree: Dict[int, int] = defaultdict(int)
    for left, right in updated_pairs:
        sku_to_degree[left] += 1
        sku_to_degree[right] += 1
    max_degree = max(*sku_to_degree.values())

    for sku in skus:
        for i in range(sku_to_degree[sku], max_degree):
            updated_pairs.append((sku, sku))

    # Represent as a matrix
    mat = np.zeros((len(skus), len(skus)))
    for left, right in updated_pairs:
        mat[sku_to_index[left], sku_to_index[right]] = 1

    # Raise mat a high power, normalizing to prevent stability problems
    for i in range(10):
        mat = linalg.matrix_power(mat, 2)
        mat = mat / linalg.norm(mat)

    # Use the possible rows as the unique keys
    sku_to_unique_sku = {}
    for sku, index in sku_to_index.items():
        sku_to_unique_sku[sku] = "".join(
                "." if abs(x) > 0.0 else "-" for x in mat[index])

    return list(set(sku_to_unique_sku.values())), sku_to_unique_sku


print(unique_skus([1, 2, 4, 5, 6], [(1, 2), (2, 5), (4, 6)]))
