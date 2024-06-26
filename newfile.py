# Perguntas e respostas
perguntas = [
    '1) O que foi a Revolução Industrial?',
    '2) Onde começou a Revolução Industrial?',
    '3) O que foi a Revolução Russa?',
    '4) Quando aconteceu a Revolução Russa?',
    '5) Quando o Brasil virou uma república?',
    '6) O que é a Constituição de 1988?',
    '7) O que é herança cultural?',
    '8) Como preservamos a herança cultural?',
    '9) O que é patrimônio material?',
    '10) O que é patrimônio imaterial?',
    '11) O que são formas de representatividade cultural?',
    '12) Pode dar um exemplo de representatividade cultural?',
    '13) O que são estados nacionais?',
    '14) Quando começaram a se formar estados nacionais?',
    '15) O que é um estado-nação?',
    '16) O que é um governo?',
    '17) O que é sentimento nacional?',
    '18) Quem é José Murilo de Carvalho?',
    '19) O que é identidade cultural?',
    '20) O que são processos civilizatórios?',
    '21) O que são disputas territoriais?',
    '22) Pode dar um exemplo de disputa territorial?',
    '23) O que é individual?',
    '24) O que é coletivo?',
    '25) O que é a ONU?',
    '26) Quando foi criada a ONU?',
    '27) O que é descolonização?',
    '28) Por que a descolonização é importante?'
]

respostas = [
    "Foi quando máquinas começaram a ser usadas para produzir coisas.",
    "Na Inglaterra.",
    "Foi quando o povo derrubou o czar e começou o governo comunista.",
    "Em 1917.",
    "Em 1889.",
    "É a lei principal do Brasil que garante a democracia.",
    "São costumes e tradições passados de geração em geração.",
    "Com museus e educação.",
    "São coisas físicas, como prédios e monumentos.",
    "São tradições e festas populares.",
    "São maneiras de mostrar e valorizar culturas diferentes.",
    "Festas tradicionais e música folclórica.",
    "São países com governo próprio e fronteiras definidas.",
    "No século XIX.",
    "É um país com seu próprio governo.",
    "É a organização que administra um estado-nação.",
    "É o orgulho e a identidade que as pessoas têm pelo seu país.",
    "Um historiador brasileiro que estudou esse tema.",
    "É o conjunto de características que identificam um grupo.",
    "São mudanças e evoluções nas sociedades ao longo do tempo.",
    "São conflitos entre países ou grupos por causa de terras.",
    "Conflitos na fronteira entre Índia e Paquistão.",
    "Algo que pertence a uma pessoa só.",
    "Algo que pertence a um grupo de pessoas.",
    "É uma organização que promove a paz e a cooperação entre países.",
    "Em 1945.",
    "É quando um país deixa de ser controlado por outro.",
    "Para que os países possam ser independentes e se governar."
]

# Imprime as perguntas
for pergunta in perguntas:
    print(pergunta)

s = True

while s:
    rnum = input('Digite o número da pergunta que você quer saber (ou 101 para sair): ')
    
    if rnum.isdigit():
        rnum = int(rnum)
        if 1 <= rnum <= 28:
            print(perguntas[rnum - 1])
            print(respostas[rnum - 1])
        elif rnum == 101:
            s = False
        else:
            print('O número digitado não corresponde a nenhuma pergunta, tente novamente.')
    else:
        print('Por favor, digite um número válido.')
