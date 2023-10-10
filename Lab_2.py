def hampter(S, C, hamsters):
    food_needs = 0
    hamsters.sort(key=lambda x: x[1])

    for hamster in hamsters:
        print(hamster)

    while True:
        for hamster in hamsters:
            food_needs += hamster[0] + hamster[1] * (C - 1)
        C -= 1
        if food_needs < S:
            break
        hamsters.pop()
        food_needs = 0





hamsters = [[1, 7],
            [2, 5],
            [3, 3],
            [3, 1],
            [3, 2],
            [0, 0],
            [0, 0],
            [0, 0]]

hampter(10, 5, hamsters)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Copy data to temporary arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Example usage:
my_array = [12, 11, 13, 5, 6, 7]
merge_sort(my_array)
print("Sorted array:", my_array)

def hampter(S, C, hamsters):
    food_needs = 0
    hamsters.sort(key=lambda x: x[1])

    for hamster in hamsters:
        print(hamster)

    for hamster in hamsters:
        food_needs += hamster[0] + hamster[1] * (C - 1)

hamsters = [[1, 2],
            [3, 4],
            [5, 6]]

hampter(10, 3, hamsters)