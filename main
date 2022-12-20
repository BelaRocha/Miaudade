#para apk

class data:
    import os
    from time import sleep
    import sys
    import random
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

    #utilidades-------------------------------------------------------------------------------------------------------------------------
    def clear(): data.os.system('cls') #função que limpa a tela do terminal

    def valInt(texto): #valInt: função que valida um input int (para menus e opçoes e etc) (use como se fosse um input normal)
        while True:
            try:
                valor = int(input(texto)) #voce insere o texto que quiser exibir antes da chamada de input aqui.
                break
            except ValueError:
                input("Opção inválida. Pressione Enter para tentar novamente... ") 
                continue
        return valor

    def dotArt(arquivo): #função que lê arquivos .txt (para ler as dot arts)
        arqTxt = open(f'{arquivo}.txt', 'r', encoding='utf-8')
        print(arqTxt.read())

    def animar(frase):
        while True:
            for letra in frase:
                print(letra, end='')
                data.sys.stdout.flush()
                data.sleep(0.05)
            break

    def falas(txt, nome, fala):
        data.clear()
        data.dotArt(txt)
        data.print(f"{nome}")
        data.animar(fala)
        input()
        data.clear()

    #check dos itens---------------------------------------------------------------------------------------------------------------
    temChave = False
    temAmuleto = False
    global temFlor 
    temFlor = False
    global temPena
    temPena = False
    global temCristal
    temCristal = False
    global temMassa
    temMassa = False

    fugiuCasa = False

    ingredientesLista = [temFlor, temPena, temCristal, temMassa]


    def ingredientesFalta():
        ingredientes = 0
        if temFlor:
            ingredientes += 1
        if temPena:
            ingredientes += 1
        if temCristal:
            ingredientes += 1
        if temMassa:
            ingredientes += 1
        ingFalta = 4 - ingredientes
        return ingFalta
    #sistemas-------------------------------------------------------------------------------------------------------------------------

    #lutinha piu piu piu kabum

    def sorteAtaque(eInimigo):
        listaDano = [0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 4]
        dadinho = (data.random.randint(0,19))
        if eInimigo == True:
            dano = listaDano[dadinho]
        else:
            if data.temAmuleto == False:
                data.animar('\nSua sorte foi: ')
                print(dadinho)
            else:
                dadinho = dadinho + 2
                data.animar('\nSua sorte foi: ')
                print(dadinho)
            data.sleep(0.05)
            dano = listaDano[dadinho]
            data.animar('\nSeu dano foi: ')
            print(dano)
        return dano



    #uiui covarde fugir

    def sortefuga():
        listafug = [False, True]
        dadinho = (data.random.randint(0,19))
        if data.temAmuleto == False:
            data.animar('\nSua sorte foi: ')
            print(dadinho)
        else:
            dadinho = dadinho + 2
            data.animar('\nSua sorte foi: ')
            print(dadinho)
        if dadinho >= 9:
            fug = listafug[1]
        else:
            fug = listafug[0]
        if fug == True:
            data.animar('\nSucesso!')
        else:
            data.animar('\nFalha!')
        return fug

    def ataquePudim():
        data.animar("\nPudim prepara sua espada para um golpe!")
        data.input('\nPressione Enter para atacar!')
        data.sleep(0.25)
        dano = data.sorteAtaque(eInimigo = False)
        if dano <= 0:
            data.animar("\nErro crítico! Pudim erra o inimigo!")
        elif dano >= 4:
            data.animar("\nAcerto crítico! Pudim acerta em cheio!")
        return dano

    def ataqueInimigo(inimigo):
        data.animar("\nO inimigo prepara um ataque!")
        data.sleep(0.5)
        dano = data.sorteAtaque(eInimigo = True)
        dano += inimigo['atk']
        if dano <= 0:
            data.animar("\nErro crítico! O inimigo errou!")
        elif dano >= 4:
            data.animar("\nAcerto crítico! O inimigo te acertou em cheio!")
        return dano

    #menus-------------------------------------------------------------------------------------------------------------------------

    def chamarMapaInicial():
        mapaTxt = open("txtes\mapainicial.txt", 'r', encoding='utf-8')
        print(mapaTxt.read())
        while True:
            mapaOpcao = data.valInt("Insira onde quer ir: ")
            match mapaOpcao:
                case 0:
                    data.animar("Não é hora de voltar ainda!")
                    data.input()
                    data.clear()
                    continue
                case 1:
                    data.clear()
                    classetorre()
                case 2:
                    data.animar('Você tem que resgatar o Grande Mago, foco!')
                    input()
                    data.clear()
                    continue
                case 3:
                    data.animar('Você tem que resgatar o Grande Mago, foco!')
                    input()
                    data.clear()
                    continue
                case 4:
                    data.animar('Você tem que resgatar o Grande Mago, foco!')
                    input()
                    data.clear()
                    continue
                case 5:
                    data.animar('Você tem que resgatar o Grande Mago, foco!')
                    input()
                    data.clear()
                    continue
                case _:
                    data.animar('Opção inválida')
                    input()
                    data.clear()
                    continue

    def chamarMapa():

        while True:
            mapaTxt = open("txtes\mapa.txt", 'r', encoding='utf-8')
            print(mapaTxt.read())
            mapaOpcao = data.valInt("Insira onde quer ir: ")
            match mapaOpcao:
                case 0:
                    if temCristal and temFlor and temMassa and temPena == True:
                        data.clear()
                        classefinal()
                    else:
                        data.animar("Não seria legal voltar de patas vazias!")
                        input()
                        data.clear()     
                case 1:
                    data.animar("Não há mais o que fazer na torre, precisamos dos ingreditentes!")
                    input()
                    data.clear()
                case   2:
                    if temFlor == False:
                        data.clear()
                        classefloresta()
                    else:
                        data.animar('Não há mais o que fazer aqui! ')
                        input()
                        data.clear()
                        continue
                case 3:
                    if temCristal == False:
                        data.clear()
                        classemina()
                    else:
                        data.animar('Não há mais o que fazer aqui! ')
                        input()
                        data.clear()
                        continue
                case 4:
                    if temMassa ==  False:
                        data.clear()
                        classeitaliano()
                    else:
                        data.animar('Não há mais o que fazer aqui! ')
                        input()
                        data.clear()
                        continue
                case 5:
                    if data.temAmuleto or data.fugiuCasa == False:
                        data.clear()
                        classecasamisteriosa()
                    elif data.fugiuCasa == True:
                        data.animar('Nunca que volto naquele lugar!')
                        input()
                        data.clear()
                        continue
                    else:
                        data.animar('Não há mais o que fazer aqui! ')
                        input()
                        data.clear()
                        continue
                case _:
                    data.animar('Opção inválida')
                    input()
                    data.clear()
                    continue 

    def luta(inimigo): #menu principal quando começam encontros com inimigos
        data.clear()
        while True:
            data.dotArt(inimigo['txt'])
            data.animar(inimigo['chamada'])
            print(f"\n----------------------------------\
            \n1 - Atacar\
            \n2 - Pudim\
            \n3 - Checar Inimigo")
            menuOpcao = data.valInt("Insira opção: ")
            match menuOpcao:
                case 1:
                    data.clear()
                    pudimHp = 10
                    while True:
                        danoPudim = data.ataquePudim()
                        inimigo['hp'] -= danoPudim
                        data.animar(f"\nO HP do {inimigo['nome']} é: {inimigo['hp']}!")
                        if inimigo['hp'] < 1:
                            break
                        danoInimigo = data.ataqueInimigo(inimigo)
                        pudimHp -= danoInimigo
                        if danoInimigo > 0:
                            data.animar(f"\nOuch! o {inimigo['nome']} te deu {danoInimigo}! Seu HP é: {pudimHp}!")
                        if pudimHp < 1:
                            break
                    if pudimHp >= 1: 
                        data.animar('\nSucesso!')
                        break
                    else:
                        data.morreu()
                        break  
                case 2:
                    data.pudim(inimigo)
                case 3:
                    data.clear()
                    data.dotArt(inimigo['txt'])
                    data.print(f"{inimigo['nome']}\
                        \n----------------------------\
                        \n{inimigo['descricao']}\
                        \nHP: {inimigo['hp']}\
                        \nAtaque: {inimigo['atk']}")
                    input()
                    continue
                case _:
                    input("Opção inválida. Pressione Enter para voltar... ")
                    continue


    def pudim(inimigo): #menu do inventario do pudim
        data.clear()
        while True:
            data.dotArt('txtes/pudim')
            print(f"Pudim\
                \n------------------\
                \n1 - Checar o Pudim \
                \n2 - Itens do Pudim\
                \n3 - Retornar")
            menuPudim = data.valInt("Insira opção: ")
            match menuPudim:
                case 1:
                    data.clear()
                    data.dotArt('txtes/pudim')
                    print("Pudim - sobrenome: de Limão\
                        \n-----------------------------\
                        \nHP: 20 - Não deixe chegar a 0\
                        \nForça: 3 - Bem forte, para um gatinho\
                        \nAtaque: 5 - Sua espada é sua maior aliada\
                        \nAgilidade: 6 - Jovem e flexível, um felino admirável")
                    if data.temAmuleto == True:
                        print("Sorte: 10 - Pudim tem certeza que é o gato mais sortudo de Miaudade")
                    else:
                        print("Sorte: 8 - Pudim está se sentindo sortudo hoje")
                    input()
                    continue
                case 2:
                    data.clear()
                    print(f"1 - {data.inventario.espada['nome']}")
                    if data.temChave == True:
                        print("2 - Chave Brilhante")
                    if data.temAmuleto == True:
                        print(f"3 - {data.inventario.amuleto['nome']}")
                    if temFlor == True:
                        print(f"4 - {data.inventario.flor['nome']}")
                    if temPena == True:
                        print(f"5 - {data.inventario.pena['nome']}")
                    if temCristal == True:
                        print(f"6 - {data.inventario.cristal['nome']}")
                    if temMassa == True:
                        print(f"7 - {data.inventario.massa['nome']}")
                    print("Pressione 0 para voltar")
                    itemOpcao = data.valInt("Insira Opção: ")
                    data.clear()
                    if itemOpcao == 1:
                        data.inventario.chamarItem(data.inventario.espada)
                        continue
                    if itemOpcao == 2 and data.temChave == True:
                        data.inventario.chamarItem(data.inventario.chave)
                        continue
                    if itemOpcao == 3 and data.temAmuleto == True :
                        data.inventario.chamarItem(data.inventario.amuleto)
                        continue
                    if itemOpcao == 4 and temFlor == True:
                        data.data.inventario.chamarItem(data.inventario.flor)
                        continue
                    if itemOpcao == 5 and temPena == True:
                        data.inventario.chamarItem(data.inventario.pena)
                        continue
                    if itemOpcao == 6 and temCristal == True:
                        data.inventario.chamarItem(data.inventario.cristal)
                        continue
                    if itemOpcao == 7 and temMassa == True:
                        data.inventario.chamarItem(data.inventario.massa)
                        continue
                    else:
                        continue
                case 3:
                    data.clear()
                    data.luta(inimigo)
                case _:
                    input("Opção inválida. Pressione Enter para voltar... ")
                    continue

    def morreu():
        data.sleep(1.0)
        data.clear()
        data.dotArt('txtes/gatoosso')
        data.animar('                       Você falhou... Miaudade cai sob o caos em sua ausência...')
        input('\n                        Pressione Enter para voltar para o Menu Principal...')
        data.sleep(0.25)
        classemenu()
                                
    class inventario:

        def chamarItem(item):
            data.dotArt(item['txt'])
            print(f"{item['nome']}\n-----------------------------\n{item['descricao']}")
            input()
        chave = {
            'txt': 'txtes/chave',
            'nome': 'Chave Brilhante',
            'descricao': 'Uma chave dourada e brilhante, difícil de tirar os olhos.'
        }
        espada = {
            'txt':'txtes/espada',
            'nome':'Espada Velha',
            'descricao':'Uma espada enferrujada e antiga.'
        }
        amuleto = { 
            'txt':'txtes/amuleto', 
            'nome': 'Amuleto Misterioso da Sorte',
            'descricao': 'Um amuleto estranho que Pudim conseguiu de uma casa misteriosa.\
                        \nVocê se sente mais sortudo usando ele. Adiciona +2 Sorte'
        }
        flor = {
            'txt':'txtes/flor',
            'nome': 'Flor Ancestral',
            'descricao': 'Uma belissima flor de tempos ancestrais. Emana uma fragância distinta, mas agrádavel.\
                        \nEntregue ao Gato Mago Bola de Pelos junto com os outros ingredientes.'
        }
        pena = {
            'txt':'txtes/pena',
            'nome': 'Pena Suja',
            'descricao': 'Uma pena um pouco suja, retirada da plumagem de um pombo despercebido.\
                        \nEntregue ao Gato Mago Bola de Pelos junto com os outros ingredientes.'
        }
        cristal = {
            'txt':'txtes/cristal',
            'nome': 'Cristal Reluzente',
            'descricao': 'Um cristal encantador que emana uma luz fraca.\
                        \nEntregue ao Gato Mago Bola de Pelos junto com os outros ingredientes.'
        }
        massa = {
            'txt':'txtes/macarrao',
            'nome': 'Massa Sagrada',
            'descricao': 'Uma massa italiana da mais alta qualidade. A obra prima da vida do Doguitaliano.\
                        \nEntregue ao Gato Mago Bola de Pelos junto com os outros ingredientes.'
        }

    #inimigos

    soldadoRato = {
        'txt': 'txtes/soldadorato',
        'nome': 'Soldado Rato',
        'descricao': 'Um grande e forte soldado rato. Parece que não vão muito com a sua cara.',
        'chamada': 'Um Soldado Rato ergue-se na sua frente! Cuidado Pudim!',
        'atk': 0,
        'hp': 5
    }
    ratão = {
        'txt': 'txtes/ratão',
        'nome': 'Ratão',
        'descricao': 'Um ratazana enorme, tanto para cima quanto pros lados. Parece muito perigosa.',
        'chamada': 'O Ratão pisoteia a frente! Cuidado Pudim!',
        'atk': 0.5,
        'hp': 6
    }

    ratãoFinal = {
        'txt': 'txtes/ratão',
        'nome': 'Ratão: o Grande Rato',
        'descricao': 'O Ratão retorna. Ele parece nervoso e inspirado, sua força é maior do que antes.',
        'chamada': 'O chão treme sob as patas do Ratão! Muito cuidado Pudim!',
        'atk': 2.5,
        'hp': 10
    }

    dinoPlanta = {
        'txt': 'txtes/dinoplanta',
        'nome': 'Dinoplanta: a Planta Ancestral',
        'descricao': 'Uma planta carnívora de eras antepassadas. Nos tempos antigos, plantas dinossauro alimentavam-se de felinos.',
        'chamada': 'A Planta Ancestral estica suas vinhas! Muito cuidado Pudim!',
        'atk': 1,
        'hp': 7
    }

    monstroLago = {
        'txt': 'txtes/monstrolago',
        'nome' : 'Monstro Cristalino: o Protetor das Jóias',
        'descricao': 'Um monstro misterioso que se camufla perfeitamente nas cavernas da mina. Extremamente perigoso.',
        'chamada': 'A olhos do monstro brilham o mesmo azul que cintila dos cristais nas suas costas. Muito cuidado Pudim!',
        'atk': 1.5,
        'hp': 8
    }

    italiano = {
        'txt': 'txtes/italiano',
        'nome' : 'Doguitaliano: O Cão Gourmet',
        'descricao': 'Um cão italiano, excepcionalmente excêntrico. É um mestre da ávido da cúlinaria',
        'chamada': 'O Doguitaliano late para você, e mostra suas prezas! Muito cuidado Pudim!',
        'atk': 2,
        'hp': 9
    }

