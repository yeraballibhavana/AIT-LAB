from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

api_key = "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"

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

messages = [
    {"role": "system", "content": "I'm Bhavana's personal chatbot assistant. Respond helpfully, personally, and warmly as if you are assisting Bhavana directly."}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

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
    messages.append({"role": "assistant", "content": assistant_response})

    return jsonify({'response': assistant_response})

if __name__ == '__main__':
    app.run(debug=True)
