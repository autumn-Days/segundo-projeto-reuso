def quicksort(v, l, r):
    i, j = l, r
    p = v[(l + r) // 2]
    while i <= j:
        while v[i] < p: i += 1
        while v[j] > p: j -= 1
        if i <= j:
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
    if l < j: quicksort(v, l, j)
    if i < r: quicksort(v, i, r)

v = [34,7,23,32,5,62,78,1,45,9,12,56,89,4,27,16,3,90,11,54,
     21,8,67,14,29,6,10,2,99,41,18,25,30,15,55,19,28,13,20,17]

quicksort(v, 0, len(v) - 1)
print(" ".join(map(str, v)))