def classemenu():

    data.clear()

    while True:
        data.dotArt('txtes/pata')
        data.sleep (1.0)
        print(' _______  __                   __            __\n|   |   ||__|.---.-..--.--..--|  |.---.-..--|  |.-----.\n|       ||  ||  _  ||  |  ||  _  ||  _  ||  _  ||  -__|\n|__|_|__||__||___._||_____||_____||___._||_____||_____|')
        data.sleep(0.5)
        option= data.valInt('\n \n      1- Jogar            2- Creditos\n                    ')
        data.clear()
        match option:
            case 1:
                data.animar('Os gatos viviam felizes há muito tempo em Miaudade, onde tinham comida e camas quentinhas para dormirem o dia todo. Um dia, os soldados do Rato Reiqueijão\
                        \ninvadiram e ocuparam a cidade, expulsando todos os gatos. O Rei Rato sabia que o único felino que poderia tira-lo do poder era o Mago Bola de Pelos e então,\
                        \npor medo, ele o aprisionou em uma torre perto da Floresta Macabra. Os gatos felizmente conseguiram  construir um esconderijo não muito longe da cidade,\
                        \nonde também tinham camas quentinhas, por isso muitos gatos perderam a vontade de lutar e decidiram continuar se escondendo...')
                data.clear()
                classeinicio()
                
            case 2:
                data.animar('Feito por Izabela e Álvaro')
                input()
                data.clear()
                continue



