#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Print the First 10 natural numbers

i = 0 

while i < 10:
    i = i + 1
    print (i)


# In[4]:


#2. Calculate the sum of all numbers from 1 to a given number

Num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

print(sum(Num))


# In[5]:


#3. Write a program to print a multiplication table of a given number

Num = 2 
for i in range(1, 12):
    
    print(Num, 'x', i, '=', Num * i) 


# In[6]:


#4. Display numbers from a list using loop

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numbers in A:
    print (A)


# In[7]:


#5. Count the total number of digits in a number

A = [2, 3, 5.8, 7, 9.0, 4, 50]
print (len(A))


# In[8]:


#6. Write a program to display all prime numbers within a range

lower = 1
upper = 20
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




