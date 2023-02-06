import json

# Example dictionary
data = {
    "apple": 3,
    "banana": 5,
    "cherry": 1
}

# Convert dictionary to JSON data
json_data = json.dumps(data, sort_keys=True, indent=4)

# Print JSON data
print(json_data)
