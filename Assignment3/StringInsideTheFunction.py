
#Write a Python program to reverse a string

def reverse(string):
    reversed_string = ''
    for i in string:
        reversed_string = i + reversed_string
    print(reversed_string)

string = input('enter the string : ')
reverse(string)