def classeinicio():
    import sys

    #introdução
    data.animar('Inúmeros gatinhos dormem silenciosa (e preguiçosamente) no Miauderijo...   Enquanto isso, um felino solitario se levanta')
    input()
    data.clear()

    #diálogos
    data.falas('txtes/pudim', 'Pudim', 'Rum... não vou ficar parado aqui... Miau!')
    data.animar('Pudim pula por cima dos outros gatos e corre até a saida do seu abrigo.')
    data.falas('txtes/gatovelho', 'Gato Sabio Sr. bigodes', 'Espere, Pudim!')
    data.falas('txtes/pudim', 'Pudim', 'Vô Bigodes! Não tente me deter vovô... alguém precisa fazer algo!')
    data.falas('txtes/gatovelho', 'Sr. bigodes', 'Eu sei Pudim... e precisamos que seja você!')
    data.falas('txtes/pudim', 'Pudim', 'O que?')
    data.falas('txtes/gatovelho', 'Sr. bigodes', 'Os outros gatinhos são preguiçosos demais! \nVocê acabou de completar 1 ano, (15 Anos em idade felina), e ainda \nestá cheio de energia. Só você pode nos salvar, Pudim...')
    data.falas('txtes/pudim', 'Pudim', 'Hmm... bem, nesse caso, já tô de partida')
    data.falas('txtes/gatovelho', 'Sr. bigodes', 'Espere, Pudim!',)
    frase = '.\n.\n.'
    while True:
        for letra in frase:
            print(letra, end='')
            sys.stdout.flush()
            data.sleep(0.5)
        break
    data.falas('txtes/gatovelho', 'Sr. bigodes', 'É perigoso demais ir desequipado... Tome isso.')
    data.falas('txtes/espada', 'Pudim recebeu a Espada Velha', '')
    data.falas('txtes/gatovelho', 'Sr. bigodes', 'Use isso, e salve o Grande Gato Mago, o ilustre Bola de Pelos!\n Ele é a nossa esperança, o único poderoso o suficiente para se livrar dos ratos!')
    data.falas('txtes/pudim', 'Pudim', 'Então... tenho que resgatá-lo! Sei que o prenderam nas masmorras da Grande Torre!\nObrigado vovô, tenho minha missão! Me deseje sorte...')
    data.animar('O corajoso Pudim salta para fora, iniciando sua aventura.')

    data.chamarMapaInicial()



def classecasamisteriosa():
    #acontecimentos
    print("      __________\n   _-'      _-'||'-_ \n_-'______-xxxxxxxxxxx_\n [_[]__[]_[__I-==-I_]\n [_[]__[]_[__]/--\[_]\n [_II__II_[__]|__|[_]")
    data.animar('\nentrando em Casa Misteriosa')
    data.sleep(2.0)
    data.clear()
    data.sleep(1.0)
    data.animar('Pudim se aproxima da casa misteriosa. Nunca em Miaudade havia ele visto esse lugar, pode ser perigoso.\nChegar mais perto?')
    escolha = data.valInt('\n1-Sim               2-Não\n            ')
    data.clear()
    match escolha:
        case 1:
            data.animar('Pudim bate na porta da casa misteriosa... ninguém vem atender. Pudim percebe que a porta estava aberta e entra (sem educação).')
            input()
            data.falas('txtes/pudim', 'Pudim', 'Rummm... que lugar é esse?')
            data.animar('Uma fumaça grossa cobre por inteiro o recinto, dificultando até ver as paredes do lugar.\nVultos sombrios deixam rastros pelo ambiente esfumaçado e sons estranhos arrepiam até a ponta do rabo do Pudim, que avança cautelosamente.\nEm meio ao breu e toda a fumaça que lacrimeja os olhos do gato, ele avista um objeto brilhante um pouco mais a frente, que parece atrair não só os olhos mas a mente de Pudim.')
            escolha = data.valInt('\n1 - Ceder e pegar o objeto           2 - Resistir e voltar\n                  ')
            data.clear()
            match escolha:
                case 1:
                    data.animar('Pudim chega mais perto, e estende sua pata até o objeto. Ao tocá-lo, sua mente começa a girar, e suas vistas a escurecer...')
                    frase = '.      .      .'
                    while True:
                        for letra in frase:
                            print(letra, end='')
                            data.sys.stdout.flush()
                            data.sleep(0.2)
                        break
                    data.animar('Pudim abre os olhos, parece q se passaram horas, ou talvez minutos? Ele percebe, em sua pata, um amuleto estranho, que não estava com ele antes.\nEle se levanta, e a casa misteriosa, havia desaparecido por completo. Teria sido tudo um sonho?')
                    data.falas('txtes/amuleto', '', '(Pudim conseguiu o Amuleto da Sorte!)')
                    data.temAmuleto = True
                case 2:
                    data.animar('O bom senso de Pudim parece falar mais alto, e ele corre para fora da casa sem olhar para trás. Ele nunca saberá o que era aquilo.')
                    data.fugiuCasa = True
        case 2:
            data.animar('Você dá meia volta e vai embora, com o rabinho entre as pernas.')
            data.fugiuCasa = True
    #abre mapa
    data.clear()
    data.chamarMapa()



