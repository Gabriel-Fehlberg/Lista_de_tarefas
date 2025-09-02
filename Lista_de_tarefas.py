lista_tarefas = []
while True:
    print('\n--- Menu ---')
    print('1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Remover tarefa')
    print('4 - Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        tarefa = input('Digite a tarefa: ')
        lista_tarefas.append(tarefa)
        print('Tarefa adicionada com sucesso!')

    elif opcao == 2:
        if len(lista_tarefas) == 0:
            print('\nNenhuma tarefa cadastrada\n')
        else:
            print('\nLista de tarefas: ')
            for x in range(len (lista_tarefas)):
                print(f'{x + 1} {lista_tarefas[x]}')
                

    elif opcao == 3:
        if len(lista_tarefas) ==0:
            print('\nNenhuma tarefa para remobver.\n')
        else:
            print('\nTarefas: ')
            for x in range(len (lista_tarefas)):
                print(f'{x + 1} {lista_tarefas[x]}')

        num = int(input('Digite o número da tarefa para remover: '))
        if 1 <= num <= len(lista_tarefas):
            removida = lista_tarefas.pop(num - 1)
            print(f"Tarefa '{removida}' removida com sucesso. ")
        else: print('Número inválido.')

    elif opcao == 4:
        print('Saindo do programa...')
        break

    else:
        print('Opção invalida, tente novamente: ')
