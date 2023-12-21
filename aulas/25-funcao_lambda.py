# Função de potencia de números
power = lambda num: num**2

#Função verifica Par
pair = lambda x: x % 2 == 0

#divite número por outro 
divNum = lambda x, y : x / y

#Inverte número por string
reverse = lambda s: s[::-1]

print(power(5))
print(power(9))
print(pair(4))
print(pair(3))
print(divNum(10, 2))
print(divNum(10, 3))
print(reverse("Python"))
print(reverse("Javascript"))