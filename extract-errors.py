import json

def extract_enames(json_file_path):
    with open(json_file_path, 'r') as my_file:
        tmp_var = json.load(my_file)
    for u in tmp_var["original_checkpoint"]:
        print(u, type(u))
        # print(tmp_var.keys())




def extract_fields(json_file_path, field_name):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    items_with_field = [item for item in data if field_name in item]

    return items_with_field


# Provide the path to your JSON file
json_file_path = "C:\\Users\\giris\\Documents\\0uni\\495\\drive-download-20240225T212209Z-001\\Synchronous Sessions\\Bash\\sexysushi_One.json"
#json_file_path = "C:\\Users\\admin\\Documents\\0uni\\495\ " 
field_name = 'ename'

# Extract fields with the specified name from the JSON file
result = extract_fields(json_file_path, field_name)

# Print the result
print(result)
