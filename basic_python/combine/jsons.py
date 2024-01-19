import json

person = {"name": "John", "yes": True, "no": False}
jsonPerson = json.dumps(person, indent=4, separators=('|', '='))
print(jsonPerson)