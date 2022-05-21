arr = [-4, 3, -9, 0, 4, 1]
count1 = 0
count2 = 0
count3 = 0
for i in range(len(arr)):
    if arr[i] > 0:
        count1 += 1
    elif arr[i] == 0:
        count2 += 1
    elif arr[i] < 0:
        count3 += 1

print(f'{count1 / len(arr):>.6f}')
print(f'{count3 / len(arr):>.6f}')
print(f'{count2 / len(arr):>.6f}')
