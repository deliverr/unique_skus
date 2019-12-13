from typing import Dict

# A very common solution by junior candidates.  It requires very little
# knowledge of algorithms and achieves a poor (quadratic) runtime.


def unique_skus(skus, equal_pairs):
    sku_to_unique_sku: Dict[int, int] = {}
    for left, right in equal_pairs:
        if left in sku_to_unique_sku:
            if right in sku_to_unique_sku:
                # Both skus are mapped
                old = sku_to_unique_sku[left]
                new = sku_to_unique_sku[right]
                for sku, unique_sku in list(sku_to_unique_sku.items()):
                    if unique_sku == old:
                        sku_to_unique_sku[sku] = new
            else:
                # Only the left sku is mapped
                sku_to_unique_sku[right] = sku_to_unique_sku[left]
        elif right in sku_to_unique_sku:
            # Only the right sku is mapped
            sku_to_unique_sku[left] = sku_to_unique_sku[right]
        else:
            # Neither sku is mapped
            sku_to_unique_sku[left] = sku_to_unique_sku[right] = left

    for sku in skus:
        if sku not in sku_to_unique_sku:
            sku_to_unique_sku[sku] = sku

    return list(set(sku_to_unique_sku.values())), sku_to_unique_sku


print(unique_skus([1, 2, 4, 5, 6], [(1, 2), (2, 5), (4, 6)]))
