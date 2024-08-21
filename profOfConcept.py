from openai import OpenAI
import json
import os

with open(r'C:\Users\awolf\OneDrive\Documents\Projects\ApiKeys.json', 'r') as f:
  data = json.load(f)
client=OpenAI(api_key = data["OpenAi"])
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

message = input("User : ")

messages.append(
            {"role": "user", "content": message},
        )
completion = client.completions.create(model='gpt-3.5-turbo',prompt=messages)

reply = completion.choices[0].message.content
print(f"ChatGPT: {reply}")
f.close()

