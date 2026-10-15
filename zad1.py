suma = 0
for i in range(2, 101, 2):
    suma += i
print(f"Suma: {suma}")

sumak = 0
for i in range(1, 101):
    sumak += i*i
print(f"Suma kwadratów: {sumak}")

sumap = 0
for i in range(1, 64):
    sumap += 2**i
print(f"Suma potęg 2: {sumap}")