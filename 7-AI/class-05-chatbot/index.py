from openai import OpenAI
from _api_key import API_KEY

def send_message(array_messages=[]):  
  client = OpenAI(api_key=API_KEY)
  
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
print('\nDigite "sair" para encerrar o chat')

array_messages = []
while True:
  message = input("\033[4m\nYou\033[0m: ")
  array_messages.append({"role": "user", "content": message})

  if message.lower() == "sair":
    print("\033[4m\nChatbot\033[0m: Obrigado, volte sempre que desejar!\n")
    break

  response = send_message(array_messages)
  array_messages.append({"role": "assistant", "content": response})
  print(f"\nChatbot: {response}")
