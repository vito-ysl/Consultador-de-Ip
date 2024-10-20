import requests

def consultar_ip():
    try:
        # URL do serviço que retorna o IP
        response = requests.get('https://api.ipify.org?format=json')
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Extrai o IP do JSON retornado
            ip_info = response.json()
            ip = ip_info['ip']
            print(f"Seu IP público é: {ip}")
        else:
            print("Erro ao consultar o IP.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    consultar_ip()
