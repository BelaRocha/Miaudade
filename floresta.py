#area da floresta
import data

data.animar('Pudim adentra a floresta, uma densa vegetação ao seu redor.')
if data.temPena == False:
    print('Ele sente uma vontade repentina de subir uma árvore, mas se controla. É quando ele nota, parado num galho, um pombo distraído!\nDar o bote?')
##1-sim/2-nao
    data.animar('Você pula no pombo e arranca uma pena.')
    data.falas('txtes/pombo', 'Pombo', 'Ei, o que pensa que tá fazendo? Prometo que vou te processar, seu gato imundo!')
    data.animar('O Pombo parece bravo. Ele sai voando para longe.')
    data.falas('txtes/pena', 'Pudim conseguiu a Pena Suja!', '')
    data.temPena == True
    data.animar('Você não faz nada. Parece uma oportunidade desperdiçada.')
if data.temFlor == False:
    data.animar('Pudim continua o seu caminho pela floresta, passando entre as arvores enquanto procura a flor até que encontra um Soldado Rato no caminho!\
        \nEle parece distraido cortando lenha, o que fazer?')
    #(1-ataque\2-passar despercebido)
    data.animar("Você pula no inimigo, o atacando de surpresa!") 
    #luta
    data.animar('...O rato cai derrotado, Pudim segue em frente novamente!') #sucesso
    data.animar('Você tenta se camuflar nas árvores e passar despercebido...')
    data.animar('...Mas Pudim é branco! O rato percebe sua presença e te ataca!') 
    #luta
    data.animar('...E mesmo Pudim sendo branco, o rato é dautônico! Pudim passa de fininho e avança!') #sucesso

    data.animar('Pudim anda por o que parecem horas para suas perninhas curtas de gatinho, até que, num caminho ingrime e escuro, ele vê,\
        \niluminada por um unico feiche de luz que corta pela copa das árvores, a Flor Ancestral! Pudim pula em sua direção, porém!')
        #luta com dinoplanta
    data.animar('A Dinoplanta mítica de lenda cai derrotada de volta ao chão! Você segura a Flor Ancestral em suas patas')
    data.falas('txtes/flor', '(Pudim pegou a Flor Ancestral!)', '')
    data.temFlor = True
    if data.ingredientesFalta == 0:
        data.falas('txtes/pudim', 'Pudim', 'Tudo bem, consegui todos! Agora tenho que voltar para o Miauderijo! Miau!')
    else:
        data.falas('txtes/pudim', 'Pudim', f'Tudo bem, Só mais {data.ingredientesFalta} pra pegar! Miau!')
else:
    data.falas('Rum... o que tô fazendo aqui? Não tenho tempo pra perder!')