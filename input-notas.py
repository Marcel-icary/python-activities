notas_impares = []
notas_pares = []

for i in range(1, 51, 2):
        print("você esta digitando as notas dos alunos impares.")
        nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {i}: "))
        notas_impares.append(nota)

for e in range(2, 51, 2):
        print("vocÊ esta digitando as notas dos alunos pares.")
        nota = float(input(f"POR FAVOR, insira a nota do aluno de numero {e}: "))
        notas_pares.append(nota)

media_impares = sum(notas_impares) / len(notas_impares)
media_pares = sum(notas_pares) / len(notas_pares)

if media_impares > media_pares:
    print("A metade ímpar teve a maior nota.")
elif media_pares > media_impares:
    print("A metade par teve a maior nota.")
else:
    print("As duas metades tiveram a mesma nota média.")