def classefinal():
        #ato final
    data.animar('Pudim avança por Miaudade, percebendo um vazio estranho pela cidade. O ar parece completamente parado enquanto o gato corre para o\
        \nMiauderijo, ele se pergunta onde foram todos os Soldados Ratos que marchavam pelas ruas, mas não permite que sua mente vague por\
        \nmuito tempo. Logo a saída da cidade aparece a vista, e depois dela a o Miauderijo.')
    input()
    data.clear()

    data.falas('txtes/pudim', 'Pudim', 'Rummmm... Esperava algo a mais, foi muito fácil!')
    data.falas('txtes/gatovelho', 'Sr. Bigodes', 'Pudim, você retornou!')
    data.falas('txtes/gatomago', 'Bola de Pelos', 'Pudim... você recolheu todos os ingredientes?')
    data.falas('txtes/pudim', 'Pudim', 'Sim... aqui estão...')
    data.animar('(Pudim entrega a Flor, a Pena, o Cristal e a Massa para o Mago Bola de Pelos)')
    input()
    data.clear()
    data.falas('txtes/gatomago', 'Bola de Pelos', 'Certo! Então, meu trabalho começa agora!')
    data.animar('O gato Bola de Pelos se retira, adentrando uma sala escura com os ingredientes em patas. Pudim e Sr. Bigodes permanecem, ansiosos\
        \ne tensos.')
    input()
    data.clear()
    data.falas('txtes/gatovelho', 'Sr. Bigodes', 'Pudim, se isso funcionar, Miaudade estará li--')

    data.animar('???\nHihihi!\nGatos imundos! Saiam daí agora!')
    input()
    data.clear()
    data.falas('txtes/pudim', 'Pudim', 'O que? De quem é essa voz aguda e estridente?')
    data.animar('Pudim e o velho Sr. Bigodes saem para fora do Miauderijo, e são encontrados por uma dupla aterrorizante.')
    input()
    data.clear()
    data.falas('txtes/ratão', 'Ratão', 'Nos encontramos novamente, bichano!')
    data.falas('txtes/pudim', 'Pudim', 'Você! Já é tarde demais, ratão!')
    data.falas('txtes/gatovelho', 'Sr. Bigodes', 'Não pode ser! Reiqueijão, seu dentuço maldito!')
    data.animar('???\nHihihi...')
    input()
    data.clear()
    data.falas('txtes/reiqueijão', 'Reiqueijão, o Rei dos Ratos', 'Hihihihihihihi!!! Simmm! Eu, o Reiqueijão (leia-se requeijão), vim prender vocês, meliantes!')
    data.falas('txtes/pudim', 'Pudim', '...')
    data.falas('txtes/reiqueijão', 'Reiqueijão', 'Hihihi...hiiii!')
    data.falas('txtes/pudim', 'Pudim', 'Ei ratão, você era o Reiqueijão desde o início?!')
    data.falas('txtes/ratão', 'Ratão (não é o Reiqueijão)', 'Não, gato burro! Você está na presença do mais ilustre Rei do reino animal, meu irmão! Tenha respeito.')
    data.falas('txtes/gatovelho', 'Sr. Bigodes', 'Sim, Pudim, esse é o Reiqueijão... o tirano que tomou nossa Miaudade!')
    data.falas('txtes/gatomago', 'Bola de Pelos', 'Pudim? Sr. Bigodes? A receita está quase pronta! Onde vocês es--')
    data.falas('txtes/reiqueijão', 'Reiqueijão', 'Bola de Pelos! Farei você voltar para sua cela!')
    data.falas('txtes/gatomago', 'Bola de Pelos', 'Rei! Droga, o que será de nós ag--')
    data.falas('txtes/pudim', 'Pudim', 'Você, colocar alguem numa cela? Acho mais facil pisarem em você, nanico! Hahahaha!')
    data.falas('txtes/reiqueijão', 'Reiqueijão', 'O queeeeeeeeeeeeeeeeeeeee?!!!!!')
    data.falas('txtes/ratão', 'Ratão', 'Ora... agora você foi longe de mais, bichano! Olha como você fala com o meu irmãozinho!')

    #luta com ratão

    data.falas('txtes/ratão', 'Ratão', 'Argh... de novo, não! Irmão... fuja!')
    data.falas('txtes/reiqueijão', 'Reiqueijão', 'Irmãozão!')
    data.falas('txtes/pudim', 'Pudim', 'Rum! Agora só falta você, Reiqueijão!')
    data.falas('txtes/gatomago', 'Bola de Pelos', 'Pudim! O feitiço secreto que nos livrará dos ratos está pronto!')
    data.falas('txtes/pudim', 'Pudim', 'Ótimo! E você, reizinho, você vem comigo!')

    data.animar('Pudim, levando o rei consigo, adentra o Miauderijo novamente. O gato mago Bola de Pelos deixa o trio aguardando por mais alguns\
        \nminutos, até que finalmente, ele retorna com uma grande tigela de madeira. O cheiro que emana dela é divino para o olfato dos gatos\
        \nali presentes, porém, o efeito que parece ter no rei rato aparenta ser dez vezes maior.')

    data.falas('txtes/gatomago', 'Bola de Pelos', 'Aqui está... o Queijo Irresistível! Quando ele for colocado em ação, nenhum rato conseguirá se segurar.')
    data.falas('txtes/pudim', 'Pudim', 'É claro... rum... não seria de outro jeito.\\nMas, antes disso... O que fazer com você, Reiqueijão!?')
    data.animar('O rato parece ser retirado de um transe ao ouvir seu nome')
    input()
    data.clear()
    data.falas('txtes/reiqueijão', 'Reiqueijão', 'O-O que?!')
    data.falas('txtes/gatovelho', 'Sr. Bigodes', 'O que você sugere, Pudim?')
    data.falas('txtes/pudim', 'Pudim', 'Rum...')
    escolha = data.valInt('\n1-Sim               2-Não\n            ')
    data.clear()
    match escolha:
        case 1:
            data.falas('txtes/pudim', 'Pudim', '... sua crueldade com o Bolinha não vai passar despercebida, Reiqueijão! Os outros ratos vão para longe daqui, mas você...\
            \nvocê vai ficar!')
            data.falas('txtes/reiqueijão', 'Reiqueijão', 'O que-o que quer dizer?!')
            data.falas('txtes/pudim', 'Pudim', 'Para a masmorra da Torre! Você ficara preso em Miaudade, até que se arrependa completamente dos seus atos... mesmo que isso\
                \ndure para sempre!')
            data.falas('txtes/gatomago', 'Bola de Pelos', 'Então... preparados?...')
            data.animar('Os gatos saem mais uma vez, e sob o céu escarlate do por do sol, o gato mago traz o Queijo Irresistível, e o levanta para o topo de seu\
            \ncajado, o qual ele ergue e aponta ao céu.')
            input()
            data.clear()
            data.falas('txtes/gatomago', 'Bola de Pelos', 'Que esse Queijo irresistível e delicioso, voe ao mais distante horizonte, e leve os ratos para longe de Miaudade!')
            data.animar('Ao fim das suas palavras encantadas, o Queijo decola, voando alto e rapidamente pelo céu, até sumir de vista. Pouco se passa, e inúmeros ratos,\
            \ntodos ocupantes de Miaudade, correm na direção em que o laticinio partiu. A multidão logo sai de vista, e o gosto do sucesso chega à lingua\
            \nde Pudim. Miaudade está livre novamente.')
            input()
            data.clear()
            data.falas('txtes/pudim', 'Pudim', 'E você, Reiqueijão... para a masmorra!')
            data.animar('Pudim carrega o pequeno ratinho pelas ruas de Miaudade, enquanto ele grita e pede clemência. Os dois chegam até a Torre, o felino puxando o\
            \nroedor escada abaixo, até a cela onde o Gato Mago Bola de Pelos esteve preso.')
            input()
            data.clear()
            data.falas('txtes/pudim', 'Pudim', 'Esse é o seu novo lar... Rei do queijão...')
            
            data.animar('Fim\
                \n\nVocê salvou Miaudade e retornou aos gatos o seu lar, parabéns!\
                \n\nObrigado por jogar nosso jogo!')
            input()
            data.clear()
        case 2:
            data.falas('txtes/pudim', 'Pudim', 'Seus atos em Miaudade são imperdoáveis, Reiqueijão... mas, terei piedade de você! Você sairá da nossa cidade, junto dos seus\
                \noutros ratos!')
            data.falas('txtes/gatovelho', 'Sr. Bigodes', 'Pudim... que mais nobre ação! Fico feliz... em ver o gato que você se tornou!')
            data.falas('txtes/gatomago', 'Bola de Pelos', 'Então... preparados?...')
            data.animar('Os gatos saem mais uma vez, e sob o céu escarlate do por do sol, o gato mago traz o Queijo Irresistível, e o levanta para o topo de seu\
            \ncajado, o qual ele ergue e aponta ao céu.')
            input()
            data.clear()
            data.falas('txtes/gatomago', 'Bola de Pelos', 'Que esse Queijo irresistível e delicioso, voe ao mais distante horizonte, e leve os ratos para longe de Miaudade!')
            data.animar('Ao fim das suas palavras encantadas, o Queijo decola, voando alto e rapidamente pelo céu, até sumir de vista. Pouco se passa, e inúmeros ratos,\
            \ntodos ocupantes de Miaudade, correm na direção em que o laticinio partiu. A multidão logo sai de vista, e o gosto do sucesso chega à lingua\
            \nde Pudim. Miaudade está livre novamente.')
            input()
            data.clear()
            data.falas('txtes/pudim', 'Pudim', 'E você, Reiqueijão... vá, e não volte nunca mais!')
            data.animar('Pudim solta dos bracinhos frágeis do rato, que sai correndo na direção de seus compatriotas, sem olhar para trás.')
            input()
            data.clear()

            data.animar('Fim\
                \n\nVocê salvou Miaudade e retornou aos gatos o seu lar, parabéns!\
                \n\nObrigado por jogar nosso jogo!')
            input()
            data.clear()



    #area da floresta
