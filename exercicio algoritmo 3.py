print("Seja bem vindo ao terceiro exercicio de Lucas Gabriel Moreira dos Santos")


def escolha_servico ():
   global produto  #aqui eu sofri bastante pois não estava conseguindo acertar a questão de escopo global e local
   while(True):
        print('Escolha um serviço: ')
        print('Digitalização(dig) R$1,10,')
        print('Impressão colorida(ico) R$1,00,')
        print('Impressão preto e branco(ipb) R$0,40,')
        print('Fotocópia(fot) R$0,20.')
        servico = input('')
        if (servico == 'dig'):
          produto = 1.10
          break
        elif (servico == 'ico'):
          produto = 1.00
          break
        elif (servico == 'ipb'):
          produto = 0.40
          break
        elif (servico == 'fot'):
          produto = 0.20
          break
        else:
          print('Serviço invalido requisitado, por favor tente novamente.')
          continue

def num_pagina():
   global paginas
   global total_paginas
   global desconto
   global total_desconto
   while(True):
      try:
         paginas = int(input('Quantas páginas deseja imprimir?  '))
         if (paginas < 20):
            desconto = paginas - 0  #sei que poderia só excluir essa linha, mas sinto que ficaria vago parecendo que esqueceu de colocar o desconto
            total_paginas = paginas * produto
            break
         elif (paginas >= 20 and paginas < 200):
            total_paginas = paginas * produto
            desconto = total_paginas * 0.15
            total_desconto = total_paginas - desconto #achei mais facil colocar a soma do desconto dentro da função
            break
         elif (paginas >= 200 and paginas < 2000):
            total_paginas = paginas * produto
            desconto = total_paginas * 0.20
            total_desconto = total_paginas - desconto
            break
         elif (paginas >= 2000 and paginas < 20000):
            total_paginas = paginas * produto
            desconto = total_paginas * 0.25
            total_desconto = total_paginas - desconto
            break
         elif (paginas >= 20000):
            print('Pedido com valor acima do permitido, por favor tente novamente')
            continue

      except ValueError:
         print('Valor inválido, por favor tente novamente.')
         continue

def servico_extra():
   global adicional
   while(True):
      try:
        print('Deseja adicional? ') #talvez esses prints sejam desnecessarios porém achei valido colocar uma explicação para melhor aparencia do código
        print('digite 1 para encadernação simples(R$15,00)')
        print('digite 2 para encadernação capa dura(R$40,00)')
        print('digite 0 para encerrar o pedido')
        escolha_adicional = int(input())
        if (escolha_adicional == 1):
          adicional = 15
          break
        elif (escolha_adicional == 2):
          adicional = 40
          break
        elif (escolha_adicional == 0):
          adicional = 0
          break
        else:  #essa parte com else e except achei redundante, porém preferi deixar mesmo que acabe perdendo algo na avaliação, pois o exercicio pedia a utilização do excepet mesmo que o else esteja ali
          print('Adicional invalido, por favor tente novamente')
          continue
      except ValueError:
         print('Valor invalido, por favor tente novamente')
         continue


escolha_servico()
num_pagina()
servico_extra()
#teste print(produto)
#teste print(total_paginas)
#teste print(desconto)
#teste print(total_desconto)
#teste print(adicional)
total = total_desconto + adicional #Fiquei em duvida se tinha que ser exatamente igual ao enunciado mas preferi resolver dessa forma
print(f'O valor final do seu pedido foi R${total:.2f} ({produto} X {paginas} - {desconto:.2f} + {adicional})') #copiei a logica do exemplo do docx porém achei valido colocar o valor de desconto também