arr1 = [5, 6, 7]
arr2 = [3, 6, 10]
count = 0
count1 = 0

for i in range(len(arr1)):

    if arr1[i] > arr2[i]:
        count += 1
    elif arr1[i] < arr2[i]:
        count1 += 1

print("player1 has", count, "point")
print("player2 has", count1, "point")
