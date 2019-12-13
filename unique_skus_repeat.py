
# A very simple algorithm with terrible performance.


def unique_skus(skus, equal_pairs):
    unique_skus = {sku: sku for sku in skus}

    updated = True
    while updated:
        updated = False
        for left, right in equal_pairs:
            if unique_skus[left] != unique_skus[right]:
                updated = True
                unique_skus[left] = unique_skus[right]

    return list(set(unique_skus.values())), unique_skus


print(unique_skus([1, 2, 4, 5, 6], [(1, 2), (2, 5), (4, 6)]))
