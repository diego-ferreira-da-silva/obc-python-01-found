## Contagem Regressiva
# Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”. 
import winsound
cronometro = 10
for cont in range (10, -1, -1):
  print (cont)
  if cont == 0:
    print(winsound.Beep(2500, 500))

## Tabuada
# Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário

number = int(input('Tabuada de: \n'))
begin = int(input("De: \n"))
end = int(input("Até: \n"))

x = begin
while x <= end:
  print(f"Tabuada de {number} x {x} = {number * x}")
  x += 1