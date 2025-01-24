#frase = f'\n\nO python é uma linguagem de programação top ne?\n ou nao?\n' \
#'\tmultiparadigma' \
#'\tinterpretada' \
#'\torientada a objetos' \
#'\tfuncional' \
#'\tprocedural' \
#'\trefletiva\n' \
#'\ncom uma tipagem boa ou ruim ? ' \
#'boa, comparada com typescript'\
#'e ruim comparada com quais mais outras ? \n\n'\
#
#i = 0
#qtd_maisvezes = 0
#apareceu_mais = 0
#while i < len(frase):
#    letra_atual = frase[i]
#    apareceu = frase.count(letra_atual)
#
#    print(letra_atual, apareceu)
#    i += 1

frase = 'O Python é bom para quais areas de infraestrutura?'\
'para automação de tarefas'\
'para desenvolvimento web' \
'para desenvolvimento de jogos'\
'como pode ser importante em cybersecurity?'\
'apps de cybersecurity ?'\



i = 0
n = 0
l = ''

print(len(frase))

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    n_atual = frase.count(letra_atual)

    if n < n_atual:
        n = n_atual
        l = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{l}" que apareceu '
    f'{n}x'
)