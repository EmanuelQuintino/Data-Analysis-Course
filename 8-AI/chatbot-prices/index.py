import speech_recognition as sr
import pyttsx3
from products_data import products  

def user_speech_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...\n")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="pt-BR").lower()
            return text
        except sr.UnknownValueError:
            print(f"\033[4mChatbot\033[0m: Não entendi o que falou, por favor fale novamente!\n")
        except sr.RequestError as error:
            print(f"Erro ao solicitar resultados: {error}")

def talk(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 200)
    engine.setProperty("volume", 1)
    engine.say(text)
    engine.runAndWait()

def search_response(message):
    if any(greeting in message for greeting in ["olá", "oi", "bom dia", "boa tarde", "boa noite"]):
        return "Olá, tudo bem? Por favor, fale o nome do produto para saber preço ou descrição."

    if any(keyword in message for keyword in ["preço", "custo", "custa"]):
        for product in products:
            if any(tag in message for tag in product['tags']):
                return f"O preço d{product['genero']} {product['name']} é {product['preço']} reais."

    if any(keyword in message for keyword in ["descrição", "mais sobre", "me conte", "me conte sobre", "saber mais", "fale sobre"]):
        for product in products:
            if any(tag in message for tag in product['tags']):
                return f"{product['descricao']}."
            
    if any(keyword in message for keyword in ["chamar vendedor", "falar com vendedor", "quero falar com vendedor", "vendedor", "ajuda", "chame", "chamar", "falar", "falo", "ajude", "ajudante", "atendente"]):
        return "Chamando um de nossos vendedores para te atender..."

    return "Posso te ajudar com preço e descrição. Se quiser saber mais irei chamar um de nossos vendedores para melhor te atender."


while True:
    user_message = user_speech_recognition()

    if user_message:
        print(f"Cliente: {user_message.capitalize()}")  

        if any(keyword in user_message for keyword in ["sair", "parar", "encerrar", "obrigado"]):
            print("Zê: Obrigado, volte sempre!")
            talk("Obrigado, volte sempre!")
            break

        bot_response = search_response(user_message)
        print(f"Zê: {bot_response}")  
        talk(bot_response)
    else:
        print("Zê: Não entendi o que falou, por favor fale novamente!")
