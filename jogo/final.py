#ato final
import data

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