import json
from openai import OpenAI
from newScript import parse_json
client = OpenAI(api_key='sk-')

error_list = []

def send_to_chatgpt(messg):
    print("----- streaming request -----")
    print("Original Error message was: ", messg)
    print("________________")
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": messg,
            },
        ],
        stream=True,
    )

    for chunk in stream:
        if not chunk.choices or chunk.choices[0].delta.content is None:
            break
        print(chunk.choices[0].delta.content, end="")
    print()


def find_in_json(data, key="stderr"):
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key and v:
                # print(v, type(v))
                error_list.append(v)
            elif isinstance(v, (dict, list)):
                find_in_json(v, key)
    elif isinstance(data, list):
        for item in data:
            find_in_json(item, key)


if __name__ == '__main__':
    json_file_path = "C:\\Users\\giris\\Documents\\0uni\\495\\drive-download-20240225T212209Z-001\\Synchronous Sessions\\Bash\\zwy324.json" # path to JSON file with logs
    with open(json_file_path, 'r') as file:
        json_data = file.read()  
        parsed_json_arr = parse_json(json_data)
        for i, j in enumerate(parsed_json_arr): # this iterates through the file and prints all errors
            if len(j["stderr"]) > 0: # contains an error
                # print(f"Error on line {i}: ", j[]
                if (j["stderr"][:2] == "ls"): 
                    continue
                print(j["stderr"])
                
                gptPromptString = f'What is the error here? Running this command: {j["full_command"]} \ results in this error: {j["stderr"]}. The last command run before this one was: {parsed_json_arr[i-1]["full_command"]}. Is there any relation to this error?'
                send_to_chatgpt(gptPromptString)

                # print(gptPromptString)