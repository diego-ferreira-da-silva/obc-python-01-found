#Fatorial de um númeor

def fatorial(num):
  if num == 1:
    return num
  else:
    return(num * fatorial(num -1))
  
number = int(input("Digite um número para o fatorial: \n"))
print(f"O Fatorial de {number} é: {fatorial(number)}")

#Soma total de um número
#ex: 4 > 4 + 3 + 2 + 1
def total_sum(num):
  if num == 1:
    return num
  else:
    return(num + total_sum(num - 1))

num = int(input("Digite um número para soma \n"))
print(f"A Soma total do {num} é: {total_sum(num)}")

