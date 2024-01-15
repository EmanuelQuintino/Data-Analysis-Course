from openai import OpenAI
from api_key import API_KEY

client = OpenAI(api_key=API_KEY)

def send_message(message, array_messages=[]):  
  array_messages.append({"role": "user", "content": message})

  stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=array_messages,
    stream=True,
  )
  
  response = ""
  for chunk in stream:
    if chunk.choices[0].delta.content is not None:
      response += chunk.choices[0].delta.content
  
  return response
  
print("\nBem-vindo ao Chat do Reprograma Jucás!")
print("\nDigite 'sair' para encerrar o chat")

array_messages = []
while True:
  message = input("\nYou: ")
  if message.lower() == "sair":
    print("\nChatbot: Obrigado, volte sempre que desejar!")
    break

  response = send_message(message)
  array_messages.append({"role": "assistant", "content": response})
  print(f"\nChatbot: {response}")