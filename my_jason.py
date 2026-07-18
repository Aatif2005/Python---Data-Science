import json

obj = {
    "name": "Aatif",
    "age": 20
}

file = open("data.json", "w")
json.dump(obj, file)
file.close()