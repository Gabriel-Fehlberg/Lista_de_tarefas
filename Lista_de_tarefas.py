tarefas = []
while True:
    print('\n--- Menu ---')
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Remover tarefa')
    print('4 - Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        tarefa = input('Digite a tarefa: ')
        tarefas.append(tarefa)
        print('Tarefa adicionada com sucesso!')

    elif opcao == 2:
        if len(tarefas) == 0:
            print('\nNenhuma tarefa cadastrada\n')
        else:
            print('\nLista de tarefas: ')
        for i, tarefa in enumerate (tarefas, start=1):
            print(f'{i}. {tarefa}')

    elif opcao == 3:
        if len(tarefas) ==0:
            print('\nNenhuma tarefa para remobver.\n')
        else:
            print('\nTarefas: ')
        for i, tarefa in enumerate (tarefas, start=1):
            print(f'{i}. {tarefa}')

        num = int(input('Digite o número da tarefa para remover: '))
        if 1 <= num <= len(tarefas):
            removida = tarefas.pop(num - 1)
            print(f"Tarefa '{removida}' removida com sucesso. ")
        else: print('Número inválido.')

    elif opcao == 4:
        print('Saindo do programa...')
        break

    else:
        print('Opção invalida, tente novamente: ')