def classefloresta():
    #acontecimentos
    print('         /\                             /\ \n    /\ //\\  /\  /\       /\       /\ //\\ \n\/\//\\/\\/\//\\//\\ /\/\//\\/\ /\//\///\\\/\                            \n\\///\\\\//\\/\///\\//\\///\\\\//\\/\///\\//\\ \n\\\//\\\///\\\///||///\\\//\\\///\\\///||///\\\ \n\\\/||\\///\\\///||///\\\/||\\///\\\///||///\\\ \n|\\\||\///||\\\  |///||\\\||\///||\\\  |///||\\\ \n|\\\|| ///||\\\   ///||\\\|| ///||\\\   ///||\\\ \n|         ||         ||         ||         ||')
    data.animar('\n Entrando em Floresta Macabra')
    data.sleep(2.0)
    data.clear()
    data.sleep(1.0)
    data.animar('Pudim adentra a floresta, uma densa vegetação ao seu redor.')
    input()
    data.clear()
    if data.temPena == False:
        data.animar('Ele sente uma vontade repentina de subir uma árvore, mas se controla. É quando ele nota, parado num galho, um pombo distraído!\nDar o bote?')
        data.animar('')
        data.animar('\n\n1-Atacar           2-Passar despercebido')
        escolha = data.valInt('\n             ')
        match escolha:
            case 1:
                data.animar('Você pula no pombo e arranca uma pena.')
                input()
                data.clear()
                data.falas('txtes/pombo', 'Pombo', 'Ei, o que pensa que tá fazendo? Prometo que vou te processar, seu gato imundo!')
                data.animar('O Pombo parece bravo. Ele sai voando para longe.')
                input()
                data.clear()
                data.falas('txtes/pena', '(Pudim pegou a Pena Suja!)', '')
                data.temPena == True
            case 2:
                data.animar('Você não faz nada. Parece uma oportunidade desperdiçada.')
                input()
                data.clear()
    if data.temFlor == False:
        data.animar('Pudim continua o seu caminho pela floresta, passando entre as arvores enquanto procura a flor até que encontra um Soldado Rato no caminho!\
            \nEle parece distraido cortando lenha, o que fazer?')
        data.animar('\n\n1-Atacar           2-Passar despercebido')
        escolha = data.valInt('\n             ')
        data.animar("Você pula no inimigo, o atacando de surpresa!") 
        data.menu_luta
        data.animar('...O rato cai derrotado, Pudim segue em frente novamente!') #sucesso
        input()
        data.clear()
        data.animar('Você tenta se camuflar nas árvores e passar despercebido...')
        data.animar('...Mas Pudim é branco! O rato percebe sua presença e te ataca!') 
        data.menu_luta
        data.animar('...E mesmo Pudim sendo branco, o rato é dautônico! Pudim passa de fininho e avança!') #sucesso
        input()
        data.clear()

        data.animar('Pudim anda por o que parecem horas para suas perninhas curtas de gatinho, até que, num caminho ingrime e escuro, ele vê,\
            \niluminada por um unico feiche de luz que corta pela copa das árvores, a Flor Ancestral! Pudim pula em sua direção, porém!')
        data.luta(data.dinoPlanta)
        data.animar('A Dinoplanta mítica de lenda cai derrotada de volta ao chão! Você segura a Flor Ancestral em suas patas')
        input()
        data.clear()
        data.falas('txtes/flor', '(Pudim pegou a Flor Ancestral!)', '')
        data.temFlor = True
        if data.ingredientesFalta == 0:
            data.falas('txtes/pudim', 'Pudim', 'Tudo bem, consegui todos! Agora tenho que voltar para o Miauderijo! Miau!')
        else:
            data.falas('txtes/pudim', 'Pudim', f'Tudo bem, Só mais {data.ingredientesFalta} pra pegar! Miau!')
    else:
        data.falas('Rum... o que tô fazendo aqui? Não tenho tempo pra perder!')
    data.chamarMapa



