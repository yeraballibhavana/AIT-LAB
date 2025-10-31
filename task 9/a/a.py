import os
from openai import OpenAI

api_key = "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"

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

messages = []

while True:
    user_message = input("You: ")
    if user_message.lower() == 'quit':
        break
    messages.append({"role": "user", "content": user_message})

    completion = client.chat.completions.create(
      extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
      },
      extra_body={},
      model="nvidia/nemotron-nano-9b-v2:free",
      messages=messages
    )
    assistant_response = completion.choices[0].message.content
    print(f"Bot: {assistant_response}")
    messages.append({"role": "assistant", "content": assistant_response})