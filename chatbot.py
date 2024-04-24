from key_api import API_KEY  # type: ignore
import openai, json

# Substitua 'YOUR_API_KEY' pela sua chave de API real
openai.api_key = API_KEY

# Função para gerar texto a partir do modelo de linguagem
def gerar_texto(texto: str):
    # Obtem a resposta do modelo de linguagem
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # Substitua pelo modelo desejado
        messages=[
            {"role": "system", "content": "Você é um assistente de chat inteligente."},
            {"role": "user", "content": texto},
        ],
        max_tokens=150,
        n=1,
        log_level="info",
    )
    return response.choices[0].message['content'].strip()

def main():
    print("\nBem-vindo ao Gpt-3 Chatbot do Projeto 3 do Curso Gratuito da Data Science Academy!")
    print("https://jeffersonmoraesjunior.com.br")
    print("(Digite 'sair' a qualquer momento para encerrar o chat)")

    # Loop
    while True:
        user_message = input("\nVocê: ")
        if user_message.lower() == "sair":
            break
        gpt_prompt = f"\nUsuário: {user_message}\nChatbot:"
        chatbot_response = gerar_texto(gpt_prompt)
        print(f"\nChatbot: {chatbot_response}")

# Execução do programa (bloco main) em Python
if __name__ == "__main__":
    main()



