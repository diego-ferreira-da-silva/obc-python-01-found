## Conta letras maiúsculas e minúsculas
#Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

def contLetter(frase):
  maiuscula = 0
  minuscula = 0
  
  for letra in frase:
    if letra.isalpha():
      if letra.isupper():
        maiuscula += 1
      else:
        letra.islower()
        minuscula += 1

  print(f"A frase: {frase} tem essa quantidade de letras maiúsculas e minúsculas\nMaiúsculas: {maiuscula} \nMinúsculas: {minuscula}")

contLetter("Teste de Frase")

## Lista números pares e ímpares de uma lista
#Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.

def parImpar(listaNumeros):
  
  par = []
  impar = []
  
  for num in listaNumeros:
    if num % 2 == 0:
      par.append(num)
    else:
      impar.append(num)
  
  print(f"Separação de números ímpares e pares da lista: {listaNumeros} \nPares: {par} \nImpares: {impar}")
  
parImpar([2, 3, 4, 5])