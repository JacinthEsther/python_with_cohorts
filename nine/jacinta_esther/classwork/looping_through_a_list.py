name = ["Jacinta", "Adeol", "Judit", "Damilola", "Lotar"]
temp = " "
for i in range(len(name)):
    # largest = len(name[0])
    if len(name[i]) == 5:
        index = i
        print(index, end=" ")
        print(name[i])
    if name[i].__contains__("nta"):
        print(name[i])

#  if len(name[i]) > largest:
# largest = len(name[i])
# name_str = name[i]
#  index = i
# print("The length of the longest name is",largest)
#  print("The longest name is",name_str)
# print("The index with the longest name is",index)