#casa de italiano
def classeitaliano():
    #acontecimentos
    print("// //// / // /====| \n|HH\ /HH\ /--|++++| \n|==| |==| |UU||HH|| \n|-- ¨ -- ¨ --||¨¨|| \n|¨¨ -( .)- ¨¨|----|")
    data.animar('\n Entrando em Casa de Italiano')
    data.sleep(2.0)
    data.clear()
    data.sleep(1.0)
    data.animar('Pudim faz seu caminho até a casa misteriosa ao lado da Torre, num primeiro olhar discreta, porém ao pular pela janela e ver o interior,\
        \nele percebe, claramente, que é uma casa de italiano. Quadros de queijos, lasanhas e pizzas decoram a casa junto aos papeis de parede\
        \nde tipos diferentes de macarrão. A casa parece vazia entretanto, talvez o dono estava fora num restaurante? Pudim pula para dentro e\
        \ncomeça a procurar a Massa Sagrada.')
    input()
    data.clear()
    data.animar('\n???\nEi, quem tá aí? Woof!')
    input()
    data.clear()
    data.animar('Uma voz latida corre de uma porta (há uma placa nela, escrito "Quarto")! Pudim corre para se esconder, se jogando atrás de um sofá\
        \n(com estampa de macarronada) e observando a figura que surge.')
    input()
    data.clear()
    data.falas('txtes/italiano', 'Doguitaliano', 'Quem tá aqui? Mi Familia não gosta de intrusos!\
        \nWoof... tentando se esconder? Saiba que nós cães italianos temos o mais apurado olfato do reino animal!')
    data.animar("O Doguitaliano se prepara para farejar o intruso (você), o que fazer")
    data.animar('\n\n1-Atacar           2-Passar despercebido')
    escolha = data.valInt('\n             ')
    match escolha:
        case 1:
            data.animar('Pudim avança contra o cão excêntrico, pulando para cima dele antes que farejasse sua posição! Ataque surpresa!')
            data.clear()
            fight = True
        case 2:
            data.animar('Pudim tenta passar de fininho pelo cão...')
            if data.sortefuga() == True:
                data.animar('\n...mas o cheiro delicioso de algo no forno atrapalha o fucinho do cão! Você foge para o "Quarto"!')
            else:
                data.animar('\n...mas Pudim cheira a pudim! é forte demais para passar pelo fucinho apurado do Doguitaliano!')
                fight = True

    if fight == True:
        data.falas('txtes/italiano', 'Doguitaliano','Oh, mamma mia, se não é um gato nojento! Veio virar parte da minha receita suprema, felino? Woof Woof!')
        data.falas('txtes/pudim', 'Pudim', 'Só se estiver fazendo um doce, Miau! Tenho certeza que tenho gosto de Pudim!')
        data.falas('txtes/italiano', 'Doguitaliano', 'Pudim, é? Tudo bem, não sou contra comidas agridoces, Woof! Minha receita secreta estará completa com você nela!')
        data.falas('txtes/pudim', 'Pudim', 'Receita? Por acaso teria um Massa Sagrada nessa sua receita?')
        data.falas('txtes/italiano', 'Doguitaliano', 'Mamma mia! Não esperava que um gato inculto como o próprio conheceria de culinaria! Pois é claro, é a receita que\
                    \nmudará o mundo, e usará da grande Massa Sagrada como fundamento.')
        data.falas('txtes/pudim', 'Pudim', 'Miau! Nesse caso, passe pra cá!')
        data.falas('txtes/italiano', 'Doguitaliano', 'Woof Woof! Não vai ser tão fácil assim, Pudim!')
        data.luta(data.italiano)
        data.falas('txtes/italiano', 'Doguitaliano', 'Arf... Arf... Droga! Diga, felino, você vai mesmo roubar a Massa Sagrada?')
        data.falas('txtes/pudim', 'Pudim', 'Sim! Pelo bem de Miaudade, preciso dela para levar os ratos para longe!')
        data.falas('txtes/italiano', 'Doguitaliano', 'Arf... nesse caso... me prometa, Pudim, que ira fazer uma receita que faz juz à culinária italiana!')
        data.falas('txtes/pudim', 'Pudim', 'Rum... Prometo, Dogui! Miau!')
        data.sleep(0.5)
        data.animar('Doguitaliano desmaia, você prossegue para o "Quarto".')
        input()
        data.clear()

    data.animar('Pudim adentra o "Quarto", e logo percebe que é uma cozinha, com uma casinha de cachorro em um dos cantos.\
        \nSobre uma bancada ele avista a Massa Sagrada, quentinha e apetitosa. Ele a segura, o cheiro delicioso entrando em seu fucinho.')
    input()
    data.clear()
    data.animar('Ele controla a vontade de experimentar e guarda a massa.')
    data.falas('txtes/macarrao', '(Pudim pegou a Massa Sagrada!)', '')
    data.temMassa = True
    if data.ingredientesFalta == 0:
        data.falas('txtes/pudim', 'Pudim', 'Tudo bem, consegui todos! Agora tenho que voltar para o Miauderijo! Miau!')
    else:
        data.falas('txtes/pudim', 'Pudim', f'Tudo bem, Só mais {data.ingredientesFalta} pra pegar! Miau!')
    data.chamarMapa() 



    #mina
def classemina():
    #acontecimentos
    print("       ______ \n    ___/   ___\_ \n __/.'.__/  _ \_\_ \n/.'___/    | |    \ \n':/   \:'''+-+''':.''. \n           +-+ \n            +-+")
    data.animar('\n Entrando em Mina Decadente')
    data.sleep(2.0)
    data.clear()
    data.animar('Pudim corre até a Mina nos arredores de Miaudade.\
                \nAs lendas sobre os perigos da Mina, há muito tempo abandonada pelos gatos, arrepiam os pelos do felino, enquanto ele adentra a mina. Não há sequer uma luz\
                \nfraca em vista. As paredes da caverna ecoam com os passos leves das patas do Pudim. O gato segue bravamente pela mina sombria, seus olhos felinos escaneando\
                \nminuciosamente através da escuridão porém, nenhum objeto reluzente é encontrado aqui, somente varias e varias placas espalhadas pelos cantos,\
                \ntodas escrito "PERIGO!".')
    input()
    data.clear()
    data.animar('Pudim as ignora e segue em frente, determinado a encontrar o Cristal. Seu caminho é livre, apenas pequenos insetos e animais rastejantes aparecendo no caminho,\
            \nque se amedrontam ao ver o gato e fogem. De repente, ao tomar uma esquina dentro do labirinto de cavernas da mina ele finalmente avista uma formação de cristais,\
            \nilhados no centro de um pequeno lago num grande espaço.')
    input()
    data.clear()
    data.falas('txtes/pudim', 'Pudim', 'Rum... água... por você, Miaudade!')
    data.animar('Pudim dá o maior salto de sua vida, passando com sua elegância felina por cima da água. Os cristais em sua frente são bonitos, e brilham com uma luz que ilumina\
        \nos arredores, porém, ele só precisa de um no momento (talvez ele volte para pegar mais e guardar como brinquedo para uso futuro). Pudim usa sua espada para quebrar um pedaço do cristal.')
    input()
    data.falas('txtes/cristal', 'Cristal Relusente', '(Pudim pegou o Cristal Reluzente)')
    input()
    data.clear()
    data.temCristal = True
    if data.ingredientesFalta == 0:
        data.falas('txtes/pudim', 'Pudim', 'Tudo bem, consegui todos! Agora tenho que voltar para o Miauderijo! Miau!')
    else:
        data.falas('txtes/pudim', 'Pudim', f'Tudo bem, Só mais {data.ingredientesFalta} pra pegar! Miau!')
    data.animar('Pudim pula de volta ao outro lado, e segue para a saída... até que o chão em baixo de suas patas começa a tremer! Pudim olha para trás e vê...')
    input()
    data.falas('monstrolago', 'Monstro Cristalino: o Protetor das Jóias', '')
    data.animar('O que antes era uma ilha com uma formação de cristais, se ergue do lago e se revela como um grande monstro, com cristais descendo por suas costas!')
    input()
    data.luta(data.monstroLago)
    data.animar('Pudim permanece de pé, como o vitorioso da grande batalha!')
    input()
    data.animar('Pudim deixa o monstro para trás, se retirando da Mina de uma vez por todas.')
    input()
    data.clear()
    data.chamarMapa()



    #torre
