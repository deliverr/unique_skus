from typing import Dict, List, Tuple, Set

# An algorithm based on Floyd–Warshall
# https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm


def unique_skus(skus: List[int], equal_pairs: List[Tuple[int, int]]):
    neighbors: Dict[int, Set[int]] = {s: set([s]) for s in skus}

    for a, b in equal_pairs:
        neighbors[a].add(b)
        neighbors[b].add(a)

    for a in skus:
        for b in skus:
            for c in skus:
                if b in neighbors[a] and c in neighbors[b]:
                    neighbors[a].add(c)
                    neighbors[c].add(a)

    sku_to_unique_sku = {a: min(*neighbors[a]) for a in skus}
    return list(set(sku_to_unique_sku.values())), sku_to_unique_sku


print(unique_skus([1, 2, 4, 5, 6], [(1, 2), (2, 5), (4, 6)]))
