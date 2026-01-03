<div align="center">

# 🔍 Web Directory Fuzzer

**A Python tool for web path discovery / Ferramenta Python para descoberta de diretórios web**

[🇺🇸 English](#-english) | [🇧🇷 Português](#-português)

</div>

---

## 🇺🇸 English

### 📋 About the Project
**Web Directory Fuzzer** is a lightweight Python script designed for **web reconnaissance**. It uses a wordlist to brute-force directories and files on a web server, helping penetration testers identify hidden paths, admin panels, or backup files.

This tool was developed as part of my Cybersecurity studies, based on concepts from **SOLYD Offensive Security**, with additional features and refactoring implemented by me.

### 🚀 Key Features
* **User-Agent Spoofing:** Simulates a real browser (Windows 10) to bypass basic WAFs and bot filters.
* **Error Handling:** Gracefully handles `CTRL+C` interruptions and connection timeouts without crashing.
* **SSL Verification Bypass:** Automatically ignores insecure certificate warnings (useful for local labs/CTFs).
* **Clean Output:** Filters out 404 errors, showing only relevant results.

### 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mariaesmdev/web-directory-fuzzer.git
    cd web-directory-fuzzer
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests
    ```

3.  **Run the script:**
    ```bash
    python web_fuzzer.py
    ```

4.  **Input:**
    * **URL:** Target website (e.g., `http://example.com`).
    * **Wordlist:** Path to your text file containing the words to test.

### ⚠️ Disclaimer
This tool is intended for **educational purposes** and **authorized security testing** only. The author is not responsible for any misuse or damage caused by this program.

---

## 🇧🇷 Português

### 📋 Sobre o Projeto
**Web Directory Fuzzer** é um script leve em Python desenvolvido para **reconhecimento web**. Ele utiliza uma wordlist para fazer força bruta (brute-force) em diretórios e arquivos de um servidor, ajudando a identificar caminhos ocultos, painéis administrativos ou arquivos de backup.

Esta ferramenta foi desenvolvida como parte dos meus estudos em Segurança da Informação, baseada nos conceitos da **SOLYD Offensive Security**, com melhorias e refatorações implementadas por mim.

### 🚀 Funcionalidades
* **User-Agent Spoofing:** Simula um navegador real (Windows 10) para evitar bloqueios simples de filtros e WAFs.
* **Tratamento de Erros:** Lida com interrupções (`CTRL+C`) e timeouts de conexão sem travar o script.
* **Bypass de SSL:** Ignora avisos de certificados inseguros (útil para laboratórios locais e CTFs).
* **Saída Limpa:** Filtra erros 404, exibindo apenas o que foi encontrado.

### 🛠️ Instalação e Uso

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/mariaesmdev/web-directory-fuzzer.git
    cd web-directory-fuzzer
    ```

2.  **Instale as dependências:**
    ```bash
    pip install requests
    ```

3.  **Execute o script:**
    ```bash
    python web_fuzzer.py
    ```

4.  **Entrada de dados:**
    * **URL:** Site alvo (ex: `http://exemplo.com`).
    * **Wordlist:** Caminho para o seu arquivo de texto com as palavras.

### ⚠️ Aviso Legal
Esta ferramenta foi desenvolvida apenas para **fins educacionais** e **testes de segurança autorizados**. O autor não se responsabiliza pelo mau uso ou danos causados por este programa.

---

<div align="center">
    Made with 💻 and ☕ by <b>Maria Eduarda Machado</b>
</div>
