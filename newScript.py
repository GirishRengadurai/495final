import json

def parse_json(json_data):
    try:
        data = json.loads(json_data)
        timestamp = data["timestamp"]
        log_id = data["log_id"]
        machine_id = data["machine_id"]
        session_id = data["session_id"]
        course_id = data["course_id"]
        log_type = data["log_type"]
        arr = []
        arr.append(f"Timestamp: {timestamp}")
        arr.append(f"Log ID: {log_id}")
        arr.append(f"Machine ID: {machine_id}")
        arr.append(f"Session ID: {session_id}")
        arr.append(f"Course ID: {course_id}")
        arr.append(f"Log Type: {log_type}")

        commands = data["log"]["commands"]
        arr = [command for command in commands]
        return arr
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

if __name__ == '__main__':
    json_file_path = "C:\\Users\\giris\\Documents\\0uni\\495\\drive-download-20240225T212209Z-001\\Synchronous Sessions\\Bash\\sexysushi_One.json" # path to JSON file with logs
    with open(json_file_path, 'r') as file:
        json_data = file.read()  
        parsed_json_arr = parse_json(json_data)
        for i, j in enumerate(parsed_json_arr): # this iterates through the file and prints all errors
            if j[0] and type(j) is tuple : # contains an error
                print(f"Error on line {i}:")
                print(j)