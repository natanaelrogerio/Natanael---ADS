#notas = [9,7,7,10,3,9,6,6,2]
#total = notas.count(7)   contando quantas ocorrencias dentro de uma lista
#print(total)

#notas = [9,7,7,10,3,9,6,6,2]
#notas[-1] = 4              alterando ultimo item da lista
#print(notas)

#notas = [9,7,7,10,3,9,6,6,2]
#m=max(notas)                     descobrindo o maior valor em uma lista
#print('O maior número encontrado na lista é o {} !'.format(m))

#notas = [9,7,7,10,3,9,6,6,2]
#ordenada = sorted(notas, reverse=True)   ordenando uma lista decrescente
#print(ordenada)

#notas = [9,7,7,10,3,9,6,6,2]
#soma=sum(notas)
#media=soma / len(notas)
#print(media)

#     Exibindo as palavras dentro de uma tupla e contando as vogais
#palavras = ("banana", "maçã", "laranja", "uva", "abacaxi", "manga", "limão", "pera", "morango", "kiwi")
#for palavra in palavras:
#    print('\n Palavra : {} . Vogais :  '.format(palavra.upper()), end='')
#    for letra in palavra:
#        if letra.lower() in 'aeiou':
#         print(letra.upper(), end='')
"""
from random import randint

print('******************')
print('*****Jo Ken Po****')
print('******************')
print('1 - Pedra ')
print('2 - Papel ')
print('3 - Tesoura')
print('******************')
vitoria = 0
derrota = 0
empate = 0
lista = ['PEDRA','PAPEL','TESOURA']
while True:
    escolha = int(input('Faça sua escolha : (1)Pedra (2)Papel (3)Tesoura (0)Sair :'))
    escolhapc = randint(1, 3)
    print('Você escolheu {} e o computador escolheu {} '.format(lista[escolha-1],lista[escolhapc-1]))
    if escolha == escolhapc:
        empate = empate+1
        print('Deu empate!!!')
    elif escolha == 1 :
        if escolhapc == 2:
            derrota = derrota+1
            print('Você perdeu!!!')
        if escolhapc == 3:
            vitoria = vitoria+1
            print('Você venceu!!!')
    elif escolha == 2 :
        if escolhapc == 1:
            vitoria = vitoria+1
            print('Você venceu!!!')
        if escolhapc == 3:
            derrota = derrota+1
            print('Você perdeu!!!')
    elif escolha == 3 :
        if escolhapc == 1:
            derrota = derrota+1
            print('Você perdeu!!!')
        if escolhapc == 2:
            vitoria = vitoria+1
            print('Você venceu!!!')
    elif escolha == 0:
        print('Você venceu : ' , vitoria)
        print('Você perdeu : ', derrota)
        print('Vocês empataram : ' , empate)
        break
"""
"""
produto=0
qte=0
desc=0

print('**********************************')
print('Bem vindo a loja do Natanael Rosa') #exibindo nome da loja
print('**********************************')
produto = float(input('Digite o valor do produto:')) #recebendo dados 
qte = int(input('Digite a quantidade do produto:'))
if qte < 10: #início das condicionais
    print('O valor total é R${} . (não houve desconto)'.format(produto*qte))
elif 9 < qte < 100:
    desc=0.05
    print('O valor total sem desconto é R${} .'.format(produto * qte))
    print('O valor total com desconto é R${:.2f} . (desconto de 5% aplicado)'.format((produto * qte)-((produto*qte)*desc)))
elif 99 < qte < 999:
    desc = 0.1
    print('O valor total sem desconto é R${} .'.format(produto * qte))
    print('O valor total com desconto é R${:.2f} . (desconto de 10% aplicado)'.format((produto * qte) - ((produto * qte) * desc)))
else :
    desc = 0.15
    print('O valor total sem desconto é R${} .'.format(produto * qte))
    print('O valor total com desconto é R${:.2f} . (desconto de 15% aplicado)'.format((produto * qte) - ((produto * qte) * desc)))
print('Volte sempre')
"""
"""
def confirmação(): # função chamada para descrever o nome do produto pedido pelo usuário
    if escolha == '100':
        print('Você adicionou Hot dog à sua cesta')
    elif escolha == '101':
        print('Você adicionou Hot duplo à sua cesta')
    elif escolha == '102':
        print('Você adicionou X-egg à sua cesta')
    elif escolha == '103':
        print('Você adicionou X-salada à sua cesta')
    elif escolha == '104':
        print('Você adicionou X-bacon à sua cesta')
    elif escolha == '105':
        print('Você adicionou X-tudo à sua cesta')
    elif escolha == '200':
        print('Você adicionou Refrigerante lata à sua cesta')
    elif escolha == '201':
        print('Você adicionou Chá gelado à sua cesta')

#menu = {100: 'Hot dog simples ', 101: 'Hot Dog duplo', 102: 'X-Egg' , 103: 'X-Salada', 104: 'X-Bacon', 105: 'X-Tudo', 200: 'Refrigerante Lata', 201: 'Chá Gelado'}
cesta = []

print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==')
print('     Bem vindo à lanchonete do Natanael Rosa') #exibindo nome da loja
print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==')
print('--------------------Cardápio----------------------')
print('==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==')
print('''| Código |          Descrição          | Valor |
|   100  |       Hot dog simples       |  9,00 |
|   101  |       Hot Dog duplo         | 11,00 |
|   102  |       X-Egg                 | 12,00 |
|   103  |       X-Salada              | 12,00 |
|   104  |       X-Bacon               | 14,00 |
|   105  |       X-Tudo                | 17,00 |
|   200  |       Refrigerante Lata     |  5,00 |
|   201  |       Chá Gelado            |  4,00 |
''')

while True: # iniciando coleta de dados
    escolha=str(input('Entre com o código desejado:>>>'))

    if escolha != '100' and escolha != '101' and escolha != '102' and escolha != '103' and escolha != '104' and escolha != '105' and escolha != '200' and escolha != '201':
        print('produto não existe , tente novamente:') # caso usuario digite numero diferente do menu
        continue
    else :
        confirmação() #chamando a função para exibir produto escolhido
        cesta.append(escolha)
        a=0
        while a == 0:
            while True:
                n = int(input('''Deseja pedir algo mais ?
                    | 1 | Sim 
                    | 0 | Não 
                    >>>'''))
                if n == 1 :
                    a=1
                    break
                elif n == 0 :
                    a=3
                    break
                else :
                    print('Opção inválida ') #mensagem de erro por opção inválida
                    continue
    if a == 3:
        break

total100 = cesta.count('100')
total101 = cesta.count('101')
total102 = cesta.count('102')
total103 = cesta.count('103') #contando quantas vezes cada produto foi selecionado
total104 = cesta.count('104')
total105 = cesta.count('105')
total200 = cesta.count('200')
total201 = cesta.count('201')
if total100 > 0:
    total100 = total100 * 9
if total101 > 0:
    total101 = total101 * 11
if total102 > 0:
    total102 = total102 * 12   # calculando valor total dos produtos
if total103 > 0:
    total103 = total103 * 12
if total104 > 0:
    total104 = total104 * 14
if total105 > 0:
    total105 = total105 * 17
if total200 > 0:
    total200 = total200 * 5
if total201 > 0:
    total201 = total201 * 4

print('O total da sua compra é R$ {:.2f} . '.format(total100+total101+total102+total103+total104+total105+total200+total201))
print('Seu pedido foi finalizado com sucesso!!!')

print(cesta)
"""


