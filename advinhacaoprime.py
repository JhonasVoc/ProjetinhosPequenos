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


def selecao_dificuldade():
    print("Vamos Definir a dificuldade do game:")
    print("1 - Facil (intervalo de advinhação 0-25/5 dicas)")
    print("2 - Médio (intervalo de advinhação 0-50/4 dicas)")    
    print("3 - Dicifil(intervalo de advinhação 0-75/3 dicas)")  
    print("4 - Mega HardCore rock and rollDicifil(intervalo de advinhação 0-125/2 dicas)")           
    while True:                                
        escolha = int(input("Escolha a dificuldade desejada(1-4): "))
        if escolha == 1:
            min = 0
            max = 25
            dicas = 5
            return min,max,dicas
            # essa parte é igual, vamos colocar em funcao
            #rand_num = gerar_numero(min,max)
            #escolha = receber_chute(min,max)
        elif escolha == 2:
            min = 0
            max = 50
            dicas = 4
            return min,max,dicas
        elif escolha == 3:
            min = 0
            max = 75
            dicas = 3
            return min,max,dicas
        elif escolha == 4:
            min = 0
            max = 125
            dicas = 2
            return min,max,dicas
        else:
            print("Escolha incorreta, digite novamente")
        

def conferir_jogo(num,chute,dicas):
    count = 0
    tentativas = 0
    while num != chute:
        if count <= dicas:
            print(f"Aqui vai sua dica n'{count +1}")
            print(f"xxxxx dica")
            count += 1
            tentativas +=1
            chute = int(input("Digite seu chute novamente: "))
        else:
            print("Você acertou!!!!")
            print(f"Tentativas usadas:{tentativas}")
            print(f"Dicas usadas{count}")
            break



def gerar_dicas(num,chute):
        if abs(num,chute) <= 10:
            print("A diferença entre chute e o numero é menor ou igual a 10")
        else:
            print("A diferença entre chute e o numero é maior ou que 10")

        if num % 2 == 0:
            print("O numero é par")
        else:
            print("O numero é impar")

        if num % 10 == 0:
            print("O número é divisivel por 10")
        else:
            print("O número não é divisivel por 10")

        if num < 10:
            print("O número é menor que 10")
        else:
            print("O número é menor que 10")

        if chute<num:
            print("O chute é menor que o numero")
        else:
            print("O chute é maior que o numero")
            
    

gerar_dicas(2,3)



#min,max, dicas =selecao_dificuldade()
#print(f"{min}. {max}. {dicas}. ")


