items = [6, 20, 8, 8, 19, 56, 23, 87, 41, 49, 53]


def mergesort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        leftarr = arr[:middle]
        rightarr = arr[middle:]

        mergesort(leftarr)
        mergesort(rightarr)

        i = 0
        j = 0
        k = 0
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
                k += 1
            else:
                arr[k] = rightarr[j]
                j += 1
                k += 1

        while i < len(leftarr):
            arr[k] = leftarr[i]
            i += 1
            k += 1

        while j < len(rightarr):
            arr[k] = rightarr[j]
            j += 1
            k += 1


print(items)
mergesort(items)
print(items)
