#Faça um jogo para o usuário adivinhar qual a palavra secreta.
#Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
#Quando o usuário digitar uma letra, voce vai conferir se a letra digitada está na palavra.
#Se a letra estiver na palavra, exiba a letra.
#Se a letra não estiver, exiba *
#Faça a contagem de tentativas do seu usuário.
import random
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- DEFINIÇÃO DE VARIÁVEIS/ELEMENTOS
biblioteca = ['amar','computador','foto','televisao','casa','carro','porta','arvore'] #biblioteca de palavras que compõem o jogo
mostrador = [] #cria uma lista para atualizar as letras que vão sendo acertadas
cont_ponto=cont_palpite = 0 
op='S'
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- CORPO DO PROGRAMA
while True:
    palavra=random.choice(biblioteca) #escolhe a palavra dentro da lista de biblioteca

    for i in range (0,len(palavra)): #preenche a lista do mostrador com a quantidade de letras da palavra escolhida
        mostrador.append('_')
    print(mostrador)
    print(f'A palavra tem {len(palavra)} letras.')

    while True: 
        palpite=str(input('Digite uma letra: ')).lower()
        if len(palpite) != 1: #verifica se o usuário digitou apenas uma letra
            print('Você digitou mais de uma letra!')
        else: #Se ele digitou apenas uma letra, verifica se ela está correta
            cont_palpite += 1 #conta a quantidade de jogadas do usuário
            for i in range(0,len(palavra)): #percorre a palavra escolhida em busca pela letra igual,
                if palavra[i] == palpite:
                    cont_ponto += 1
                    mostrador[i] = palpite #se a letra estiver na palavra, ele preenche a lista "MOSTRADOR" na posição correta
            print(mostrador)
            print('')
            if cont_ponto == len(palavra):
                break
    print(f'Você acertou em {cont_palpite} chutes! A palavra era: {palavra.upper()}')

    op=str(input('Deseja jogar novamente [S/N]: ')).upper() #verifica se o ousuário deseja continuar o programa
    if op=='S': #se deseja continuar, ele reseta a lista da palavra e os contadores dos palpites e pontuação.
        mostrador.clear()
        cont_ponto=0
        cont_palpite=0
    elif op!='S':
        break
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- FIM DO PROGRAMA
