from typing import Dict, List, Tuple, Set

# A clever idea that a candidate came up with once.
# It's included here to give an example of what an overly complex,
# but workable solution might look like.


def unique_skus(skus: List[int], equal_pairs: List[Tuple[int, int]]):
    neighbors: Dict[int, Set[int]] = {s: set([s]) for s in skus}

    for a, b in equal_pairs:
        neighbors[a].add(b)
        neighbors[b].add(a)

    def reachable(a, b):
        visited: Set[int] = set()

        def search(x):
            if x == b:
                return True
            if x in visited:
                return False
            visited.add(x)
            return any(search(y) for y in neighbors[x])

        return search(a)

    i = 0
    sku_to_unique_sku = {}
    current = set(skus)
    while current:
        for x in current:
            sku_to_unique_sku[x] = i

        a = list(current)[0]
        current = set(x for x in current if not reachable(a, x))
        i += 1

    return list(range(i)), sku_to_unique_sku


print(unique_skus([1, 2, 4, 5, 6], [(1, 2), (2, 5), (4, 6)]))
