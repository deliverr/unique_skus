
# An algorithm based on the "disjoint-set" (a.k.a. "union-find") datastructure:
# https://en.wikipedia.org/wiki/Disjoint-set_data_structure
# Also sometimes refferred to - erroneously - as kurscal's algorithm or the
# minimum-spanning-tree algorithm.

# One of the most sophisticated ways to solve the unique_skus problem, it has
# asymptotically optimal run-time, but can be rather tricky to get right.

# Typical know-it-all candidates using this algorithm make it much more
# complex than the below solution.


def unique_skus(skus, equal_pairs):
    parent = {sku: sku for sku in skus}

    def root(sku):
        if parent[sku] != sku:
            parent[sku] = root(parent[sku])
        return parent[sku]

    for left, right in equal_pairs:
        parent[root(left)] = root(right)

    for sku in skus:
        root(sku)

    return list(set(parent.values())), parent


print(unique_skus([1, 2, 4, 5, 6], [(1, 2), (2, 5), (4, 6)]))
