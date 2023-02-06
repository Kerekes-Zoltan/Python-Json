import json

# Load the existing JSON file
with open('existing_file.json', 'r') as file:
    data = json.load(file)

# Write the data to a new JSON file
with open('new_file.json', 'w') as file:
    json.dump(data, file, indent=4)