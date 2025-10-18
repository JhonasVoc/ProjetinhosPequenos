# Aqui eu gostaria que o nome não fosse vazio, nem menor que 4 caracteres
def receber_nome():
     while True:
        nome = str(input("Por favor, insira seu nome: "))
        if nome.strip() != "":
            if len(nome) > 3:
                return nome
            else:
                print("O nome deve ter pelo menos 4 caracteres. Tente novamente.")
        else:
            print("O nome não pode ser vazio. Tente novamente.")


def receber_idade_usuario():
    idade = int(input("Por favor, insira sua idade: "))
    if idade < 1 or idade > 120:
        print("Idade invalida. Tente novamente.")
        return receber_idade_usuario()
    else:
        return idade    

def receber_saldo():
    while True:
            saldo = float(input("Por favor, insira seu saldo em R$:"))
            if saldo < 0:
                print("Saldo não pode ser negativo. Tente novamente.")
            else:
                return saldo


def main():
     nome = receber_nome()
     idade = receber_idade_usuario()
     saldo = receber_saldo()
     print(f"Usuário cadastrado com sucesso!\nNome: {nome}\nIdade: {idade}\nSaldo: R${saldo:.2f}")

main()
