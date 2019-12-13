from typing import Dict, List, Tuple

# One of the simplest algorithms for unique_skus.
# It has asymptotically optimal run time.


def unique_skus(skus: List[int], equal_pairs: List[Tuple[int, int]]):
    edges: Dict[int, List[int]] = {sku: [] for sku in skus}
    for left, right in equal_pairs:
        edges[left].append(right)
        edges[right].append(left)

    sku_to_unique_sku: Dict[int, int] = {}

    for sku in skus:
        frontier = [sku]
        while frontier:
            connected_sku = frontier.pop()
            if connected_sku not in sku_to_unique_sku:
                sku_to_unique_sku[connected_sku] = sku
                frontier.extend(edges[connected_sku])

    return list(set(sku_to_unique_sku.values())), sku_to_unique_sku


print(unique_skus([1, 2, 4, 5, 6], [(1, 2), (2, 5), (4, 6)]))
