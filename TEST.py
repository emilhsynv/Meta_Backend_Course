# numbers = [15, 30, 47, 82, 95]
# def lesser(numbers):
#    return numbers < 50

# small = list(filter(lesser, numbers))
# print(small)

from Algorithms import bubble_sort
arr = [15, 30, 47, 82, 95, 64, 34, 35, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)