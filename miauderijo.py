#miauderijo]
import data

#atecimentos
print('   /\   \n  //\\  \n //||\////\  /\   _____ \n  _||////==\//\\ ////==\ \n /==\| |__ |/||\ | | []| \n/====\/===\//||\\/\\\\\\\  \n| TT /=====//||\\==\ \\ \\ \n     |--T--| || |++|_| |_| ')
data.animar('\n Entrando em Miauderijo')
data.sleep(2.0)
data.clear()
data.sleep(1.0)
data.animar('Pudim leva o velho Bola de Pelos até o Miauderijo, onde a dupla se reune com o Sabio Sr. Bigodes')
input()
data.clear()
data.falas('txtes/gatovelho', 'Gato Sábio', ' É muito bom vê-lo saudável, ó grande mago!')
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
data.falas('pudim', 'Pudim', 'Tudo bem Bolinha, diz pra nós, como se livrar daqueles ratos!')
data.falas('txtes/gatovelho', 'Gato Sábio', 'Ei, não chame o grande mago de Bolinha!')
data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Eu tenho um plano, Pudim e Sr. Bigodes! Um feitiço que os levará para longe!')
data.falas('pudim', 'Pudim', 'Ótimo Bolinha, Então faça logo sua magia!')
data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Tudo em seu tempo, Pudim... o feitiço é grande e poderoso, por isso... vou precisar de ingredientes especiais!')
data.falas('pudim', 'Pudim', 'Rum... lá vem.')
data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Pudim, preciso que você recolha para mim os ingredientes mais poderosos dessa cidade!\n\n -A Flor Ancestral na Floresta Macabra\n -O Cristal Reluzente, da Mina Decadente\n -Uma Pena de uma grande ave.\n -E por último, a Massa Sagrada...')
data.falas('pudim', 'Pudim', '...')
data.falas('txtes/gatomago', 'Mago Bola de Pelos', '...')
data.falas('pudim', 'Pudim', 'Ei! E essa tal de massa, você não falou onde que eu encontro essa aí!')
data.falas('txtes/gatomago', 'Mago Bola de Pelos', 'Sinto que não terei a resposta para essa pergunta... mas talvez, o Grande Gato Sábio a tenha?')
data.falas('txtes/gatovelho', 'Gato Sábio', 'Hummm... parece que com a vinda dos ratos, uma figura... estrangeira... construiu uma casa misteriosa perto da Torre\n Um italiano... Pudim, talvez ele possua a massa que procura, mas sinto que não será amigável com nós felinos.')
data.falas('pudim', 'Pudim', 'Miau! Tenho minha missão! Obrigado vovô e Bolinha!')
data.animar('Pudim salta para fora do Miauderijo, voltando à sua aventura.')
input()
data.clear()
#(abre o mapa, agora com todas as áreas liberadas)
data.clear()
data.chamarMapa()

