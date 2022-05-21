import sys

arr = [1, 2, 3, 4, 5]
total = 0
maximum = -sys.maxsize
minimum = sys.maxsize
for i in range(len(arr)):
    total += arr[i]
    if arr[i] > maximum: maximum = arr[i]
    if arr[i] < minimum: minimum = arr[i]

print("maximum sum is", total - minimum)
print("minimum sum is", total - maximum)
print(total)
