numero1 = float(input("Digite o primeiro número\n"))
numero2 = float(input("Digite o segundo número\n"))
operation = input("Digite a operação a realizar(+ - * /)\n")

if operation == "+":
  result = numero1 + numero2
elif operation == "-":
  result = numero1 - numero2
elif operation == "*":
  result = numero1 * numero2
elif operation == "/":
  result = numero / numero2
else:
  print("Operação Inválida")
  result = 0

print(f"O resultado de {numero1} {operation} {numero2} é = {result}")