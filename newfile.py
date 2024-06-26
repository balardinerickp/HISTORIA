Aqui está o código corrigido:

```python
from colorama import Fore, Style

# Perguntas e respostas
pergunta1 = '1) O que foi a Revolução Industrial?'
pergunta2 = '2) Onde começou a Revolução Industrial?'
pergunta3 = '3) O que foi a Revolução Russa?'
pergunta4 = '4) Quando aconteceu a Revolução Russa?'
pergunta5 = '5) Quando o Brasil virou uma república?'
pergunta6 = '6) O que é a Constituição de 1988?'
pergunta7 = '7) O que é herança cultural?'
pergunta8 = '8) Como preservamos a herança cultural?'
pergunta9 = '9) O que é patrimônio material?'
pergunta10 = '10) O que é patrimônio imaterial?'
pergunta11 = '11) O que são formas de representatividade cultural?'
pergunta12 = '12) Pode dar um exemplo de representatividade cultural?'
pergunta13 = '13) O que são estados nacionais?'
pergunta14 = '14) Quando começaram a se formar estados nacionais?'
pergunta15 = '15) O que é um estado-nação?'
pergunta16 = '16) O que é um governo?'
pergunta17 = '17) O que é sentimento nacional?'
pergunta18 = '18) Quem é José Murilo de Carvalho?'
pergunta19 = '19) O que é identidade cultural?'
pergunta20 = '20) O que são processos civilizatórios?'
pergunta21 = '21) O que são disputas territoriais?'
pergunta22 = '22) Pode dar um exemplo de disputa territorial?'
pergunta23 = '23) O que é individual?'
pergunta24 = '24) O que é coletivo?'
pergunta25 = '25) O que é a ONU?'
pergunta26 = '26) Quando foi criada a ONU?'
pergunta27 = '27) O que é descolonização?'
pergunta28 = '28) Por que a descolonização é importante?'

resposta1 = f"{Fore.GREEN}Foi quando máquinas começaram a ser usadas para produzir coisas.{Style.RESET_ALL}"
resposta2 = f"{Fore.GREEN}Na Inglaterra.{Style.RESET_ALL}"
resposta3 = f"{Fore.GREEN}Foi quando o povo derrubou o czar e começou o governo comunista.{Style.RESET_ALL}"
resposta4 = f"{Fore.GREEN}Em 1917.{Style.RESET_ALL}"
resposta5 = f"{Fore.BLUE}Em 1889.{Style.RESET_ALL}"
resposta6 = f"{Fore.BLUE}É a lei principal do Brasil que garante a democracia.{Style.RESET_ALL}"
resposta7 = f"{Fore.YELLOW}São costumes e tradições passados de geração em geração.{Style.RESET_ALL}"
resposta8 = f"{Fore.YELLOW}Com museus e educação.{Style.RESET_ALL}"
resposta9 = f"{Fore.MAGENTA}São coisas físicas, como prédios e monumentos.{Style.RESET_ALL}"
resposta10 = f"{Fore.MAGENTA}São tradições e festas populares.{Style.RESET_ALL}"
resposta11 = f"{Fore.CYAN}São maneiras de mostrar e valorizar culturas diferentes.{Style.RESET_ALL}"
resposta12 = f"{Fore.CYAN}Festas tradicionais e música folclórica.{Style.RESET_ALL}"
resposta13 = f"{Fore.RED}São países com governo próprio e fronteiras definidas.{Style.RESET_ALL}"
resposta14 = f"{Fore.RED}No século XIX.{Style.RESET_ALL}"
resposta15 = f"{Fore.GREEN}É um país com seu próprio governo.{Style.RESET_ALL}"
resposta16 = f"{Fore.GREEN}É a organização que administra um estado-nação.{Style.RESET_ALL}"
resposta17 = f"{Fore.BLUE}É o orgulho e a identidade que as pessoas têm pelo seu país.{Style.RESET_ALL}"
resposta18 = f"{Fore.BLUE}Um historiador brasileiro que estudou esse tema.{Style.RESET_ALL}"
resposta19 = f"{Fore.YELLOW}É o conjunto de características que identificam um grupo.{Style.RESET_ALL}"
resposta20 = f"{Fore.YELLOW}São mudanças e evoluções nas sociedades ao longo do tempo.{Style.RESET_ALL}"
resposta21 = f"{Fore.MAGENTA}São conflitos entre países ou grupos por causa de terras.{Style.RESET_ALL}"
resposta22 = f"{Fore.MAGENTA}Conflitos na fronteira entre Índia e Paquistão.{Style.RESET_ALL}"
resposta23 = f"{Fore.CYAN}Algo que pertence a uma pessoa só.{Style.RESET_ALL}"
resposta24 = f"{Fore.CYAN}Algo que pertence a um grupo de pessoas.{Style.RESET_ALL}"
resposta25 = f"{Fore.RED}É uma organização que promove a paz e a cooperação entre países.{Style.RESET_ALL}"
resposta26 = f"{Fore.RED}Em 1945.{Style.RESET_ALL}"
resposta27 = f"{Fore.GREEN}É quando um país deixa de ser controlado por outro.{Style.RESET_ALL}"
resposta28 = f"{Fore.GREEN}Para que os países possam ser independentes e se governar.{Style.RESET_ALL}"

# Imprime as perguntas
print(pergunta1)
print(pergunta2)
print(pergunta3)
print(pergunta4)
print(pergunta5)
print(pergunta6)
print(pergunta7)
print(pergunta8)
print(pergunta9)
print(pergunta10)
print(pergunta11)
print(pergunta12)
print(pergunta13)
print(pergunta14)
print(pergunta15)
print(pergunta16)
print(pergunta17)
print(pergunta18)
print(pergunta19)
print(pergunta20)
print(pergunta21)
print(pergunta22)
print(pergunta23)
print(pergunta24)
print(pergunta25)
print(pergunta26)
print(pergunta27)
print(pergunta28)

s = True

while s:
    rnum = input('Digite o número da pergunta que você quer saber: ')

    if rnum == "1":
        print(pergunta1)
        print(resposta1)
    elif rnum == "2":
        print(pergunta2)
        print(resposta2)
    elif rnum == "3":
        print(pergunta3)
        print(resposta3)
    elif rnum == "4":
        print(pergunta4)
        print(resposta4)
    elif rnum == "5":
        print(pergunta5)
        print(resposta5)
    elif rnum == "6":
        print(pergunta6)
        print(resposta6)
    elif rnum == "7":
        print(pergunta7)
        print(resposta7)
    elif rnum == "8":
        print(pergunta8)
        print(resposta8)
    elif rnum == "9":
        print(pergunta9)
        print(resposta9)
    elif rnum == "10":
        print(pergunta10)
        print(resposta10)
    elif rnum == "11":
        print(pergunta11)
        print(resposta11)
    elif rnum == "12":
        print(pergunta12)
        print(resposta12)
    elif rnum == "13":
        print(pergunta13)
        print(resposta13)
    elif rnum == "14":
        print(pergunta14)
        print(resposta14)
    elif rnum == "15":
        print(pergunta15)
        print(resposta15)
    elif rnum == "16":
        print(pergunta16)
        print(resposta16)
    elif rnum == "17":
        print(pergunta17)
        print(resposta17)
    elif rnum == "18":
        print(pergunta18)
        print(resposta18)
    elif rnum == "19":
        print(pergunta19)
        print(resposta19)
    elif rnum == "20":
        print(pergunta20)
        print(resposta20)
    elif rnum == "21":
        print(pergunta21)
        print(resposta21)
    elif rnum == "22":
        print(pergunta22)
        print(resposta22)
    elif rnum == "23":
        print(pergunta23)
        print(resposta23)
    elif rnum == "24":
        print(pergunta24)
        print(resposta24)
    elif rnum == "25":
        print(pergunta25)
        print(resposta25)
    elif rnum == "26":
        print(pergunta26)
        print(resposta26)
    elif rnum == "27":
        print(pergunta27)
        print(resposta27)
    elif rnum == "28":
        print(pergunta28)
        print(resposta28)
    elif rnum == '101':
        s = False
    else:
        print('O número digitado não corresponde a nenhuma pergunta, tente novamente.')
```