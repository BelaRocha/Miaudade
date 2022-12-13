##inicio
import sys
import data

#introdução (diálogo)
frase = ' Inúmeros gatinhos dormem silenciosa (e preguiçosamente) no Miauderijo...   Enquanto isso, um felino solitario se levanta'
data.animar(frase)
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

data.animar("(Pressione 'm' para abrir o mapa)")
data.chamarMapaInicial()