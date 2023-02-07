N = int(input("Введите длину массива: "))
L = [ int(input()) for i in range(N) ] 
print (L) 

X = int(input("Введите число: "))
count = 0
for i in range(N):
    if L[i] == X:
        count += 1
print(count)