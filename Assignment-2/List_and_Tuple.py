'''
 Write a Python program to get a list, sorted in increasing order by the last element in 
 each tuple from a given list of non-empty tuples
'''
tuple=[(4,4),(3,2),(2,1),(1,3)]
print(tuple)
for i in range(0,len(tuple)):
    for j in range (0,len(tuple)-1):
        if(tuple[j][-1]>tuple[j+1][-1]):
            temp=tuple[j+1]
            tuple[j+1]=tuple[j]
            tuple[j]=temp
print("Answer \n",tuple)

