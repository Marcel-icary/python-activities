idade = input("digite sua idade")
bpm_min = input("digite a quantidade de batimentos cardíacos")

idade = int(idade)
bpm_min = int(bpm_min)

if (idade >0 and idade <=2):
    if bpm_min <120:
        print("batimentos abaixo do padrão")
    elif bpm_min >140:
        print("batimentos acima do padrão")
    else:
        print("batiments normais")
        
elif (idade >=3 and idade <=7):
    if bpm_min <120:
        print("batimentos abaixo do padrão")
    elif bpm_min >140:
        print("batimentos acima do padrão")
    else:
        print("batiments normais")

elif (idade >=8 and idade <=17):
    if bpm_min <80:
        print("batimentos abaixo do padrão")
    elif bpm_min >100:
        print("batimentos acima do padrão")
    else:
        print("batiments normais")

elif (idade >=18 and idade <=60):
    if bpm_min <70:
        print("batimentos abaixo do padrão")
    elif bpm_min >80:
        print("batimentos acima do padrão")
    else:
        print("batiments normais")