from openai import OpenAI
from api_key import API_KEY

def send_message(message, array_messages=[]):
  client = OpenAI(api_key=API_KEY)
  
  array_messages.append({"role": "user", "content": message})

  stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=array_messages,
    stream=True,
    # temperature=0.8,
    # max_tokens=100,
    # stop=None,
  )
  
  return stream["choices"][0]["message"]

array_messages = []
while True:
  message = input("You: ")
  if message.lower() == "sair":
    print("Chatbot: Obrigado, volte sempre!")
    break

  response = send_message(message, array_messages)
  array_messages.append(response)
  print(f"Chatbot: {response}")