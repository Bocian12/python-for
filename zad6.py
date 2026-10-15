print("Podaj wysokość trójkąta:",end=' ')
wys = int(input())
spaces = wys - 1 #ilosc spacji
for i in range(1, wys*2+1, 2):
    print(spaces*" ",i*"*")
    spaces -= 1