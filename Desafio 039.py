# Bibliotecas usadas
import time
import random

# Estética
print('{:=^40}'.format('Desafio 39'))
print('{:80}'.format(40 * '='))

# Interação
apr = input('')
nome = input('Olaaaa!!!!! Eu me chamo ASCE, como é seu nome ?  ').strip().upper()

# Correção no nome, agora verifica corretamente
if nome == 'LUIS' or nome == 'LUÍS':  # Corrigido para comparar corretamente
    print('Iaew cara, suavidade ?')
elif nome == 'KAROL' or nome == 'ANE':  # Corrigido para comparar corretamente
    print('Fala guria')
else:
    print('É um prazer em te conhecer!!!!')

# Lista de fases
estoubem = [  # Frases felizes
    'Se você está bem, eu estou bem!',
    'Que sua felicidade contagie a todos como me contageou ;D',
    'Eu estou feliz por você estar feliz.',
    'Que bom que você está bem!'
]

estoumal = [  # Frases de encorajamento
    "Não desista, você é capaz de tudo!",
    "Cada desafio é uma oportunidade para crescer.",
    "Acredite em você, pois você tem muito potencial!",
    "Continue lutando, o sucesso está perto!"
]

# Pergunta sobre como o usuário está se sentindo
emoção = input('Você está bem? ').strip().upper()

# Enquanto a entrada não for 'SIM' ou 'NÃO', pede novamente
while emoção not in ['SIM', 'NÃO']:
    emoção = input('Eu sou meio binário, vai ter que escolher entre SIM e NÃO :D : ').strip().upper()

if emoção == 'SIM':
    frase = print(random.choice(estoubem))
else:
    frase = print(random.choice(estoumal))

time.sleep(3)

duvida = input('Aprendi uma nova utilidade. Agora consigo checar se já está se\naproximando a data do seu alistamento Militar. Quer ver?: ').strip().upper()

# Enquanto a entrada não for 'SIM', 'NÃO' ou 'QUERO', pede novamente
while duvida not in ['SIM', 'NÃO', 'QUERO']:
    duvida = input('Eu sou meio binário, vai ter que escolher entre SIM e NÃO :D : ').strip().upper()

time.sleep(2)

if duvida == 'SIM':
    print('Vamos nessa!!!!')
elif duvida == 'QUERO':
    print('Vamos nessa!!!!!')
else:
    print('Ok, outro dia então...')
    exit()

time.sleep(3)

while True:
    sexo = input('Você tem o sexo masculino ou feminino ?: ').upper().strip()

    # Correção para aceitar apenas 'MASCULINO' ou 'FEMININO'
    while sexo not in ['MASCULINO', 'FEMININO']:
        sexo = input('Escolha entre masculino ou feminino: ').strip().upper()

    if sexo == 'FEMININO':
        print('Se livrou dessa em kskskskskskskksskks.')
        

    else:
        while True:
            try:
                pergunta = int(input('Qual foi o ano do seu nascimento?: '))
                break
            except ValueError:
                print('Isso não parece com o ano')

        ano = 2025 - pergunta
        idade = 18 - ano
        anoal = 2025 + idade
        multa = -(idade) * 10
        anoc = 18  # Ajuste da variável 'anoc' para um valor correto

        if ano == 18:
            print('2025 é o ano do seu alistamento, pois você já tem {}'.format(ano))
        elif ano < anoc:
            print('Seu alistamento ocorrerá dentro de {} ano(s), mais precisamente em {}, pois você só tem {}'.format(idade, anoal, ano))
        elif ano > anoc:
            print('Você já passou do período obrigatório. Isso acarretará no pagamento de uma multa no valor de\n R$10 por ano após da data correta, totalizando um valor de R${}'.format(multa))

        time.sleep(2)

    # Pergunta se o usuário deseja repetir o código
    replay = input('Gostaria de tentar de novo? (Sim/Não): ').strip().upper()

    # Valida a entrada para aceitar apenas 'SIM' ou 'NÃO'
    while replay not in ['SIM', 'NÃO']:
        time.sleep(2)
        replay = input('É que eu sou meio binário, vai ter que escolher entre Sim e Não :D: ').strip().upper()

    # Sai do loop principal se a resposta não for 'SIM'
    if replay != 'SIM':
        time.sleep(2)
        print('Espero ter sido útil a você! Até a próxima :D')
        print('{:=^80}'.format(''))
        print('{:=^80}'.format(''))
        break

    # Mensagem opcional ao continuar
    print('Reiniciando o código...\n')








