#casa misteriosa
import data

#acontecimentos
print("      __________\n   _-'      _-'||'-_ \n_-'______-xxxxxxxxxxx_\n [_[]__[]_[__I-==-I_]\n [_[]__[]_[__]/--\[_]\n [_II__II_[__]|__|[_]")
data.animar('\nentrando em Casa Misteriosa')
data.sleep(2.0)
data.clear()
data.sleep(1.0)
data.animar('Pudim se aproxima da casa misteriosa. Nunca em Miaudade havia ele visto esse lugar, pode ser perigoso.\n Chegar mais perto?')
escolha = int(input('\n1-Sim               2-Não\n            '))
data.clear()
match escolha:
    case 1:
        data.animar('Pudim bate na porta da casa misteriosa... ninguém vem atender. Pudim percebe que a porta estava aberta e entra (sem educação).')
        input()
        data.falas('txtes/pudim', 'Pudim', 'Rummm... que lugar é esse?')
        data.animar('Uma fumaça grossa cobre por inteiro o recinto, dificultando até ver as paredes do lugar.\n Vultos sombrios deixam rastros pelo ambiente esfumaçado e sons estranhos arrepiam até a ponta do rabo do Pudim, que avança cautelosamente.\n Em meio ao breu e toda a fumaça que lacrimeja os olhos do gato,  ele avista um objeto brilhante um pouco mais a frente, que parece atrair não só os olhos mas a mente de Pudim.')
        escolha = int(input('\n1 - Ceder e pegar o objeto           2 - Resistir e voltar\n                  '))
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
                data.animar('Pudim abre os olhos, parece q se passaram horas, ou talvez minutos? Ele percebe, em sua pata, um amuleto estranho, que não estava com ele antes.\n Ele se levanta, e a casa misteriosa, havia desaparecido por completo. Teria sido tudo um sonho?')
                data.falas('txtes/amuleto', '', 'Pudim conseguiu o Amuleto da Sorte!')
            case 2:
                data.animar(' O bom senso de Pudim parece falar mais alto, e ele corre para fora da casa sem olhar para trás. Ele nunca saberá o que era aquilo.')
    case 2:
        data.animar(' Você dá meia volta e vai embora, com o rabinho entre as pernas.')
#abre mapa
data.clear()
data.chamarMapa()
