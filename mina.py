#mina
import data

#acontecimentos
print("       ______ \n    ___/   ___\_ \n __/.'.__/  _ \_\_ \n/.'___/    | |    \ \n':/   \:'''+-+''':.''. \n           +-+ \n            +-+")
data.animar('\n Entrando em Mina Decadente')
data.sleep(2.0)
data.clear()
data.sleep(1.0)
data.animar('Pudim corre até a Mina nos arredores de Miaudade.\n As lendas sobre os perigos da Mina, há muito tempo abandonada pelos gatos, arrepiam os pelos do felino, enquanto ele adentra a mina.\n Não há sequer uma luz fraca em vista. As paredes da caverna ecoam com os passos leves das patas do Pudim.\n O gato segue bravamente pela mina sombria, seus olhos felinos escaneando minuciosamente através da escuridão porém, nenhum objeto reluzente é encontrado aqui, somente varias e varias placas espalhadas pelos cantos, todas escrito "PERIGO!".')
input()
data.clear()
data.animar('Pudim as ignora e segue em frente, determinado a encontrar o Cristal. Seu caminho é livre, apenas pequenos insetos e animais rastejantes aparecendo no caminho, que se amedrontam ao ver o gato e fogem. De repente, ao tomar uma esquina dentro do labirinto de cavernas da mina ele finalmente avista uma formação de cristais, ilhados no centro de um pequeno lago num grande espaço.')
input()
data.clear()
data.falas('txtes/pudim', 'Pudim', 'Rum... água... por você, Miaudade!')
data.animar('Pudim dá o maior salto de sua vida, passando com sua elegância felina por cima da água. Os cristais em sua frente são bonitos, e brilham com uma luz que ilumina os arredores, porém, ele só precisa de um no momento (talvez ele volte para pegar mais e guardar como brinquedo para uso futuro). Pudim usa sua espada para quebrar um pedaço do cristal.')
input()
data.falas('txtes/cristal', 'Cristal Relusente', 'Pudim pegou Cristal Relusente')
if data.ingredientesFalta == 0:
    data.falas('txtes/pudim', 'Pudim', 'Tudo bem, consegui todos! Agora tenho que voltar para o Miauderijo! Miau!')
else:
    data.falas('txtes/pudim', 'Pudim', f'Tudo bem, Só mais {data.ingredientesFalta} pra pegar! Miau!')
data.animar('Pudim pula de volta ao outro lado, e segue para a saída... até que o chão em baixo de suas patas começa a tremer! Pudim olha para trás e vê...')
input()
data.falas('monstrolago', 'Monstro Cristalino: o Protetor das Jóias', '')
data.animar('O que antes era uma ilha com uma formação de cristais, se ergue do lago e se revela como um grande monstro, com cristais descendo por suas costas!')
input()
data.luta('data.monstrolago')
data.animar('Pudim permanece de pé, como o vitorioso da grande batalha!')
input()
data.animar('Pudim deixa o monstro para trás, se retirando da Mina de uma vez por todas.')
input()
data.chamarMapa()