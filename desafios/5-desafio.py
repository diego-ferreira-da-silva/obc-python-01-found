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

"""
Abaixo a resolução criada pelo Professor
def check_char(text):
    type={"Uppercase":0, "Lowercase":0}
    for char in text:
        if char.isupper():
           type["Uppercase"]+=1
        elif char.islower():
           type["Lowercase"]+=1
    print ("Texto original: ", text)
    print ("Número de letras maiúsculas: ", type["Uppercase"])
    print ("Número de letras minúsculas: ", type["Lowercase"])

#string_test('The quick Brown Fox')
check_char("A melhor forma de prever o futuro é Criá-Lo")

"""

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

"""
Abaixo a resolução criada pelo professor

def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd
print(check_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""