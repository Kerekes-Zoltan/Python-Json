import json

python_obj = {"Name": "Zoltan", "Age": "23", "Height": "183cm"}

print("Python Data is a ", type(python_obj))

json_data = json.dumps(python_obj)

print("Python object converted to JSON data: ", json_data)