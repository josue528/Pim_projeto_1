import json
import hashlib

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    senha_criptografada = criptografar_senha(senha)
    
    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha_criptografada
    }
    
    try:
        with open('usuarios.json', 'r') as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError:
        usuarios = []
    
    usuarios.append(usuario)
    
    with open('usuarios.json', 'w') as arquivo:
        json.dump(usuarios, arquivo, indent=4)
    
    print("Usuário cadastrado com sucesso!")


if __name__ == "__main__":
    cadastrar_usuario()
