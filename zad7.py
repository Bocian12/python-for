import math

print("Podaj ilość liczb naturalnych:",end=' ')
n = int(input())
liczby = []
for i in range(1, n+1):
    print(f"Podaj liczbę a{i}:", end=' ')
    a = float(input())
    liczby.append(a)
suma_dodawania = 0
suma_mnozenia = 1
suma_pierwiastkow = 0
suma = 0
for i in range(0, n):
    suma_dodawania += liczby[i]
for i in range(0, n):
    suma_mnozenia *= liczby[i]
for i in range(0, n):
    suma_pierwiastkow += math.sqrt(abs(liczby[i]))
for i in range(0, n):
    if i%2 != 0:
        suma -= liczby[i]
    else:
        suma += liczby[i]

print(f"a) {suma_dodawania}")
print(f"b) {suma_mnozenia}")
print(f"c) {suma_pierwiastkow}")
print(f"d) {suma}")