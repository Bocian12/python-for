print("Podaj liczbę rzędów:",end=' ')
rzedy = int(input())
for i in range(1, rzedy+1):
    print(f"Podaj krzeseł w rzędzie: {i}", end=' ')
    krzesla = int(input())
    print(f"Rząd {i}: {krzesla} krzeseł")