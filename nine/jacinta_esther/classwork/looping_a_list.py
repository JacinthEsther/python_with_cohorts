
class_a = ["Esther_Jacinta", "Adeola", "Judith", "Damilola", "Lota"]
class_b = ["Jibola", "Jerry", "Oluwadamilola", "Lekan", "Loiz_Increase"]
max_class_a = max(class_a, key=len)
max_class_b = max(class_b, key=len)

if len(max_class_a) > len(max_class_b):
    print("class_a: ", max_class_a)
else:
    print("class_b: ", max_class_b)
print()
classes = [class_a, class_b]
for i in range(len(classes)):

    for j in range(len(classes[i])):
        largest = len(classes[0])
        print(classes[i][j], end=" ")
        if len(classes[i][j]) > largest:
            largest = len(classes[i][j])
            name_str = classes[i][j]
print()
print("The length of the longest name is", largest)
print("The longest name is", name_str)
print()
for i in classes:
    for j in i:
        if len(j) > largest:
            largest = len(j)
            name_str = j
            print(largest)
            print(name_str)