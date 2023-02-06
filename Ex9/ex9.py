import json

# The original Python object
obj = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 2
}

# Convert the Python object to a JSON string
json_str = json.dumps(obj)

# Load the JSON string into a Python dictionary
data = json.loads(json_str)

# Use a set to store unique values
unique_values = set(data.values())

# Iterate over the key-value pairs in the dictionary
# and add the pair to a new dictionary only if the value
# is unique
unique_data = {}
for key, value in data.items():
    if value in unique_values:
        unique_values.remove(value)
        unique_data[key] = value

# Convert the new dictionary back to a JSON string
unique_json_str = json.dumps(unique_data)

print(unique_json_str)
# Output: {"a": 1, "b": 2, "c": 3}