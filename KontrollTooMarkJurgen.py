#V1
#Task1

num = int(input("Kirjutage number 1 kuni 9: "))

try:
    if num < 1 or num > 9:
        print("Number peab olla ainult 1 kuni 9")
    else:
        for l in range(4):
            i = 0
            while i < num: 
                if l == 0:
                    print("    /V\\    ", end=" ")  
                elif l == 1:
                    print("   / V \\   ", end=" ")  
                elif l == 2:
                    print("  / V V \\  ", end=" ")  
                elif l == 3:
                    print(" /VV V VV\\ ", end=" ")  
                i += 1
            print()  
except ValueError:
    print("Ainult numbrid 1 kuni 9")

#Task2
R = int(input("Kirjuta number R: "))
try:
    if R < 0:
        print("Peab olla mitte - ")
    else:
        result = 1
        for num in range(1, R +1, 2):
            result *= num
        print(f"Kõikide paaritute arvude korrutise tulemus 1 kuni {R}: {result}")
except ValueError:
    print("Vale kirjuta tais number")
    

#Task3
import random

N = random.randint(1, 20)
print(f"Genereritud number {N}")
positive = 0
for i in range(N):
    num = random.randint(-100, 100)
    print(f"Genereritud numbr: {num}")
    if num > 0:
        positive += 1
print(f"Number of positive numbers: {positive}")



#Task4
num = int(input("Kirjuta naturalne number: "))
try:
     if num < 0:
         print("Vale, kirjutage naturalne number")
     else:
         chet = 0
         nechet = 0
         for i in str(num):
             if int(i) % 2 == 0:
                 chet += 1
             else:
                 nechet += 1
         print(f"Isegi numbrid {chet}")
         print(f"Paaritud numbrid: {nechet}")
except ValueError:
     print("Vale, kirjutage ainult numbrid")


#Task5
A = int(input("Number A: "))
B = int(input("Number B: "))
try:
    if A > B:
        print("Vale; A peab olla vaiksem kui B voi sellega vordne")
    else:
        suma = 0
        for num in range(A, B +1):
            suma += num
        print(f"Arvude summa alates {A} kuni {B}: {suma}")
except ValueError:
    print("Vale, sisetage A ja B taisarvud")



    
