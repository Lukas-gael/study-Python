print("Seja bem vindo ao quarto exercicio de Lucas Gabriel Moreira dos Santos")

lista_livro = []
id_global = 0


def cadastrar_livro(id):
  while(True):
   global id_global
   id_global += 1
   id = id_global
   nome_livro = input('Digite o nome do livro por gentileza:  ')
   autor_livro = input('Digite o nome do autor por gentileza:  ')
   editora_livro = (input('Digite a editora do livro por gentileza:  '))
   dicionario = {'Nome': nome_livro, 'Id': id, 'Autor': autor_livro, 'Editora': editora_livro}
   lista_livro.append(dicionario)

   confirmacao = input('Deseja cadastrar mais um livro?(s/n)  ')
   if (confirmacao == 's'):
      continue
   elif (confirmacao == 'n'):
      break

#teste cadastrar_livro(id)
#teste print(lista_livro[1])

def consultar_livro():
   while(True):
    print('Como desejas consultar?')
    print('Para ver todos digite 1')
    print('Para consultar por nome digite 2')
    print('Para consultar por id digite 3')
    print('Para consultar por autor digite 4')
    print('Para consultar por editora digite 5')
    print('Para sair digite 0')
    confirmacao = int(input())
    if (confirmacao == 1):
      for livro in lista_livro:
        print(livro)

    elif (confirmacao == 2):
      nome_livro = input('Digite o nome do livro que deseja consultar:  ')
      for livro in lista_livro:
        if (livro['Nome'] == nome_livro):
          print(livro)

    elif (confirmacao == 3):
      id_livro = int(input('Digite o id do livro que deseja consultar:  '))
      for livro in lista_livro:
        if (livro['Id'] == id_livro):
          print(livro)

    elif (confirmacao == 4):
      autor_livro = input('Digite o nome do autor que deseja consultar:  ')
      for livro in lista_livro:
        if (livro['Autor'] == autor_livro):
          print(livro)

    elif (confirmacao == 5):
      editora_livro = input('Digite o nome da editora que deseja consultar:  ')
      for livro in lista_livro:
        if (livro['Editora'] == editora_livro):
          print(livro)

    elif (confirmacao == 0):
      break
    else:
      print('Opção invalida, tente novamente.')
      continue

#teste consultar_livro()

#teste cadastrar_livro(id)
#teste consultar_livro()

def remover_livro():
  remover  = int(input('Digite o id do livro que deseja remover:  '))
  for livro in lista_livro:
    if (livro['Id'] == remover):
      lista_livro.remove(livro)
      print('Livro removido com sucesso.')

#teste cadastrar_livro(id)
#teste consultar_livro()
#teste remover_livro()
#teste consultar_livro()

while(True):
  print('Bem vindo ao sistema de gerenciamento de livros')
  print('Escolha uma das opções: ')
  print('Para cadastrar livro digite 1')
  print('Para consultar livro digite 2')
  print('Para remover livro digite 3')
  print('Para sair digite 4')
  escolha = int(input())
  if (escolha == 1):
    cadastrar_livro(id)
  elif (escolha == 2):
    consultar_livro()
  elif (escolha == 3):
    remover_livro()
  elif (escolha == 4):
    break
  else:
    print('Opção invalida, tente novamente.')
    continue