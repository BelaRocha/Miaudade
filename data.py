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

def falas(*txt, nome, fala):
    clear()
    dotArt(txt)
    print(f"{nome}")
    animar(fala)
    input()
    clear()
#menus-------------------------------------------------------------------------------------------------------------------------

def chamarMapaInicial():
    mapaTxt = open("txtes\mapainicial.txt", 'r', encoding='utf-8')
    print(mapaTxt.read())
    mapaOpcao = int(input())
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

def menu_inimigo(nomeInimigo): #menu principal quando começam encontros com inimigos
    while True:
        print(f"O {nomeInimigo} aparece! OwO\
        \n----------------------------------\
        \n*opções aq*\
        \n1-Atacar ÒwÓ\
        \n2-Tentar passar despercebido UwU\
        \n3-Checar Inventario\
        \n..4...etc")
        menuOpcao = valInt("**Insira opção: ")
        match menuOpcao:
            case 1:
                pass
                #sistema_ataque(nomeInimigo) #pra que se possa retornar pro menu anterior, a função do proximo tem q levar argumentos anteriores
            case 2:
                pass
                #sistema_pesinho(nomeInimigo)
            case 3:
                menu_inventario(nomeInimigo)
            #case x:
            case _:
                input("Opção inválida. Pressione Enter para voltar... ")
                continue

def menu_inventario(nomeInimigo): #menu do inventario do pudim
    while True:
        print(f"Pudim\
            \n------------------\
            \n*opções aq*\
            \n1-Checar no Pudim \
            \n2-Itens do Pudim\
            \n3-Objetivo Atual\
            \n4-Retornar\
            \n..5...etc")
        menuInv = valInt("**Insira opção: ")
        match menuInv:
            case 1:
                print("aq vai os status do pudim**")
            case 2:
                print("aq vai os itens do pudim***")
            case 3:
                print("mostrar objetivo atual do pudimm***")
            case 4:
                clear()
                menu_inimigo(nomeInimigo)
            #case x:
            case _:
                input("Opção inválida. Pressione Enter para voltar... ")
                continue
            
def inventario():
    espada = {
        'nome':'Espada Velha',
        'descrição':'Uma espada enferrujada e antiga.'
    }

#mapa

