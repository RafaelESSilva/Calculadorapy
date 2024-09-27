'''Calculadora Python'''
comecar = True
try:
    while comecar:
        continuar = input('Deseja continuar? ')
        if continuar == 'nao':
            comecar = False
        else:
            comecar = True
        operacao = input('Informe a operação que ocê deseja operar: soma, subitracao, divizao,multiplicacao.')
        primeiro_numero = input('Informe o primeiro valor a operaçã: ')
        int_primeiro_numero = int(primeiro_numero)
        segundo_numero = input('Informe o segundo numero da operação: ')
        int_segundo_numero = int(segundo_numero)
        if operacao == 'soma':
            print(f'{primeiro_numero} + {segundo_numero} =',int_primeiro_numero + int_segundo_numero)
        elif operacao == 'subtracao':
            print(f'{primeiro_numero} - {segundo_numero} =',int_primeiro_numero - int_segundo_numero)
        elif operacao == 'multiplicacao':
            print(f'{primeiro_numero} * {segundo_numero} =',int_primeiro_numero * int_segundo_numero)
        elif operacao == 'divisao':
            print(f'{primeiro_numero} / {segundo_numero} =',int_primeiro_numero / int_segundo_numero)
        else:
            print('Informação incorreta tente de novo.')
except:
     print('')