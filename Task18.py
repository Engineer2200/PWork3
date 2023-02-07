N = int(input("Введите длину массива: "))
L = [ int(input()) for i in range(N) ] 
print (L) 

X = int(input("Введите число: "))
closest_number_up = 10001
closest_number_down = -10001

for i in range(N):
    if L[i] > X and L[i] < closest_number_up:
        closest_number_up = L[i]
    elif L[i] < X and L[i] > closest_number_down:
        closest_number_down = L[i]

if X - closest_number_down > closest_number_up - X or X - closest_number_down == closest_number_up - X:
    print(closest_number_up)
else:
    print(closest_number_down)