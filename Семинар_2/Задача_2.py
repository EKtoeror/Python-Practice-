# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
n = int(input("Введите число: "))

s1=0 #Первое число Фибаначи 
s2=1 #Второе число Фибаначи

m=2 #Предполагаемый номер числа

while n>s2:
    s1=s1+s2
    s2=s1+s2
    m+=2
    #print(s1,s2,m)
if n==s2:
    print(m)
elif n==s1:
    print(m-1)
else:
    print(-1)

# c, d = 0,1
# m=2
# while d<n:
#     c,d=d,c+d надо прописывать одной строкой иначе не работает
#     m+=1
# if d==n:
#     print(m)
# else: print(-1)