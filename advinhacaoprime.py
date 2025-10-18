import random


def gerar_numero():
    num = random.randint(min,max)
    return num



def receber_chute(min,max):
    while True:
        try:   
            chute = int(input("Digite seu chute (entre 0 e 100): "))
            if chute < min or chute >max:
                print(f"Por favor, digite um número entre {min} e {max}.")
            else:
                return chute
        except ValueError:
            continue

