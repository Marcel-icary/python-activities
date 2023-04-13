votos = {}
dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

for dia in dias:
    votos[dia] = int(input(f"Informe a quantidade de votos para {dia}: "))

dia_vencedor = ""
maior_voto = 0

for dia, voto in votos.items():
    if voto > maior_voto:
        dia_vencedor = dia
        maior_voto = voto

print(f"O dia escolhido foi {dia_vencedor}, com {maior_voto} votos.")
