from key_api import API_KEY  # type: ignore
import requests
import openai
import json

headers = {"Authorization": f"Bearer {API_KEY}",
           "Content-Type": "application/json"
        }

link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

body_message = {
    "model": id_modelo,
    "message": [{
        "role": "user",
        "content": "fale sobre a previsão do bitcoin daqui a 2 meses"
    }]
}

body_message = json.dumps(body_message)

requisicao = requests.post(link, headers=headers, data=body_message)

# print(requisicao)
# print(requisicao.text)

resposta = requisicao.json()
mensagem = resposta["choices"][0]["message"]["content"]
print(mensagem)