"""
try:
    # Código que pode gerar exceções
    x = int(input("Digite um número: "))
    resultado = 10 / x
except ZeroDivisionError:
    # Tratamento específico para divisão por zero
    print("Não é possível dividir por zero.")
except ValueError:
    # Tratamento específico para entrada inválida
    print("Digite um número válido.")"""



"""
print('Bem vindo a Natanael Rosa Translog - Eficiência e qualidade!')
def dimensaoObjeto ():
    try:

        alt = int(input('Digite a altura do objeto em CM:>>>'))
        comp = int(input('Digite o comprimento do objeto em CM:>>>'))
        larg = int(input('Digite a largura do objeto em CM:>>>'))
        vol = (alt * comp * larg)
        print('O volume total do objeto é : {} cm³ . '.format(vol))
        if vol >= 100000:
            print('Este volume ultrapassa o nosso limite!')
            while True :
                resp = int(input('''Deseja tentar um novo objeto?
                                 |1| SIM
                                 |2| NAO>>>'''))
                if resp == 1:
                    return dimensaoObjeto()
                elif resp == 2:
                    print('Foi um prazer atende-lo , Volte Sempre!')
                    exit()
                else:
                    print('Opção inválida!')

        elif vol < 1000 :
            vol2 = vol*10
            return vol2

        elif vol >=1000 and vol < 10000:
            vol2 = vol*20
            return vol2

        elif vol >= 10000 and vol < 30000:
            vol2 = vol * 30
            return vol2

        elif vol >= 30000 and vol < 100000:
            vol2 = vol * 50
            return vol2

    except ValueError:
        # Tratamento específico para entrada inválida
        print("Você digitou um valor inválido , reinicie o programa!")

def pesoObjeto ():
    while True:
        try:
            peso = float(input('Digite o peso do objeto em KG:>>>'))
            mult=0
            if peso <= 0.1:
                mult=1
                peso2 = peso * mult
                return peso2
                break
            elif peso > 0.1 and peso < 1:
                mult=1.5
                peso2 = peso * mult
                return peso2
                break
            elif peso >= 1 and peso < 10:
                mult=2
                peso2 = peso * mult
                return peso2
                break
            elif peso >= 10 and peso < 30:
                mult=3
                peso2 = peso * mult
                return peso2
                break
            elif peso >= 30:
                print('Peso fora das normas da empresa !')
                continue
#            peso2 = peso * mult
#            return peso2
#            break
        except ValueError:
            # Tratamento específico para entrada inválida
            print("Você digitou um valor inválido , tente novamente!")

def rotaObjeto ():
    print('''| SIGLA |          ROTA           
|   RS   |       De Rio de Janeiro até São Paulo      
|   SR   |       De São Paulo até Rio de Janeiro         
|   BS   |       De Brasília até São Paulo                  
|   SB   |       De São Paulo até Brasília              
|   BR   |       De Brasília até Rio de Janeiro    
|   RB   |       De Rio de Janeiro até Brasília                     
''')
    while True:
        rota = str(input('Digite a sigla referente à sua rota :>>>'))
        if rota.upper() == 'SR' or rota.upper() == 'RS':
            multirota = 1

            break
        elif rota.upper() == 'BS' or rota.upper() == 'SB':
            multirota = 1.2
            break
        elif rota.upper() == 'BR' or rota.upper() == 'RB':
            multirota = 1.5
            break
        elif rota.upper() not in 'BR' and rota.upper() not in 'RB' and rota.upper() not in 'BS' and rota.upper() not in 'SB' and rota.upper() not in 'RS' and rota.upper() not in 'SR':
            print('Sigla não reconhecida, tente novamente!')
"""
"""
print('Bem vindo a Natanael Rosa Translog - Eficiência e qualidade!')
print('Vamos calcular o valor do frete desejado:')
def DimensaoObjeto():
    while True:
        try:
            tamanho = int(input("Qual o comprimento em CM: "))
            altura = int(input("Qual a altura em CM: "))
            largura = int(input("Qual a largura em CM: "))
            break
        except ValueError:
            print("Digite apenas números inteiros. Tente novamente.")

    volume = tamanho * altura * largura
    print("O volume do objeto é:", volume, "cm³")

    if volume < 1000:
        volume2 = volume * 10
        return volume2
    elif 1000 <= volume < 10001:
        volume2 = volume * 20
        return volume2
    elif 10001 <= volume < 30001:
        volume2 = volume * 30
        return volume2
    elif 30001 <= volume < 100000:
        volume2 = volume * 50
        return volume2
    else:
        while True:
            resposta = input("Este volume ultrapassa os limites aceitados. Digite 1 para iniciar o programa novamente ou 0 para sair: ")
            if resposta == '1':
                return DimensaoObjeto()
            elif resposta == '0':
                return None
            else:
                print("Opção inválida. Tente novamente.")

def PesoObjeto():
    while True:
        try:
            peso = float(input("Qual o peso do objeto em kg: "))
            break
        except ValueError:
            print("Digite apenas números. Tente novamente.")

    if peso == 0.1:
        mult = 1
    elif 0.1 < peso < 1:
        mult = 1.5
    elif 1 <= peso < 10:
        mult = 2
    elif 10 <= peso < 30:
        mult = 3
    elif peso >= 30:
        print("O produto ultrapassa os limites de peso aceitos.")
        return None

    peso2 = peso * mult
    return peso2

def RotaEscolhida():
    rotas = {
        'RS': {'valor': 1},
        'SR': {'valor': 1},
        'BS': {'valor': 1.2},
        'SB': {'valor': 1.2},
        'BR': {'valor': 1.5},
        'RB': {'valor': 1.5},
    }

    while True:
        escolha = input('''| SIGLA |          ROTA           
|   RS   |       De Rio de Janeiro até São Paulo      
|   SR   |       De São Paulo até Rio de Janeiro         
|   BS   |       De Brasília até São Paulo                  
|   SB   |       De São Paulo até Brasília              
|   BR   |       De Brasília até Rio de Janeiro    
|   RB   |       De Rio de Janeiro até Brasília    
>>>                 
''' ).upper()
        if escolha in rotas:
            return escolha, rotas[escolha]['valor']
        else:
            print("Sigla inválida. Tente novamente.")


volume2 = DimensaoObjeto()
peso2 = PesoObjeto()
sigla, valor_rota = RotaEscolhida()

total = volume2 * peso2 * valor_rota

print("Valor total a ser pago pelo cliente:", total)
print("Muito obrigado!")
print(peso2)
print(volume2)
print(sigla)
"""
#---------Inicio das variáveis globais -----------
lista_produto = []
codigo_produto = 0

