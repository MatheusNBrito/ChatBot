import openai

openai.api_key = "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"

def gera_texto(texto):

    response = openai.Completion.create(

        model = "gpt-3.5-turbo",

        prompt = texto,

        max_tokens = 150, 

        n = 5,

        stop = None,

        temperature = 0.8,
    )
    return response.choices[0].text.strip()

def main():

    print("\nSeja bem vindo ao Chatbot do Brito!")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")

    while True:

        user_message = input("\nVocê:")

        if user_message.lower() == "sair":
            break

        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"

        chatbot_response = gera_texto(gpt4_prompt)

        print(f"\nChatbot: {chatbot_response}")

if __name__ == "__main__":
    main()