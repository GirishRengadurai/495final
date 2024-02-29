import json

def process_json(data):
    command_frequency = {}
    command_duration = {}

    def process_item(item, current_duration=0):
        nonlocal command_frequency, command_duration

        if isinstance(item, dict):
            for key, value in item.items():
                if key == "command":
                    command_frequency[value] = command_frequency.get(value, 0) + 1
                    command_duration[value] = command_duration.get(value, 0) + current_duration
                elif isinstance(value, (dict, list)):
                    process_item(value, current_duration)
        elif isinstance(item, list):
            for element in item:
                process_item(element, current_duration)

    process_item(data)

    return command_frequency, command_duration

file_path = 'log_part_1.json'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        frequency, duration = process_json(json_data)

        # Print results
        for command, count in frequency.items():
            print("Command is:", command, "Frequency of:", count)
#print(f"Command: {command}, Frequency: {count}, Total Duration: {duration[command]} seconds")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except json.JSONDecodeError:
    print(f"Error decoding JSON in file: {file_path}")
