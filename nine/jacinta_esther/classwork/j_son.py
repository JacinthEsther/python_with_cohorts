import json


a = open("C:/Users/Public/data.json", )
data = json.load(a)

print(data)

colors = json.dumps(data)

file = open("colors.json", "w")
file.write(colors)

print(file)