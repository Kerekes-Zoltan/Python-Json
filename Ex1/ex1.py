import json

json_obj = '{"Name":"Zoltan", "Age":23 }'

python_obj = json.loads(json_obj)

print("\nJSON Data: ", python_obj)
print("\nName: ", python_obj["Name"])
print("Age: ", python_obj["Age"])