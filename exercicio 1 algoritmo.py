print("Seja bem vindo ao primeiro exercicio de Lucas Gabriel Moreira dos Santos")


compras_quantidade = int(input('Qual a quantidade de produtos que deseja adquirir?  '))
compras_valor = float(input('Qual é o valor unitário desse produto?  '))
total = compras_quantidade * compras_valor
desconto = 0

if (total > 0 and total < 2500):
   total_desconto = total - desconto
   print(f'O valor total da sua compra foi: R${total:.2f}') #tive que pesquisar a questão de numeros apos virgula, dai aproveitei e usei aqui pra deixar mais bonitinho
   print(f'O valor da compra com desconto é: R${total_desconto:.2f}')
   print(f'O valor de desconto foi: R${desconto:.2f}') #achei valido colocar o valor do desconto total também, apenas aparencia não muda nada no codigo
elif (total >= 2500 and total < 6000):
   desconto = total * 0.04 #vi que exista outra forma para fazer porcentagens mais achei a multiplicação por decimal a forma mais simples
   total_desconto = total - desconto
   print(f'O valor total da sua compra foi: R${total:.2f}')
   print(f'O valor da compra com desconto é: R${total_desconto:.2f}')
   print(f'O valor de desconto foi: R${desconto:.2f}')
elif (total >= 6000 and total < 10000):
   desconto = total * 0.07
   total_desconto = total - desconto
   print(f'O valor total da sua compra foi: R${total:.2f}')
   print(f'O valor da compra com desconto é: R${total_desconto:.2f}')
   print(f'O valor de desconto foi: R${desconto:.2f}')
elif (total >= 11000):
   desconto = total * 0.11
   total_desconto = total - desconto
   print(f'O valor total da sua compra foi: R${total:.2f}')
   print(f'O valor da compra com desconto é: R${total_desconto:.2f}')
   print(f'O valor de desconto foi: R${desconto:.2f}')
else:
   print('Quantidades negativas não são permitidas, por favor tente novamente.')