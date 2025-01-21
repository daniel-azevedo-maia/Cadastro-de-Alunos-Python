from time import sleep

# Inicialização
turmas = {"A": [], "B": [], "C": []}

def cadastrar_alunos(turma):
    while True:
        nome = input("Nome do aluno: ").strip()
        if nome in turmas[turma]:
            print(f"O aluno '{nome}' já está cadastrado na turma {turma}.")
        else:
            turmas[turma].append(nome)
        continuar = input("Deseja cadastrar outro aluno? [S/N]: ").lower().strip()
        if continuar != 's':
            break

def exibir_alunos(turma, inverso=False):
    print(f"\nLista de alunos da turma {turma}:")
    alunos = turmas[turma][::-1] if inverso else turmas[turma]
    for i, nome in enumerate(alunos, start=1):
        print(f"{i}. {nome}")

def juntar_turmas(turma1, turma2):
    alunos_unidos = turmas[turma1] + turmas[turma2]
    print("\nLista de alunos das turmas unidas:")
    for i, nome in enumerate(alunos_unidos, start=1):
        print(f"{i}. {nome}")

def remover_aluno(turma):
    nome = input("Informe o nome do aluno para remover: ").strip()
    if nome in turmas[turma]:
        turmas[turma].remove(nome)
        print(f"Aluno '{nome}' removido com sucesso.")
    else:
        print(f"Aluno '{nome}' não encontrado na turma {turma}.")

# Menu principal
while True:
    print("\n----------- MENU -----------")
    print("[1] Cadastrar Alunos")
    print("[2] Exibir Lista de Alunos")
    print("[3] Exibir Lista Invertida")
    print("[4] Juntar Duas Turmas")
    print("[5] Remover Aluno")
    print("[6] Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        turma = input("Informe a turma [A/B/C]: ").upper().strip()
        if turma in turmas:
            cadastrar_alunos(turma)
        else:
            print("Turma inválida.")

    elif opcao == "2":
        turma = input("Informe a turma [A/B/C]: ").upper().strip()
        if turma in turmas:
            exibir_alunos(turma)
        else:
            print("Turma inválida.")

    elif opcao == "3":
        turma = input("Informe a turma [A/B/C]: ").upper().strip()
        if turma in turmas:
            exibir_alunos(turma, inverso=True)
        else:
            print("Turma inválida.")

    elif opcao == "4":
        turma1 = input("Informe a primeira turma [A/B/C]: ").upper().strip()
        turma2 = input("Informe a segunda turma [A/B/C]: ").upper().strip()
        if turma1 in turmas and turma2 in turmas:
            juntar_turmas(turma1, turma2)
        else:
            print("Turma inválida.")

    elif opcao == "5":
        turma = input("Informe a turma [A/B/C]: ").upper().strip()
        if turma in turmas:
            remover_aluno(turma)
        else:
            print("Turma inválida.")

    elif opcao == "6":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
