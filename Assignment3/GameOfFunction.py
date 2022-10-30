

#Write a Python function to sum all the numbers in a list.

def sum(*n):         
    total=0
    for i in n:
        total=total+i
    print("The sum of elements in the list is:",total)
sum(5,4,3,1,2)