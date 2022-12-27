#casa de italiano
import data

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
    data.chamarLuta(data.italiano)
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