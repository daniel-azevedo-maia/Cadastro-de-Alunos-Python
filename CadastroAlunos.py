from time import sleep

print('\n ----------- CADASTRO DE ALUNOS ----------- ')

prosseguirCadastroTurma = 's'
turmaA = []
turmaB = []
turmaC = []

while prosseguirCadastroTurma == 's':
    print("""
Selecione a turma em que deseja cadastrar alunos:
[ A ] Turma A
[ B ] Turma B
[ C ] Turma C
    """)
    opcaoTurma = str(input('Opção: ')).upper().strip()
    prosseguirCadastro = 's'

    if opcaoTurma == 'A':
        while prosseguirCadastro == 's':
            nome = str(input('Nome do aluno: '))
            turmaA.append(nome)
            prosseguirCadastro = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        print('Cadastrando alunos...')
        sleep(2)
    elif opcaoTurma == 'B':
        while prosseguirCadastro == 's':
            nome = str(input('Nome do aluno: '))
            turmaB.append(nome)
            prosseguirCadastro = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        print('Cadastrando alunos...')
        sleep(2)
    else:
        while prosseguirCadastro == 's':
            nome = str(input('Nome do aluno: '))
            turmaC.append(nome)
            prosseguirCadastro = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        print('Cadastrando alunos...')
        sleep(2)

    prosseguirCadastroTurma = str(input('Deseja cadastrar alunos em outra turma? [S/N]: ')).lower().strip()

desejaVoltar = 's'
while desejaVoltar == 's':
    print("""
    Qual operação deseja realizar?:
    
    [ 1 ] Exibir lista de alunos
    [ 2 ] Exibir lista de alunos em ordem inversa
    [ 3 ] Juntar alunos de duas turmas
    [ 4 ] Ordenar alunos por ordem alfabética
    [ 5 ] Exibir a quantidade de alunos
    [ 6 ] Remover aluno (s)
    """)
    opcaoOperacoes = int(input('Opção: '))

    # OPERAÇÃO 1:
    if opcaoOperacoes == 1:
        print("""
    Selecione a turma em que deseja exibir os alunos:
    [ A ] Turma A
    [ B ] Turma B
    [ C ] Turma C
    [ D ] Exibir listas de todas as turmas 
            """)
        opcaoTurma = str(input('Opção: ')).upper().strip()
        if opcaoTurma == 'A':
            print('Buscando alunos para exibir...')
            sleep(2)
            print("LISTA DE ALUNOS DA TURMA A: ")
            for i, v in enumerate(turmaA):
                print(f'{i + 1} - {v}.')

        elif opcaoTurma == 'B':
            print('Buscando alunos para exibir...')
            sleep(2)
            print("LISTA DE ALUNOS DA TURMA B: ")
            for i, v in enumerate(turmaB):
                print(f'{i + 1} - {v}.')

        elif opcaoTurma == 'C':
            print('Buscando alunos para exibir...')
            sleep(2)
            print("LISTA DE ALUNOS DA TURMA C ")
            for i, v in enumerate(turmaC):
                print(f'{i + 1} - {v}.')

        else:
            print('Buscando alunos para exibir...')
            sleep(2)
            print("LISTA DE ALUNOS DA TURMA A: \n")
            for i, v in enumerate(turmaA):
                print(f'{i + 1} - {v}.')

            print("LISTA DE ALUNOS DA TURMA B: \n")
            for i, v in enumerate(turmaB):
                print(f'{i + 1} - {v}.')

            print("LISTA DE ALUNOS DA TURMA C: \n")
            for i, v in enumerate(turmaC):
                print(f'{i + 1} - {v}.')

        desejaVoltar = str(input('Deseja voltar? [S/N]: ')).lower().strip()

    # OPERAÇÃO 2:
    elif opcaoOperacoes == 2:
        print("""
    Selecione a turma em que deseja exibir os alunos:
    [ A ] Turma A
    [ B ] Turma B
    [ C ] Turma C
    [ D ] Exibir listas de todas as turmas 
                """)
        opcaoTurma = str(input('Opção: ')).upper().strip()
        if opcaoTurma == 'A':
            print('Buscando alunos para exibir...')
            sleep(2)
            print("LISTA DE ALUNOS DA TURMA A: ")
            turmaA.reverse()
            for i, v in enumerate(turmaA):
                print(f'{i + 1} - {v}.')
        elif opcaoTurma == 'B':
            print('Buscando alunos para exibir...')
            sleep(2)
            print("LISTA DE ALUNOS DA TURMA B: ")
            turmaB.reverse()
            for i, v in enumerate(turmaB):
                print(f'{i + 1} - {v}.')
        elif opcaoTurma == 'C':
            print('Buscando alunos para exibir...')
            sleep(2)
            print("LISTA DE ALUNOS DA TURMA C ")
            turmaC.reverse()
            for i, v in enumerate(turmaC):
                print(f'{i + 1} - {v}.')
        else:
            print('Buscando alunos para exibir...')
            sleep(2)
            print("LISTA DE ALUNOS DA TURMA A: \n")
            for i, v in enumerate(turmaA):
                print(f'{i + 1} - {v}.')
            print("LISTA DE ALUNOS DA TURMA B: \n")
            for i, v in enumerate(turmaB):
                print(f'{i + 1} - {v}.')
            print("LISTA DE ALUNOS DA TURMA C: \n")
            for i, v in enumerate(turmaC):
                print(f'{i + 1} - {v}.')

# OPERAÇÃO 3:
    elif opcaoOperacoes == 3:
        print("""
            Selecione a primeira turma:
            [ A ] Turma A
            [ B ] Turma B
            [ C ] Turma C
            [ D ] Exibir listas de todas as turmas 
                        """)
        opcaoTurma1 = str(input('Turma 1: ')).upper().strip()

        if opcaoTurma1 == 'A':
            opcaoTurma1 = turmaA.copy()
        elif opcaoTurma1 == 'B':
            opcaoTurma1 = turmaB.copy()
        else:
            opcaoTurma1 = turmaC.copy()

        opcaoTurma2 = str(input('Turma 2: ')).upper().strip()

        if opcaoTurma2 == 'A':
            opcaoTurma2 = turmaA.copy()
        elif opcaoTurma2 == 'B':
            opcaoTurma2 = turmaB.copy()
        else:
            opcaoTurma2 = turmaC.copy()
        turmaUnida = opcaoTurma1 + opcaoTurma2

        print("LISTA DE ALUNOS DAS TURMAS UNIDAS: \n")
        for i, v in enumerate(turmaUnida):
            print(f'{i + 1} - {v}.')

    # OPERAÇÃO 4:
    elif opcaoOperacoes == 4:
        print('oi')

    # OPERAÇÃO 5:
    elif opcaoOperacoes == 5:
        print('oi')

    # OPERAÇÃO 6:
    else:
        print('oi')