#---------Inicio das variáveis globais -----------

#---------Início de cadastrar produtos() -----------
def cadastrar_produtos(codigo):
    print('Bem-vindo ao menu de Cadastro de produtos')
    print('Código do produto : {} '. format(codigo))
    nome = input('Entre com o NOME do protudo:')
    fabricante = input('Entre com o FABRICANTE do protudo:')
    valor = float(input('Entre com PREÇO(R$) do protudo:'))
    dicionario_produto={'codigo' : codigo , 'nome' : nome , 'fabricante' : fabricante, 'valor' : valor}
    lista_produto.append(dicionario_produto.copy())
#---------Início de consultar produtos() -----------
def consultar_produtos():
    print('Bem-vindo ao menu de Consulta de produtos')
    while True:

        menu_consultar = input('''Escolha a opção desejada !           
    |   1   |       Consultar TODOS os produtos    
    |   2   |       Consultar produto por Código        
    |   3   |       Consultar produto por FABRICANTE                 
    |   4   |       Retornar ao MENU principal              
    >>>''')
        if menu_consultar == '1':
            for produto in lista_produto:
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                for key , value in produto.items():
                    print('{}: {} ' .format(key,value))
                print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        elif menu_consultar == '2':
            valor_desejado = input('Entre com o Código desejado:>>>')
            for produto in lista_produto:
                if produto['codigo'] == valor_desejado:
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    for key, value in produto.items():
                        print('{}: {} '.format(key, value))
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        elif menu_consultar == '3':
            print('teste')
        elif menu_consultar == '4':
            print('Voltando....')
            return
        else:
            print('Opção inválida . Tente novamente !')

#---------Início de remover produtos() -----------
def remover_produtos():
    print('Bem-vindo ao menu de Remover  produtos')

#---------Início de main() -----------
print('Seja bem_vindo a Mercearia do Natanael Rosa')
while True:

    menu_principal = input('''Escolha a opção desejada !           
|   1   |       Cadastrar produto     
|   2   |       Consultar produto(s)        
|   3   |       Remover produto                 
|   4   |       Sair              
>>>''')
    if menu_principal == '1':
        codigo_produto = codigo_produto +1
        cadastrar_produtos(codigo_produto)
    elif menu_principal == '2' :
        consultar_produtos()
    elif menu_principal == '3' :
        remover_produtos()
    elif menu_principal == '4' :
        break
    else:
        printi('Opção inválida . Tente novamente !')



#---------Fim de main() -----------




