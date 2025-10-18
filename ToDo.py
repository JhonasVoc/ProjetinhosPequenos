import json
import os

with open("data.json", "r") as file:
    todo_dict = json.load(file)



def printar_todo():
    for tarefa, concluido in todo_dict.items():
        status = "|✔|" if concluido else "|x|"
        print(f"{status} {tarefa}")


def adicionar_tarefa(tarefa):
    todo_dict[tarefa] = False
    print(f'Tarefa "{tarefa}" adicionada.')

def remover_tarefa(tarefa):
    if tarefa in todo_dict:
        del todo_dict[tarefa]
        print(f'Tarefa "{tarefa}" removida.')
    else:
        print(f'Tarefa "{tarefa}" não encontrada.')


def main():
    while True:
        print("\nMenu de Tarefas:")
        print("1 - Ver Tarefas")
        print("2 - Adicionar Tarefa")
        print("3 - Remover Tarefa")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            printar_todo()
        elif escolha == '2':
            tarefa = input("Digite a nova tarefa: ")
            adicionar_tarefa(tarefa)
        elif escolha == '3':
            tarefa = input("Digite a tarefa a ser removida: ")
            remover_tarefa(tarefa)
        elif escolha == '4':
            print("Saindo do programa.")
            with open("data.json", "w") as file:
                json.dump(todo_dict, file,indent=4)
            break
        else:
            print("Opção inválida. Tente novamente.")


main()