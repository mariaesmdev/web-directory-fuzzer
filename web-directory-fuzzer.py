import requests
import urllib3
import sys

# Limpa os avisos de certificado https não verificado
# Disables insecure HTTPS certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def brute(url, wordlist):
    
    # Isso engana o servidor para ele achar que somos um navegador comum e não um script
    # Tricks the server into thinking this is a standard browser, not a script
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for word in wordlist:
        word = word.strip()
        
        # Pula linhas vazias na wordlist para evitar erros
        # Skips blank lines to avoid malformed URLs
        if not word:
            continue

        if url.endswith("/"):
            target_url = f"{url}{word}"
        else:
            target_url = f"{url}/{word}"
            
        try:

            response = requests.get(target_url, headers=headers, verify=False, timeout=5)
            code = response.status_code
            
            if code != 404:
                print(f"[+] Encontrado: {target_url} (Status Code: {code})")
                
        except KeyboardInterrupt:
            print("\n ----- O usuário interrompeu o processo ------")
            sys.exit()
        except Exception as e:
            # Se der erro de conexão (timeout), apenas ignora e tenta o próximo
            # Ignores connection errors (timeout) and tries the next word
            pass

if __name__ == "__main__":
    target_url = input("Digite a URL (ex: http://meusite.com): ")
    wordlist_name = input("Digite o nome da wordlist (ex: wordlist.txt): ")

    try:
        with open(wordlist_name, "r") as file:
            words = file.readlines()
            print(f"\n[*] Iniciando ataque em: {target_url}")
            print(f"[*] Usando wordlist: {wordlist_name}\n")
            brute(target_url, words)
            
    except FileNotFoundError:
        print(f"\n[!] ERRO: O arquivo '{wordlist_name}' não foi encontrado.")
    except Exception as e:

        print(f"\n[!] Ocorreu um erro inesperado: {e}")
