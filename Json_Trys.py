import json

mydict = {
    "people": [
        {
            "name": "Bob",
            "age": 28,
            "weight": 80
         },
        {
            "name": "Anna",
            "age": 34,
            "weight": 67,
        }
    ]
}

# writing to a file
json_string = json.dumps(mydict, indent=2)
with open("mydata.json", "w") as f:
    f.write(json_string);

# loading from a file
with open("mydata.json", "r") as f:
    json_object = json.loads(f.read())
print(json_object)
print(json_object["people"])
print(json_object["people"][0])
print(json_object["people"][0]["name"])