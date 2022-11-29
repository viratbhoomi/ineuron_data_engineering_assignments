# -*- coding: utf-8 -*-
"""Programming Assignment_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kqUoMAiWDJOATmGK1FXy_6VOIJ-Vgl9R

# Programming Basic Assignment 6

------------
### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
"""

def fibo(a,b,c):
    if c > 0:
        c -= 1
        print(a, end=' ')
        temp = b
        b = a + b
        a = temp
        fibo(a,b,c)

fibo(0,1,10)

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))

"""-------------------
### 2. Write a Python Program to Find Factorial of Number Using Recursion?
"""

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

fact(5)

fact(7)

def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return (n*factorial(n-1))
factorial(5)

"""-------------
### 3. Write a Python Program to calculate your Body Mass Index?
"""

def bmi(height, weight):
    
    return weight/(height*height)

bmi(1.8, 70)

def bmi(height, weight):
    
    return weight/pow(height,2)
bmi(1.8,70)

"""--------------
### 4. Write a Python Program to calculate the natural logarithm of any number?
"""

import math

try:
    num = int(input("Enter the number: "))
except Exception as e:
    print(e)
else:
    print(math.log(num))

import math
def logarithamic(n):
  return math.log(n)
logarithamic(14)

"""------------
### 5. Write a Python Program for cube sum of first n natural numbers?

"""

def cubN(n):
    return sum(range(n+1))**3

cubN(3)

cubN(4)

def cube_sum(n):
  return sum([i for i in range(n+1)])**3
cube_sum(3)



