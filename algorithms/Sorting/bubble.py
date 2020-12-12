items = [6, 20, 8, 8, 19, 56, 23, 87, 41, 49, 53]


def bubblesort(items):
    for i in range(len(items)-1, 0, -1):
        for j in range(i-1):
            if items[i] < items[j]:
                items[j], items[i] = items[i], items[j]
    return items


print(items)
print(bubblesort(items))
