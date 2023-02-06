import json

python_dict = {"Name": "Zoltan", "Age": 23}
python_list = ["black", "white", "red"]
python_str = "JSON DATA"
python_int = 123
python_float = 123.123
python_T = True
python_F = False
python_N = None

json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_str = json.dumps(python_str)
json_int = json.dumps(python_int)
json_float = json.dumps(python_float)
json_T = json.dumps(python_T)
json_F = json.dumps(python_F)
json_N = json.dumps(python_N)

print("All Python Data converted to JSON Data: ", json_dict, " ", json_list, " ", json_str, " ", json_int, " ", json_float, " ", json_T, " ", json_F, " ", json_N)