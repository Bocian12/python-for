print("Podaj liczbę a:",end=' ')
a = int(input())
print("Podaj liczbę b:",end=' ')
b = int(input())
suma = 0
if a%2 == 0:
    a +=1
if a>b:
    suma = 0
else:
    for i in range(a, b+1, 2):
        suma += i
print(f"Suma liczb nieparzystych: {suma}")



