import json

def contains_complex(json_string):
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError:
        return False

    for value in data.values():
        if isinstance(value, (list, dict)):
            return True
    return False

# Example usage
print(contains_complex('{"a": 1, "b": [1, 2, 3]}')) # True
print(contains_complex('{"a": 1, "b": 2}')) # False
