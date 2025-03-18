def mensagem_personalizada(nome):
    mensagem = f"Olá, {nome}! Bem-vindo ao mundo da programação em Python!"
    return mensagem

# Solicita o nome do usuário
nome_usuario = input("Digite seu nome: ")

# Exibe a mensagem personalizada
print(mensagem_personalizada(nome_usuario))