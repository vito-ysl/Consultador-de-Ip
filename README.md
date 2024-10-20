# Consultador de IP

Um simples projeto em Python que consulta e exibe o seu endereço IP público utilizando a API do [ipify](https://www.ipify.org/).

## Como usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/vito-ysl/Consultador-de-Ip.git
   
2. Execute o script:

   ```bash
   git clone https://github.com/vito-ysl/Consultador-de-Ip.git

## Código

   ```bash
  import requests

def consultar_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            ip_info = response.json()
            print(f"Seu IP público é: {ip_info['ip']}")
        else:
            print("Erro ao consultar o IP.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    consultar_ip()

```
## Contribuições
Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para criar um pull request.


