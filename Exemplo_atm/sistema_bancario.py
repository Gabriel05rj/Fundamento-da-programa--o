saldo = 1000.00
historico = [] #está é uma lista de dados, podendo colocar elementos nela, neste caso está vazia mas pode receber elementos

print(f' 🏧 ----Bem Vindo ao Caixa Eletrônico----')

while True: # imprime o while ao menos uma vez
    print(f''' ---Menu Principal---       
        [1] - Depositar
        [2] - Sacar
        [3] - Ver Saldo
        [4] - Ver Histórico
        [5] - Sair
          ''')  #3 ''' é a f docstring oque permite criar uma estrutura em diferentes linhas
    opcao = input('➡️ Escolha uma Opção: ')

    #Lógica para opção de depósito
    if opcao == '1':
        valor_deposito = float(input(' ➡️ Digite o valor para Depósito: R$'))
        if valor_deposito > 0:
            # saldo = saldo + valor_deposito
            saldo += valor_deposito
            registro = f'Depósito: +R$ {valor_deposito: .2f}'#.nf indica as n casas decimais que o sist. deve ler
            historico.append(registro) #append() adiciona algo a lista
            print('🆗 Depósito Realizado com Sucesso.')
        else:
            print('❌ Valor inválido. O depósito deve ser um valor positivo.')

    elif opcao == '2':
        valor_saque = float(input(' ➡️ Digite o valor para Saque: R$'))
        if valor_saque <= 0:
            print('❌ Valor inválido! O saque deve ser uma número positivo.')
        elif valor_saque > saldo:
            print('❌ Valor inválido! O saque deve ser menor que o saldo.')
        else:
            # saldo = saldo - valor_saque (ambos os métodos são válidos)
            saldo -= valor_saque
            registro = f'Saque: R${valor_saque: .2f}' #registro é uma variavel para pode colocar dados no historico
            historico.append(registro)
            print('Saque realizado com sucesso! Retire seu dinheiro.')
    elif opcao == '3':
        print(f' 💰 O valor do seu Saldo é: R$ {saldo}:.2f')
    elif opcao == '4':
        print(f' 📃 Histórico de transações: {historico}:.2f')
        if not historico: #verifica se historico esta vazio pois toda variável/estrutura vazia é True
            print('❌ Nenhuma transação foi realizada ainda.')
        else:
            for transacao in historico:
                print(transacao) #transacao é uma variável curinga
    elif opcao == '5':
        print('Obrigado por utilizar nosso caixa eletrônico. Finalizando... desapareça...')
        break # Encerra o laço while
    else:
        print(' ❌ Ser pensante, está opção é inválida selecione uma opção válida.')