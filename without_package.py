import json
import requests

url = "http://127.0.0.1:11434/api/chat"

payload = {
    "model": "gemma3:1b",
    "messages": [{"role": "user", "content": "What do you think about the pink flyod?"}]
}

response = requests.post(url, json=payload, stream=True, timeout=10)

if response.status_code == 200:
    print("Streaming response in Ollama:")
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                json_data = json.loads(line)
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
                print(f"\nFailed to parse line: {line}")
    print()  # Print a newline at the end

else:
    print(f"Error: {response.status_code} - {response.text}")
