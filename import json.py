import json

# Open and load JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Print formatted JSON
print(json.dumps(data, indent=4))
