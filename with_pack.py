import ollama

client = ollama.Client()


model = "gemma3:1b"
prompt = "What do you know about Rick from the show Rick and Morty?"

response = client.generate(model=model, prompt=prompt)

print("Response in Ollama:")
print(response.response)
