def soma(*args):
    soma = 0
    for i in args:
        soma += i

    return soma

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    while True:
        if b == 0:
            print("Erro: Divisão por zero não é permitida.")
            b = float(input("Digite um divisor diferente de zero: "))
        else:
            return a / b
def potencia(a,b):
    return a ** b

def main():
    print("Calculadora")
    print("1 - Soma")
    print("2 - Subtração")    
    print("3 - Multiplicação")  
    print("4 - Divisão")
    print("5 - Potência")                                            
    escolha = input("Escolha a operação desejada: ")     
    if escolha == '1':
        nums = input("Digite os números a serem somados, separados por espaço: ")
        num_list = list(map(int, nums.split()))
        resultado = soma(*num_list)
        print(f"O resultado da soma é: {resultado}")
    elif escolha == '2':                                                    
        a = float(input("Digite o minuendo: "))
        b = float(input("Digite o subtraendo: "))
        resultado = subtracao(a, b)
        print(f"O resultado da subtração é: {resultado}")
    elif escolha == '3':
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = multiplicacao(a, b)
        print(f"O resultado da multiplicação é: {resultado}")
    elif escolha == '4':
        a = float(input("Digite o dividendo: "))
        b = float(input("Digite o divisor: "))
        resultado = divisao(a, b)
        print(f"O resultado da divisão é: {resultado}")
    elif escolha == '5':
        a = float(input("Digite a base: "))
        b = float(input("Digite o expoente: "))
        resultado = potencia(a, b)
        print(f"O resultado da potência é: {resultado}")
    else:
        print("Operação inválida.")

main()