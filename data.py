from os import system
from time import sleep
import sys
from threading import Thread
import keyboard
#utilidades-------------------------------------------------------------------------------------------------------------------------
def clear(): system('cls') #função que limpa a tela do terminal

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
            sys.stdout.flush()
            sleep(0.05)
        break
    input()

def falas(txt, nome, fala):
    clear()
    dotArt(txt)
    print(f"{nome}")
    animar(fala)
    input()
    clear()

#check dos itens---------------------------------------------------------------------------------------------------------------
temChave = False
temAmuleto = False
temFlor = False
temPena = False
temCristal = False
temMassa = False
ingredientes = 0
ultimoIngrediente = False

if temFlor == True or temPena == True or temCristal == True or temMassa == True:
    ingredientes += 1

ingredientesFalta = 4 - ingredientes


#menus-------------------------------------------------------------------------------------------------------------------------

def chamarMapaInicial():
    mapaTxt = open("txtes\mapainicial.txt", 'r', encoding='utf-8')
    print(mapaTxt.read())
    mapaOpcao = valInt("Insira onde quer ir: ")
    match mapaOpcao:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            pass

def menu_luta(chamadaInimigo, txt): #menu principal quando começam encontros com inimigos
    clear()
    while True:
        dotArt(txt)
        animar(chamadaInimigo)
        print(f"\n----------------------------------\
        \n1 - Atacar\
        \n2 - Pudim\
        \n3 - Checar Inimigo")
        menuOpcao = valInt("Insira opção: ")
        match menuOpcao:
            case 1:
                pass
                #sistema_ataque(chamadaInimigo) #pra que se possa retornar pro menu anterior, a função do proximo tem q levar argumentos anteriores
            case 2:
                pudim(chamadaInimigo, txt)
            case _:
                input("Opção inválida. Pressione Enter para voltar... ")
                continue


def pudim(chamadaInimigo, txt = None): #menu do inventario do pudim
    clear()
    while True:
        dotArt('txtes/pudim')
        print(f"Pudim\
            \n------------------\
            \n1 - Checar o Pudim \
            \n2 - Itens do Pudim\
            \n3 - Retornar")
        menuPudim = valInt("Insira opção: ")
        match menuPudim:
            case 1:
                clear()
                dotArt('txtes/pudim')
                print("Pudim - sobrenome: de Limão\
                    \n-----------------------------\
                    \nForça: 3 - Bem forte, para um gatinho\
                    \nAtaque: 5 - Sua espada é sua maior aliada\
                    \nAgilidade: 6 - Jovem e flexível, um felino admiravel")
                if temAmuleto == True:
                    print("Sorte: 10 - Pudim tem certeza que é o gato mais sortudo de Miaudade")
                else:
                    print("Sorte: 8 - Pudim está se sentindo sortudo hoje")
                input()
                continue
            case 2:
                clear()
                print(f"1 - {inventario.espada['nome']}")
                if temChave == True:
                    print("2 - Chave Brilhante")
                if temAmuleto == True:
                    print(f"3 - {inventario.amuleto['nome']}")
                if temFlor == True:
                    print(f"4 - {inventario.flor['nome']}")
                if temPena == True:
                    print(f"5 - {inventario.pena['nome']}")
                if temCristal == True:
                    print(f"6 - {inventario.cristal['nome']}")
                if temMassa == True:
                    print(f"7 - {inventario.massa['nome']}")
                print("Pressione 0 para voltar")
                itemOpcao = valInt("Insira Opção: ")
                clear()
                if itemOpcao == 1:
                    inventario.chamarItem(inventario.espada)
                    continue
                if itemOpcao == 2 and temChave == True:
                    inventario.chamarItem(inventario.chave)
                    continue
                if itemOpcao == 3 and temAmuleto == True :
                    inventario.chamarItem(inventario.amuleto)
                    continue
                if itemOpcao == 4 and temFlor == True:
                    inventario.chamarItem(inventario.flor)
                    continue
                if itemOpcao == 5 and temPena == True:
                    inventario.chamarItem(inventario.pena)
                    continue
                if itemOpcao == 6 and temCristal == True:
                    inventario.chamarItem(inventario.cristal)
                    continue
                if itemOpcao == 7 and temMassa == True:
                    inventario.chamarItem(inventario.massa)
                    continue
                else:
                    continue
            case 3:
                clear()
                menu_luta(chamadaInimigo, txt)
            case _:
                input("Opção inválida. Pressione Enter para voltar... ")
                continue

class inventario:

    def chamarItem(item):
        dotArt(item['txt'])
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
    'nome': 'Soldado Rato',
    'descricao': 'Um grande e forte soldado rato. Parece que não vão muito com a sua cara.',
    'chamada': 'Um Soldado Rato ergue-se na sua frente! Cuidado Pudim!',
    'atk': 4,
    'hp': 30
}
ratão = {
    'nome': 'Ratão',
    'descricao': 'Um ratazana enorme, tanto para cima quanto pros lados. Parece muito perigosa.',
    'chamada': 'O Ratão pisoteia a frente! Cuidado Pudim!',
    'atk': 6,
    'hp': 40
}

ratãoFinal = {
    'nome': 'Ratão: o Grande Rato',
    'descricao': 'O Ratão retorna. Ele parece nervoso e inspirado, sua força é maior do que antes.',
    'chamada': 'O chão treme sob as patas do Ratão! Muito cuidado Pudim!',
    'atk': 10,
    'hp': 80
}

dinoPlanta = {
    'nome': 'Dinoplanta: a Planta Ancestral',
    'descricao': 'Uma planta carnívora de eras antepassadas. Nos tempos antigos, plantas dinossauro alimentavam-se de felinos.',
    'chamada': 'A Planta Ancestral estica suas vinhas! Muito cuidado Pudim!',
    'atk': 7,
    'hp': 50
}

monstroLago = {
    'nome' : 'Monstro Cristalino: o Protetor das Jóias',
    'descricao': 'Um monstro misterioso que se camufla perfeitamente nas cavernas da mina. Extremamente perigoso.',
    'chamada': 'A olhos do monstro brilham o mesmo azul que cintila dos cristais nas suas costas. Muito cuidado Pudim!',
    'atk': 8,
    'hp': 60
}
