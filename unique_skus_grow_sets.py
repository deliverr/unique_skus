from typing import Dict, Set, List, Tuple

# An algorithm that maps each sku to a set of equal skus and keeps growing
# the sets until they can't grow any more.


def unique_skus(skus: List[int], equal_pairs: List[Tuple[int, int]]):
    sets: Dict[int, Set[int]] = {sku: set([sku]) for sku in skus}
    for x in skus:  # Enough iterations to get the sets to finish growing.
        for a, b in equal_pairs:
            sets[a] = sets[b] = sets[a].union(sets[b])

    sku_to_unique_sku = {k: list(v)[0] for k, v in sets.items()}

    return list(set(sku_to_unique_sku.values())), sku_to_unique_sku


print(unique_skus([1, 2, 4, 5, 6], [(1, 2), (2, 5), (4, 6)]))
