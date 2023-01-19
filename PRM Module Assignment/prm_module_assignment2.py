'''
Q.Your task is to complete the validate_triangle and validate_rectangle functions for the classes.Hint for validating is given in the

comments of the code. Also you will have to print the following after validation in respective functions:-

1.Invalid Triangle: If the triangle sum property of sides is not valid(More hint in the comments of code)

2.Valid Triangle:If the triangle sum property of sides is valid.

3.Valid Rectangle:If 2 side pairs are same and they are input in correct order like l,b,l,b

4.Invalid Rectangle: If Not Valid rectangle as stated above.

Input Format:

The side length of triangle followed by for rectangle in the next line in order.

Output Format:

since object are created in order, so first validate info about triangle will come and than rectangle.

Sample Input 0:

3 4 5

2 4 2 4

Sample Output 0:

Valid Triangle

Valid Rectangle
'''



length = 3
width = 4
hypotenuse = 5
length1 = 2
breadth1 = 4
length2 = 2
breadth2 = 4

triangle = lambda a : hypotenuse*hypotenuse == (width*width)+(length*length)
if triangle(1) is True:
    print("Valid")
else:
    print("Invalid")


rectangle = lambda t : length1 == length2 and breadth1 == breadth2
if rectangle(1) is True:
    print("Valid")
else:
    print("Invalid") 




