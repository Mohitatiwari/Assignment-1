'''
Q.You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string.

For example: given list = ['great','hello','hiyo','abc'] so your output_dictionary should be ['great', 'abc', 'hello','hiyo']

Input Format:

At first-line it will have an integer (number of elements inside a list). In the second line, it will have a string.

Output Format:

A single line containing a sorted list.
'''


list1 = [1,2,3,4,5]
list2 = ["Hi","Hello","Great","Hiyo","abc"]

print("Original key list is : " + str(list1))
print("Orignal value list is : " + str(list2))

x = {}
for key in list1:
    for value in list2:
        x[key]=value
        list2.remove(value)
        break
print("Resultant dictionary is :" + str(x))


















'''
def convert(list):
    res_dict={lst[i]:lst[i+1] for i in range(0,len(lst),2)}
    return res_dict

lst = [1,2,3,4,5]
lst = ["Hi","Hello","Great","Hiyo","abc"]
'''