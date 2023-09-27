import math
def zig_zag(matrix):
    if not matrix:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []

    for diagonal_sum in range(m + n - 1):
        if diagonal_sum % 2 == 0:
            if diagonal_sum < m:
                row, col = diagonal_sum, 0
            else:
                row, col = m - 1, diagonal_sum - m + 1
            while row >= 0 and col < n:
                result.append(matrix[row][col])
                row -= 1
                col += 1
        else:
            if diagonal_sum < n:
                row, col = 0, diagonal_sum
            else:
                row, col = diagonal_sum - n + 1, n - 1
            while row < m and col >= 0:
                result.append(matrix[row][col])
                row += 1
                col -= 1
    print(result)
    return result

def merge_sort(array):
    right_array = []
    left_array = []
    amount_of_dividing = math.log(64, 2)
    if array//2 == 2:
        if array[0] > array[1]:
            temp = array[0]
            array[0] = array[1]
            array[1] = temp
    else:
        for divide in range(amount_of_dividing):
            for i in range(len(array) // 2):
                left_array.append(array[i])
                j = i
                while len(left_array) == len((array) // 2) and j <= i:
                    right_array.append(array[j])






if __name__ == "__main__":
    zig_zag([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
])

