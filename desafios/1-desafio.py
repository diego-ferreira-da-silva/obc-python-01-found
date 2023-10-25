#Antecessor e Sucessor

valor = int(input("Digite um valor para descobrir seu sucessor e seu antecessor: "))
sucessor = valor + 1
antecessor = valor - 1

print(f"O Sucessor do {valor} é: {sucessor}")
print(f"O Antecessor do {valor} é: {antecessor}")
print("------------------")

print("CALCULANDO MÉDIA DE 4 NOTAS:")
nota1 = int(input("Digite a Primeira nota: "))
nota2 = int(input("Digite a Segunda nota: "))
nota3 = int(input("Digite a Terceira nota: "))
nota4 = int(input("Digite a Última nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4
print(f"A média das 4 notas é {media}")