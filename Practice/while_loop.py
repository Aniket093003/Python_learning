# print numbers from 1 to 100

x = 1 
while x <= 100 :
    print(x)
    x += 1
print("x")
# print even numbers from 100 to 1

y = 100
while y >= 1 :
    print(y)
    y -= 1

# print the multiplication table of a number

num = int(input("Enter a number: ")) 
i = 1
while i <= 10 :
    print(num, "*", i, "=", num*i)
    i += 1   

    
# print the elements using while loop 1,4,9,16,25,36,49,64,81,100   
"""a = 1 
while a <= 10 :
    print(a * a)
    a += 1
"""
a = [1,4,9,16,25,36,49,64,81,100]
inx = 0
while inx < len(a) :
    print(a[inx])
    inx += 1    


# search an element in a list using while loop
x = int(input("Enter a number to search: "))
found = False
index = 0
while index < len(a):
    if a[index] == x:
        found = True
        break
    index += 1
if found:
    print(f"{x} is found in the list at index {index}.")    