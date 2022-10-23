
'''
Write a Python program to print a dictionary whose keys should be the 
 alphabet from a-z and the value should be corresponding ASCII values
'''

dict={}
x=ord('a')
for i in range(x,x+26):
    dict[chr(i)]=i
print(dict)
