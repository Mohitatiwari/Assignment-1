#Q.1  Write a program to find all pairs of an integer array whose sum is equal to a given number? 
def pairedElements(arr, sum):
   
    low = 0
    high = len(arr) - 1
 
    while (low < high):
        if (arr[low] +
            arr[high] == sum):
            print("The pair is : (", arr[low],
                  ", ", arr[high], ")")
        if (arr[low] + arr[high] > sum):
            high -= 1
        else:
            low += 1
 # Driver code
if __name__ == '__main__':
   
    arr = [2, 3, 4, -2,
           6, 8, 9, 11]
    arr.sort()
    pairedElements(arr, 6)
    

#Q.3 Write a program to check if two strings are a rotation of each other?

str1 = "abcde";  
str2 = "deabc";  
   
if(len(str1) != len(str2)):  
    print("Second string is not a rotation of first string");  
else:  
    str1 = str1 + str1;   
    if(str1.index(str2)):  
        print("Second string is a rotation of first string");  
    else:  
        print("Second string is not a rotation of first string"); 


#Q.4 Write a program to print the first non-repeated character from a string?

string = "readforlearn"
index = -1
fnc = ""
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
     print("First non-repeating character is", fnc)


# Q.8 Write a program to check if all the brackets are closed in a given code snippet.

def isbalanced(s):
    c= 0
    ans=False
    for i in s:
        if i == "(":
            c += 1
        elif i == ")":
            c-= 1
        if c < 0:
            return ans
        if c==0:
            return not ans
    return ans
s="()"
print("Given string is balanced :",isbalanced(s))



#Q.9 Write a program to reverse a stack.
class  Stack_to_reverse  :
    def __init__(  self  ):
        self.items  =  list()
        self.size=-1
 
    def  isEmpty(  self  ):
        if(self.size==-1):
            return True
        else:
            return False
 
    def  pop(  self  ):
        if  self.isEmpty():
            print("Stack is empty")
        else:
            return self.items.pop()
            self.size-=1
 
    def  push(  self,  item  ):
        self.items.append(item)
        self.size+=1
 
    def reverse(self,string):
        n = len(string)
 
        for i in range(0,n):
            S.push(string[i])
 
        string=""
  
        for i in range(0,n):
            string+=S.pop()
        return string
 
S=Stack_to_reverse()
seq=input("Enter a string to be reversed")
sequence = S.reverse(seq)
print("Reversed string is " + sequence)



#Q.10 Write a program to find the smallest number using a stack.

list1 = [17, 53, 46, 8, 71]
 
list1.sort ()
print ("The smallest number in the given list is ", list1[0])
