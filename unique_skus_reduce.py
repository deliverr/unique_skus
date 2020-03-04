from functools import reduce


def link(m, pair):
    a, b = pair

    bval = m.get(b, b)
    aval = m.get(a, a)

    m[b] = bval

    for k, v in list(m.items()):
        if v == aval:
            m[k] = bval
    return m


def unique_skus(skus, equal_pairs):
    result = reduce(link, equal_pairs, {a: a for a in skus})
    return list(set(result.values())), result


print(unique_skus([1, 2, 4, 5, 6], [(1, 2), (2, 5), (4, 6)]))
