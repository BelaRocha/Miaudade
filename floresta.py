#area da floresta
import data

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
            if data.ingredientesFalta == 0:
                data.falas('txtes/pudim', 'Pudim', 'Tudo bem, consegui todos! Agora tenho que voltar para o Miauderijo! Miau!')
            else:
                data.falas('txtes/pudim', 'Pudim', f'Tudo bem, Só mais {data.ingredientesFalta} pra pegar! Miau!')
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
