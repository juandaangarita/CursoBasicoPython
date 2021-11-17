def array_diff(a, b):
    array_diff = []
    for element_b in b:
        if element_b not in a:
            array_diff.append(el)

    return array_diff

print(array_diff([1,2,3], [1,2]))