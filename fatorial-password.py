minuto = int(input("entre com o minuto: "))

total = 1

if (int(minuto) >= 0 and int(minuto <= 59)):
    for n in range(int(minuto),0,-1):
        total = total*n
    print("liberdade"+str(total))
else:
    print("entre com um minuto valido")