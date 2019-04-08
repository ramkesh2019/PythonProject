# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:07:13 2019

@author: ramkesh sahani
"""
###########################
#fabonacci series
n=10
n1=0
n2=1
count=0
while count < n:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
       
    #################################   
# sum of all even number for a given range
n=int(input('Enter a value: '))
sum=0
for i in range(1,n):
    if i%2==0:
     sum=sum+i
print('Sume of all even number is',sum)


#################################

# sum of all odd number for a given number
n=int(input('Enter a number'))
for i in range(1,n):
    if i%2!=0:
     sum=sum+i
print(sum)

#####################################

# check prime nuber
n=int(input('Enter a value: '))
if n>0:
    for i in range(2,n):
        if n%i==0:
            print('it is not prime number')
            break
    else:
        print('it is prime number')
else:
    print('it is not prime number')
    

    
   ############################################

# find factorial for given input
x=int(input('enter a number:' ))
f=1
for i in range(1,x+1):
    f=f*i
    print(f)
  ################################  
    
    # find factorial for given input
x=int(input('enter a number:' ))
f=1
for i in range(1,x+1):
    f=f*i
print(f)

#############################################
# try with 1634 as it is armstrong number
# and try with other sequence as well
n=input()
len=len(n)
k=int(n)
rem=0
arm=0
while k>0:
    rem=int(k%10)
    arm=arm+(rem**len)
    k=int(k/10)
if arm==int(n):
    print("armstrong "+str(n))
else:
    print("num is not armstrong")

        