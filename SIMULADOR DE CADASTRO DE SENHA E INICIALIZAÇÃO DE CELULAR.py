def verificar_senha(senha_correta, tentativas):
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        print("Bem-vindo.")
        return True
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta. Tentativas restantes: {tentativas}")
            return verificar_senha(senha_correta, tentativas)
        else:
            print("Telefone bloqueado.")
            return False

def main():
    senha_correta = "senha123"
    tentativas_restantes = 3
    if not verificar_senha(senha_correta, tentativas_restantes):
        return

    # Restante do código após desbloquear o telefone...

if __name__ == "__main__":
    main()