def classetorre():
    #falas e escolhas
    print("       /-\ \n <<|__/---\__|>> \n _// // |  \\ \_ \n| //// /-\ \\\  | \n/// ///---\\ \ \\ \n |=  =|===|=  =| \n  | = |___| = | \n  +=_________=+        \n   |   ===   |        \n   |   | |   | \n   |   ===   | \n  /|   | |   |\ \n | \   ===   / | \n |\ ':.....:' /| \n | \_________/ |             \n | [** === **] |             \n  \[++ | | ++]/   ")
    data.animar('\n Entrando em Torre')
    data.sleep(2.0)
    data.clear()
    data.sleep(1.0)
    data.animar('Pudim põe suas patas para bom uso, correndo até Miaudade.\nDentro da cidade, ele se depara com varios Soldados Ratos, os lacaios do Reiqueijão. O que fazer?')
    data.animar('\n\n1-Atacar           2-Passar despercebido')
    escolha = data.valInt('\n             ')
    data.clear()

    match escolha:
        case 1:
            data.animar('Você encara de frente os inimigos com sua espada em mãos... ')
            #luta soldado
            data.luta(data.soldadoRato)
            data.animar('O Pudim segue em frente, deixando os inimigos derrotados para trás!')
            input()
            data.clear()
        case 2:
            data.animar('Você tenta passar de fininho pelos ratos, dando passos leves...')
            input()
            if data.sortefuga() == True:
                data.animar('\n...e os deixa pra trás, sem nem saberem que esteve ali!')
            else:
                data.animar('\n...Mas se distrai com uma borboleta! Tentativa falha! ')
                data.luta(data.soldadoRato)
            data.clear()

    data.falas('txtes/pudim', 'Pudim', 'Moleza!')
    data.animar(' O resto do caminho até a Torre é livre. Pudim abre suas grandes portas (com dificuldade, por não ter dedos) e começa a procurar a entrada para a masmorra.\nHá dois caminhos na sua frente...')
    data.animar('\n\n1-Esquerda           2-Direita')
    escolha = data.valInt('\n              ')
    match escolha:
        case 1:
            data.animar('Pudim segue um longo corredor, se distraindo momentaneamente quando vê um mosquito.\nMais a frente, ele encontra um grande rato, dormindo, porém ao seu lado tem um objeto dourado brilhante. Pudim quer o objeto brilhante.\nO que fazer?')
            data.animar('\n1-Atacar           2-Tentar pegar despercebido')
            escolha = data.valInt('\n             ')
            data.clear()
            match escolha:
                case 1:
                    data.animar('Você ataca o inimigo enquanto ele dorme. Golpe Baixo!')
                    input ()
                    data.clear()
                    #luta soldado
                    data.luta(data.soldadoRato)
                    data.animar('O inimigo dorme de novo (por outro motivo dessa vez). Você se sente um pouco culpado.\n')
                    input ()
                    data.clear()
                    data.animar('Você passa por ele e pega o objeto brilhante, com ele em mãos, você percebe que o objeto é na verdade uma chave. Ele não parece brilhar tanto assim mais')
                    input ()
                    data.clear()
                    data.falas('txtes/chave', '', '(Pudim pegou a Chave!)')
                    data.temChave = True
                    input ()
                    data.clear()
                    data.animar('Você retorna pelo corredor, até a sala que estava antes. O que fazer?\n1- esquerda             2-Direita')
                    escolha = data.valInt('\n             ')
                    data.clear()
                    while escolha == 1:
                        data.animar('Você percebe que acaboou de sair desta sala então retorna pelo corredor, até a sala que estava antes. O que fazer?\n1- esquerda             2-Direita')
                        escolha = data.valInt('\n             ')
                        data.clear()
                        data.animar('Pudim segue abaixo por uma escada, alguns lances depois ele se surpreende ao dar de cara com um enorme rato, que o vê antes que Pudim pudesse reagir.')
                        input ()
                        data.clear()

                case 2:
                    data.animar('Você dá pulinhos e anda de fininho, até o rato...')
                    input ()
                    data.clear()
                    if data.sortefuga() == True:
                        data.animar('...e fácilmente pega o objeto do seu lado, afinal, ele estava dormindo!')
                        input()
                    else:
                        data.animar('...mas tropeça no próprio rabo! Tentativa falha, o rato acordou!')
                        input()
                        data.luta(data.soldadoRato)
                        data.clear()
                    data.animar('Com ele em mãos, você percebe que o objeto brilhante é na verdade uma chave. Ele não parece brilhar tanto assim mais')
                    input ()
                    data.clear()
                    data.falas('txtes/chave', '', '(Pudim pegou a Chave!)')
                    data.temChave = True
                    data.animar('Você retorna pelo corredor, até a sala que estava antes. O que fazer?\n1- esquerda             2-Direita')
                    escolha = data.valInt('\n             ')
                    data.clear()
                    while escolha == 1:
                        data.animar('Você percebe que acabou de sair desta sala então retorna pelo corredor, até a sala que estava antes. O que fazer?\n1- esquerda             2-Direita')
                        escolha = data.valInt('\n             ')
                        data.clear()
                        data.animar('Pudim segue abaixo por uma escada, alguns lances depois ele se surpreende ao dar de cara com um enorme rato, que o vê antes que Pudim pudesse reagir.')
                        input ()
                        data.clear()
    data.animar('Pudim segue abaixo por uma escada, alguns lances depois ele se surpreende ao dar de cara com um enorme rato, que o vê antes que Pudim pudesse reagir.')
    input ()
    data.clear()
    data.falas('txtes/ratão', 'Ratão', 'O que é isso, um gato? Achei que vocês tinham levado seus rabos entre as pernas pra aquele muquifo!')
    data.falas('txtes/pudim', 'Pudim', 'Não fale mal do Miauderijo! Agora, me diga logo onde esta o Bola de Pelos!')
    data.falas('txtes/ratão', 'Ratão', 'Escuta aqui, eu sou o guarda da masmorra!\n Não vou deixar você soltar o Bola de Pelos que está depois dessa porta atrás de mim!')
    data.falas('txtes/pudim', 'Pudim', 'Haha! Você acabou de me contar onde ele está, seu dentuço sujismundo!')
    data.falas('txtes/ratão', 'Ratão', 'O que? Droga!!... quer dizer... Foi de proposito!\n Te falei, porque sei que você não vai passar de mim, bichano! Devia ter ficado no muquifo!')
    data.falas('txtes/pudim', 'Pudim', 'Rum... Já disse pra não falar mal do Miauderijo!')
    #luta com ratao
    data.luta(data.ratão)
    data.animar('O Ratão cai desacordado, abrindo espaço para a porta atrás dele.')
    input()
    data.clear()
    while data.temChave == False:
        data.animar('Mas a porta está trancada! Hum, onde será que está a chave?')
        input()
        data.clear()
        data.animar('Você retorna, subindo a escada para a sala que estava antes.')
        input()
        data.clear()
        data.animar('Pudim segue um longo corredor, se distraindo momentaneamente quando vê um mosquito.\nEle encontra um grande rato, dormindo, porém ao seu lado tem um objeto dourado brilhante. Pudim quer o objeto brilhante.\nO que fazer?')
        data.animar('\n1-Atacar           2-Tentar pegar despercebido')
        escolha = data.valInt('\n             ')
        data.clear()
        match escolha:
            case 1:
                data.animar('Você ataca o inimigo enquanto ele dorme. Golpe Baixo!')
                input ()
                data.clear()
                #luta soldado
                data.animar('O inimigo dorme de novo (por outro motivo dessa vez). Você se sente um pouco culpado.')
                input()
                data.clear()
                data.animar('Você passa por ele e pega o objeto brilhante, com ele em mãos, você percebe que o objeto é na verdade uma chave. Ele não parece brilhar tanto assim mais')
                input ()
                data.clear()
                data.falas('txtes/chave', '', '(Pudim pegou a Chave!)')
                data.temChave = True
                input ()
                data.clear()
            case 2:
                    data.animar('Você dá pulinhos e anda de fininho, até o rato...')
                    input ()
                    data.clear()
                    if data.sortefuga() == True:
                        data.animar('...e fácilmente pega o objeto do seu lado, afinal, ele estava dormindo!')
                    else:
                        data.animar('...mas tropeça no próprio rabo! Tentativa falha, o rato acordou!')
                        data.luta(data.soldadoRato)
                        data.clear()
                    data.animar('Com ele em mãos, você percebe que o objeto brilhante é na verdade uma chave. Ele não parece brilhar tanto assim mais')
                    input ()
                    data.clear()
                    data.falas('txtes/chave', '', '(Pudim pegou a Chave!)')
                    data.temChave = True
    data.animar('Você usa a Chave!')
    input()
    data.clear()
    data.animar('Pudim desce o resto das escadas até que, no final, encontra uma única cela.')
    input()
    data.clear()
    data.animar('A Chave parece caber nessa fechadura também...')
    input()
    data.clear()
    data.animar('Abrir?\n1-Abrir           2-Não abrir')
    escolha = data.valInt()
    data.clear()
    match escolha:
        case 1:
            data.falas('txtes/pudim', 'Pudim', 'Vim resgatar você, Bola de Pelos, Miau!')
            data.animar('Um gato velinho, segurando um grande cajado, surje das sombras da cela.')
            input()
            data.clear()
            data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Veja só, se não é Pudim...')
            data.falas('txtes/pudim', 'Pudim', '...')
            data.falas('txtes/gatomago', 'Mago Bola de Pelos', '...')
            data.falas('txtes/pudim', 'Pudim', '...')
            data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Então...\nPor que interrompeu minha soneca, Pudim?')
            data.falas('txtes/pudim', 'Pudim', 'Eu vim te resgatar, velho caduco!... quer dizer, Mago Bola de Pelos!\nOs ratos tomaram conta da nossa cidade, e os gatos de Miaudade foram exilados pro Miauderijo! Precisamos da sua ajuda.')
            data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Hmm... a situação aparenta mais critica do que imaginei...\nPudim, poderia me levar ao Miauderijo?')
            data.falas('txtes/pudim', 'Pudim', 'Rum... vamos lá!')
            data.sleep(2.0)
            data.clear()
            classemiauderijo()
        case 2:
            data.animar('Pudim repensa a jornada em sua frente. O chamado a ação, os desafios que o encontrariam se continuasse a seguir aquele caminho.\
            \n"Por que eu?" ele pensa, indignado. Ele joga a chave no chão, e retorna pelo mesmo caminho que veio, sem olhar para trás. Pudim\
            \nfoge de Miaudade, não passando no Miauderijo para se despedir de seu avô ou de nenhum dos outros gatos.')
            input()
            data.clear()
            data.animar('A grandiosa hístoria de Pudim, e o ato valente que ele fez que com certeza teria mudado o rumo dos gatos de todo o mundo, nunca\
            \nse realizou para que um dia fosse contada. Nunca mais ouviram falar do Pudim novamente.')
            input()
            data.clear()
            data.animar('Fim.')
            data.sleep(2.0)
            input()
            data.clear()
            classemenu()


