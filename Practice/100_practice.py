# Take two numbers as input and print their sum.

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# print("sum of numbers: ",a+b)

# Swap two variables without using a third variable.

# a = 20
# b = 30

# a = a + b 
# b = a - b
# a = a - b

# print(a, b)

# Check if a number is even or odd.

# num = int(input("enter a numbar: "))
# print("number is even") if num%2 == 0 else print("number is odd")

# Find the largest of three numbers.

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# num3 = int(input("enter third number: "))

# if num1 >= num2 and num1 >= num3:
#     print("num1 is greater")
# elif num2 >= num1 and num2 >= num3:
#     print("num2 is greater")
# else:
#     print("num3 is greater") 

# Check if a given year is a leap year.

# a = int(input("enter year : "))

# if a%4 == 0 and a%100 !=0 or a%400 == 0:
#     print(a,"is a leap year")
# else:
#     print(a, "is not a leap year")

# Reverse a string without using slicing.
# str = "aniket"

# rev =  "" .join(reversed(str))
# print(rev)

# Count vowels and consonants in a string.

# str = str(input("enter a string :"))
# vov = "aeiouAEIOU"
# count_vov = 0
# count_consonants = 0
# for i in str:
#     if i in vov:
#         count_vov += 1
#     else:
#         count_consonants += 1

# print("conosants :",count_consonants, "vovels :",count_vov)
        
# Find the factorial of a number using a loop.

# from math import factorial


# num = int(input("enter a number :"))
# factorial = 1
# while num >= 1:
#     factorial *= num
#     num -= 1

# print(factorial)
    
# Print the Fibonacci sequence up to n terms.
# n = 5 
# finonacci = [0 , 1]

# for i in range(2 , n):
#     next_fib = finonacci[-1] + finonacci[-2]
#     finonacci.append(next_fib)

# print(finonacci)

# Check if a string is a palindrome.

# string = str(input("enter your string: "))

# rev_str = ''.join(reversed(string))

# print("plaindrom") if string == rev_str else print("not a plaindrom")

# Count the number of digits in a number.

# x = 2345
# print(len(str(x)))
# Calculate the sum of digits of a number.

# num = int(input("enter a number :"))
# sum_of_digits = 0
# for i in str(num):
#     sum_of_digits += int(i)

# print(sum_of_digits)

# Convert Celsius to Fahrenheit and vice versa.

# def cel_to_far(temp):
#     far_temp = (float(temp) * 1.8) + 32
#     print(far_temp)
# def far_to_cel(temp):
#     cel_temp = (temp - 32) * 0.5556
#     print(cel_temp)
# temperature = int(input("enter temperature :"))
# def main():
#     while True:
#         print("\n Temperature conversion")
#         print("1. Faranhite to celcius ")
#         print("2. celcius to faranhite")
        

#         choice = (input("Enter your choice: "))
        
#         if choice == "1":
#             cel_to_far(40)
#         elif choice == "2":
#             far_to_cel(50)
       
#         else:
#             print(" Invalid input, please try again.")


# if __name__ == "__main__":
#     main()

# Find the ASCII value of a character.

# print(ord("A"))

# Print all prime numbers between 1 and 100.

# prime_numbers = []
# for i in range (10 , 100):
#     if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0:
#         prime_numbers.append(i)
        

# print(prime_numbers)


# Check if a number is an Armstrong number.

# num = int(input("enter a number :"))
# res_num = 0
# for i in str(num):
    
#     res_num += int(i)**3
# if num == res_num:
#     print(f"{num} is a armstrong number")
# else:
#     print(f"{num} is not a armstrong number")

# Find the maximum and minimum elements in a list.

# lst = [ 2, 4, 4, 6, 9]

# max_element = max(lst)
# min_element = min(lst)

# print(max_element)
# print(min_element)
# Remove duplicates from a list without using set().

# lst = [2,3,4,5,4,6]
# new_lst = []

# for i in lst:
#     if i not in new_lst:
#         new_lst.append(i)
# print(new_lst)

# Sort a list without using the sort() function.

# lst = [2,1,324,54,7]
# new_lst = []

# for i in range(1, len(lst)):
#     ele = lst[i]
#     j = i - 1 
#     while j >= 0 and ele < lst[j]:
#         lst[j + 1] = lst[j]
#         j -= 1
#     lst[j + 1] = ele

# print(lst)
# Remove duplicates from a list without using set().

# lst = [2,1,324,54,7,2,324]

# for i in lst:
#     if lst.count(i) > 1:
#         lst.remove(i)

# print(lst)



