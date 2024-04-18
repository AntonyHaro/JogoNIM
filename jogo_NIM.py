n_global = 0
m_global = 0
placar = 0

def computador_escolhe_jogada(n, m):
    global n_global
    global m_global

    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            m_global = i
            n_global = n - m_global
            if m_global == 1:
                return f"O computador retirou apenas uma peça do tabuleiro!"
            else:
                return f"O computador retirou {m_global} peças do tabuleiro!"

    m_global = m
    n_global = n - m_global

    return f"O computador retirou {m_global} peças do tabuleiro!"

def usuario_escolhe_jogada(n, m):
    global n_global
    global m_global   
    m_global = int(input("Quantas peças você vai tirar? "))
    while(m_global < 1) or (m_global > m) or (m_global > n):
        print("Oops! Jogada inválida! Tente de novo.")
        m_global = int(input("Quantas peças você vai tirar? "))  
    n_global = n - m_global
    if m_global == 1:
        return f"Você retirou apenas uma peça do tabuleiro!"
    else:
        return f"Você computador retirou {m_global} peças do tabuleiro!"

def partida():
    global placar
    global n_global
    global m_global
    n_global = int(input("Quantas peças existem no tabuleiro? "))
    m = int(input("Qual é o limite de peças por jogada? "))
    
    if(n_global % (m + 1) == 0):
        print("Você começa!")
        while(n_global != 0):
            print(usuario_escolhe_jogada(n_global, m))
            if(n_global > 1):
                print("Agora restam", n_global, "peças no tabuleiro.")
            elif(n_global == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
            if(n_global == 0):
                placar = 1
                return f"Você venceu!" 
                   
            print(computador_escolhe_jogada(n_global, m))
            if(n_global > 1):
                print("Agora restam", n_global, "peças no tabuleiro.")
            elif(n_global == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
            if(n_global == 0):
                placar = 2
                return f"O computador ganhou!"
            
    else:
        print("Computador começa!")
        while(n_global != 0):
            print(computador_escolhe_jogada(n_global, m))
            if(n_global > 1):
                print("Agora restam", n_global, "peças no tabuleiro.")
            elif(n_global == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
            if(n_global == 0):
                placar = 2
                return f"O computador ganhou!" 

            print(usuario_escolhe_jogada(n_global, m))
            if(n_global > 1):
                print("Agora restam", n_global, "peças no tabuleiro.")
            elif(n_global == 1):
                print("Agora resta apenas uma peça no tabuleiro.")
            if(n_global == 0):
                placar = 1
                return f"Você venceu!"
            
def campeonato():
    global placar
    x = 0
    y = 0
    
    print()
    print("**** Rodada 1 ****")
    print(partida())
    if(placar == 1):
        x = x + 1
    else:
        y = y + 1
    
    print()
    print("**** Rodada 2 ****")
    print(partida())
    if(placar == 1):
        x = x + 1
    else:
        y = y + 1
    
    print()
    print("**** Rodada 3 ****")
    print(partida())
    if(placar == 1):
        x = x + 1
    else:
        y = y + 1

    print()
    print("**** Final do campeonato! ****")
    print("Placar: Você", x, "X", y, "Computador" )
    print()
    if(x > y):
        return f"Uau! Você ganhou o campeonato!"
    else:
        return f"Que pena! O computador ganhou o campeonato!"
    
def main():
    print("Bem-vindo ao jogo do NIM! O jogador que retirar a última peça do tabuleiro ganha!")
    print("Vamos jogar! Escolha:")
    print()
    x = int(input("Digite 1 para jogar uma partida isolada ou 2 para jogar um campeonato: "))
    
    while(x < 1) or (x > 2):
        print("Engraçadinho! Escolha corretamente!")
        x = int(input("Digite 1 para jogar uma partida isolada ou 2 para jogar um campeonato: "))
        if(x == 1):
            print("Você escolheu jogar uma partida! O jogo vai começar!")
            return(partida())
        elif(x == 2):
            print("Você escolheu um campeonato! O campeonato vai começar!")
            return(campeonato())
        
    if(x == 1):
        print("Você escolheu jogar uma partida! O jogo vai começar!")
        return(partida())
    elif(x == 2):
        print("Você escolheu um campeonato! O campeonato vai começar!")
        return(campeonato())
    
print(main())