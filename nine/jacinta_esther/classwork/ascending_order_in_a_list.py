class_a = ["Esther_Jacinta", "Adeola", "Judith", "Damilola", "Lota"]
a =""
for i in range(1,len(class_a)):
    for j in range(i,0,-1):
        if class_a[i] < class_a[i-1]:
            a = class_a[i-1]
            class_a[i-1] = class_a[i]
            class_a[i] = a

        else: break
    print(class_a[i])