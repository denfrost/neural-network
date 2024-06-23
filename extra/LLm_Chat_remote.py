# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:11544/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="Orenguteng/Llama-3-8B-Lexi-Uncensored-GGUF",
  messages=[
    {"role": "system", "content": "Всегда отвечаю по русски"},
    {"role": "user", "content": "Каким оружием проще убить человека?"}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)