# Write a Python Program to print half pyramid using alphabets. 

rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print("\n")


# Write a Python Program to print full pyramid using '*' symbol.

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")


# Take a number as input from the user. Print the number in reversed order.

num = int(input("Enter a Number: "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))


# Given an array of integers, find the length of the longest sub-sequence such that elements in the 
# subsequence are consecutive integers,the consecutive numbers can be in any order

def findLongestConseqSubseq(arr, n):
 
    ans = 0
    count = 0

    arr.sort()
    v = []
    v.append(arr[0])
 
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            v.append(arr[i])
 
    for i in range(len(v)):
        if (i > 0 and v[i] == v[i - 1] + 1):
            count += 1
        else:
            count = 1
        ans = max(ans, count)
 
    return ans
 
arr = [1, 2, 2, 3]
n = len(arr)
 
print("Length of the Longest contiguous subsequence is",
      findLongestConseqSubseq(arr, n))
 
