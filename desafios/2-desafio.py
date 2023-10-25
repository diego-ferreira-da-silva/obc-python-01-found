# Desafio 1 - Substituindo caractere repetido
# Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere
# Ex:
# fifa 23 → **fi#a 23**
# restart→ resta#t
jogo = input("Digite o nome do jogo:\n")
char = jogo[0].lower()
novo_jogo = jogo.replace(char, "$")
novo_jogo = char + novo_jogo[1:]
print(novo_jogo)


# Desafio 2 - Substituindo caractere repetido
# Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.
# Ex:
# abc xyz → **xyc abz**

nome = 'ABC'
nome2 = 'XYZ'

novo_nome = nome[:2]
novo_nome2 = nome2[:2]

nome = nome.replace("AB", novo_nome2)
nome2 = nome2.replace("XY", novo_nome)

print(nome)
print(nome2)

