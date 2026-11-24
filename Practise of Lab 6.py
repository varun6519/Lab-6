'''
print("          Addition Table")

# Print column headings
for i in range(1, 10):
    print(i, end="  ")

print()
print("      " + "-" * 37)

# Print addition table
for i in range(1, 10):
    print(i, "|", end="  ")

    for j in range(1, 10):
        print(i + j, end="  ")

    print()
'''
'''
N=int(input())
for i in range(1,1001):
    if i%N==0:
        if i%4==0:
            continue
        print(i,end=" ")
'''
'''
#3.a
N=int(input())
for i in range(N):
    for j in range(i+1):
        print(j+1,end=" ")
        
    print()
'''
"""
#3.b
N=int(input())
for i in range(N,0,-1):
    print("* "*i, end=" ")
    print()
"""
'''
#3.c
N=int(input())
i=1
while i<=N:
    j=1
    while j<=N-i:
        print(" ", end=" ")
        j+=1
    j=1
    while j<=i:
        print("*", end=" ")
        j+=1
    print()
    i=i+1
'''

'''
N=int(input())
original=N
octal=""
while N>0:
      a=N%8
      N=N//8
      octal=str(a)+octal
print(octal)

if octal==oct(original)[2:]:
    print("Yes it is matching ")
else:
    print("No.matching")
'''
'''
N=int(input())
first=0
second=0                      #we take initiall value firsst and second
                              # and then it restore value of first and second
for i in range(1,N+1):
    D=int(input())
    if D>first:
        second=first
        first=D
    elif D<first:
        if D>second:
            second=D
    i=i+1
print("first is :", first)
print("second is :", second)
'''
'''
N=int(input())
sum=0
digits=len(str(N))


while N>0:
    a=N%10
    N=N//10
    sum=sum+a**digits
    
    if sum==N:
      print("No. is Armstrong No.",sum)
'''
'''
n = int(input("Enter the value of N: "))

for num in range(1, n + 1):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

if total == num:
    print(num)
'''
'''
print("N ","N*2 ","N**3 ","N*0.5 ")
for i in range(1,16):
    
    print(i," ",i**2," ",i**3," ",i**0.5,end=" ")
    print()
'''    
'''
N=int(input())

for i in range(1,N+1):
    for j in range(N,i,-1):
        print(" ",end="")
    for j in range(i):
        print(i,end=" ")
        
    print()
'''
'''
N=int(input())
num=1
for i in range(1,N+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()
'''

'''
N=int(input())
for i in range(1,N+1,2):
    for j in range(N//2-i//2):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
for i in range(N-2,0,-2):
    for j in range(N//2-i//2):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
'''   