def classemiauderijo():
    #miauderijo]

    #atecimentos
    print('   /\   \n  //\\  \n //||\////\  /\   _____ \n  _||////==\//\\ ////==\ \n /==\| |__ |/||\ | | []| \n/====\/===\//||\\/\\\\\\\  \n| TT /=====//||\\==\ \\ \\ \n     |--T--| || |++|_| |_| ')
    data.animar('\n Entrando em Miauderijo')
    data.sleep(2.0)
    data.clear()
    data.sleep(1.0)
    data.animar('Pudim leva o velho Bola de Pelos até o Miauderijo, onde a dupla se reune com o Sabio Sr. Bigodes')
    input()
    data.clear()
    data.falas('txtes/gatovelho', 'Sr. Bigodes', ' É muito bom vê-lo saudável, ó grande mago!')
    data.falas('txtes/gatomago', 'Mago Bola de Pelos', ' Por favor, podem me chamar de Bola de Pelos...')

    frase = '...ou Bolinha...'
    data.dotArt('txtes/gatomago')
    print(f"{'Mago Bola de Pelos'}")
    while True:
            for letra in frase:
                print(letra, end='')
                data.sys.stdout.flush()
                data.sleep(0.2)
            break
    data.falas('txtes/pudim', 'Pudim', 'Tudo bem Bolinha, diz pra nós, como se livrar daqueles ratos!')
    data.falas('txtes/gatovelho', 'Sr. Bigodes', 'Ei, não chame o grande mago de Bolinha!')
    data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Eu tenho um plano, Pudim e Sr. Bigodes! Um feitiço que os levará para longe!')
    data.falas('txtes/pudim', 'Pudim', 'Ótimo Bolinha, Então faça logo sua magia!')
    data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Tudo em seu tempo, Pudim... o feitiço é grande e poderoso, por isso... vou precisar de ingredientes especiais!')
    data.falas('txtes/pudim', 'Pudim', 'Rum... lá vem.')
    data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Pudim, preciso que você recolha para mim os ingredientes mais poderosos dessa cidade!\n\n-A Flor Ancestral na Floresta Macabra\n-O Cristal Reluzente, da Mina Decadente\n-Uma Pena de uma grande ave.\n-E por último, a Massa Sagrada...')
    data.falas('txtes/pudim', 'Pudim', '...')
    data.falas('txtes/gatomago', 'Mago Bola de Pelos', '...')
    data.falas('txtes/pudim', 'Pudim', 'Ei! E essa tal de massa, você não falou onde que eu encontro essa aí!')
    data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Sinto que não terei a resposta para essa pergunta... mas talvez, o Grande Gato Sábio a tenha?')
    data.falas('txtes/gatovelho', 'Sr. Bigodes', 'Hummm... parece que com a vinda dos ratos, uma figura... estrangeira... construiu uma casa misteriosa perto da Torre\nUm italiano... Pudim, talvez ele possua a massa que procura, mas sinto que não será amigável com nós felinos.')
    data.falas('txtes/pudim', 'Pudim', 'Miau! Tenho minha missão! Obrigado vovô e Bolinha!')
    data.animar('Pudim salta para fora do Miauderijo, voltando à sua aventura.')
    input()
    data.clear()
    #(abre o mapa, agora com todas as áreas liberadas)
    data.chamarMapa()

print(classemenu())
