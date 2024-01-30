from openai import OpenAI
from _api_key import API_KEY
import speech_recognition as sr
import pyttsx3

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

def user_speech_recognition():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Escutando...\n")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

    try:
      texto = recognizer.recognize_google(audio, language="pt-BR")
      return texto
    except sr.UnknownValueError:
      if countNotTalk == 0:
        print(f"\033[4mChatbot\033[0m: Não entendi o que falou, por favor fale novamente!\n")
    except sr.RequestError as error:
      print("Erro ao solicitar resultados: {0}\n".format(error))

def talk(text):
  engine = pyttsx3.init()
  engine.setProperty("rate", 230)
  engine.setProperty("volume", 1)
  engine.say(text)
  engine.runAndWait()

print("\nBem-vindo(a) à Assistente Virtual do Reprograma Jucás!\n")
print("Sobre o que deseja falar?\n")

talk("Bem-vindo(a) à Assistente Virtual do Reprograma Jucás!")
talk("Sobre o que deseja falar?")

array_messages = []
countNotTalk = 0
while True:
  message = user_speech_recognition()

  if message:
    countNotTalk = 0
    print(f"\033[4mYou\033[0m: {message.capitalize()}\n")
    array_messages.append({"role": "user", "content": message})
    
    if message == "sair" or message == "parar" or message == "encerrar" or message == "obrigado":
      break
    else:
      response = send_message(array_messages)
      array_messages.append({"role": "assistant", "content": response})
      print(f"\033[4mChatbot\033[0m: {response}\n") 
      talk(response)
  else:
    if countNotTalk >= 1: 
      break
    
    talk("Não entendi o que falou, por favor fale novamente!")
    countNotTalk += 1

print("\033[4mChatbot\033[0m: Obrigado, volte sempre!\n")
talk("Obrigado, volte sempre!")
