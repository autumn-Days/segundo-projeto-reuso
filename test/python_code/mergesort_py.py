def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def main():
    v = [34,7,23,32,5,62,78,1,45,9,12,56,89,4,27,16,3,90,11,54,21,8,67,14,29,6,10,2,99,41,18,25,30,15,55,19,28,13,20,17]

    mergesort(v)

    print(" ".join(map(str, v)))


main()
