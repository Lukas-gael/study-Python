print("Seja bem vindo ao segundo exercicio de Lucas Gabriel Moreira dos Santos")

acai = 11        #preferi usar variaveis fixas para facilitar e deixar um padrão afinal o aumento de preço é igual para ambos os produtos
cupuacu = 9
tamanho_p = 0
tamanho_m = 5
tamanho_g = 9
total = 0

print('Bem vindo a nossa loja de gelados') #seguindo o exemplo que estava no docx pensei em colocar os produtos e valores discrimanados antes das seleções
print('Temos o delicioso açaí nos tamanho P(R$11), M(R$16) e G(R$20),')
print('E também temos cupuaçu também nos tamanho P(R$9), M(R$14) e G(R$18).')



while (True):
   sabor = input('Digite o sabor desejado, AC para açaí ou CP para cupuaçu:  ')
   if (sabor == 'AC'):
      sabor = acai
      tamanho = input('Digite o tamanho desejado, P, M ou G:  ')
      if (tamanho == 'P'):
         pedido = acai + tamanho_p
         total += pedido
         confirmacao = input('Deseja realizar mais um pedido?(S/N)  ')
         if (confirmacao == 'S'):
            continue
         else:
            break
      elif (tamanho == 'M'):
         pedido = acai + tamanho_m
         total += pedido
         confirmacao = input('Deseja realizar mais um pedido?(S/N)  ')
         if (confirmacao == 'S'):
            continue
         else:
            break
      elif (tamanho == 'G'):
         pedido = acai + tamanho_g
         total += pedido
         confirmacao = input('Deseja realizar mais um pedido?(S/N)  ')
         if (confirmacao == 'S'):
            continue
         else:
            break
      else:
         print('Tamanho inválido selecionado, por favor tente novamente.')
         continue
   elif (sabor == 'CP'):
      sabor = cupuacu
      tamanho = input('Digite o tamanho desejado, P, M ou G:  ')
      if (tamanho == 'P'):
         pedido = cupuacu + tamanho_p
         total += pedido
         confirmacao = input('Deseja realizar mais um pedido?(S/N)  ')
         if (confirmacao == 'S'):
            continue
         else:
            break
      elif (tamanho == 'M'):
         pedido = cupuacu + tamanho_m
         total += pedido
         confirmacao = input('Deseja realizar mais um pedido?(S/N)  ')
         if (confirmacao == 'S'):
            continue
         else:
            break
      elif (tamanho == 'G'):
         pedido = cupuacu + tamanho_g
         total += pedido
         confirmacao = input('Deseja realizar mais um pedido?(S/N)  ')
         if (confirmacao == 'S'):
            continue
         else:
            break
      else:
         print('Tamanho inválido selecionado, por favor tente novamente.')
         continue
   else:
      print('Sabor inválido, por favor tente novamente.')
      print('')
      continue
print(f'O total do seu pedido foi R${total}, muito obrigado e volte sempre.')