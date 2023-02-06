import json

# JSON encoded data
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

# Convert JSON data into Python objects
python_obj = json.loads(json_data)

# Access data using key-value pairs
print("Name: ", python_obj['name'])
print("Age: ", python_obj['age'])
print("City: ", python_obj['city'])
