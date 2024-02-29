import json

def find_url(data, key="url"):
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                print(f"Found '{key}': {v}")
            elif isinstance(v, (dict, list)):
                find_url(v, key)
    elif isinstance(data, list):
        for item in data:
            find_url(item, key)

# Replace 'your_json_file.json' with the actual file path
file_path = 'lfy55-77587368.json'

try:
    with open(file_path, 'r') as file:
        json_data = json.load(file)
        find_url(json_data)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except json.JSONDecodeError:
    print(f"Error decoding JSON in file: {file_path}")
