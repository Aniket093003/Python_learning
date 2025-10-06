# # # print numbers from 1 to 100

# # x = 1 
# # while x <= 100 :
# #     print(x)
# #     x += 1
# # print("x")
# # # print even numbers from 100 to 1

# # y = 100
# # while y >= 1 :
# #     print(y)
# #     y -= 1

# # # print the multiplication table of a number

# # num = int(input("Enter a number: ")) 
# # i = 1
# # while i <= 10 :
# #     print(num, "*", i, "=", num*i)
# #     i += 1   

    
# # # print the elements using while loop 1,4,9,16,25,36,49,64,81,100   
# # """a = 1 
# # while a <= 10 :
# #     print(a * a)
# #     a += 1
# # """
# # a = [1,4,9,16,25,36,49,64,81,100]
# # inx = 0
# # while inx < len(a) :
# #     print(a[inx])
# #     inx += 1    


# # # search an element in a list using while loop
# # x = int(input("Enter a number to search: "))
# # found = False
# # index = 0
# # while index < len(a):
# #     if a[index] == x:
# #         found = True
# #         break
# #     index += 1
# # if found:
# #     print(f"{x} is found in the list at index {index}.")    
# #

# ##########
# sum of positive numbers
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# sum_num = 0
# for x in numbers:
#     if x > 0:
#         sum_num += x
#         x +=1

# print("sun of positive numbers",sum_num)

# pve_no = 0

# for x in numbers:
#     if x > 0 :
#         pve_no += 1 
#         x +=1

# print("total positive numbers",pve_no)
# ###############3

# calculate the sun of even numbers up to a given number n

# n = 20
# sum_of_even_numbers = 0
# for i in range(n+1):
#     if i % 2 == 0:
#         sum_of_even_numbers += i

# print(sum_of_even_numbers)

#################
#################
# print the multipliction table for a given number upto 10 but skip the fifith iteration
# n = 3
# for i in range(1,11):
#     if i == 5 :
#         continue
#     print(n*i)

#################
#reverse a string using for loop

# str = "Aniket"
# rev_str = ""
# for i in str:
#     rev_str = i + rev_str

# print(rev_str)


# find the first non repeated chracter in a given string 

# ste = "aahil"
# for i in ste:
#     if ste.count(i) == 1:
#         print("non-repeated character:", i)
#         break

##############3333
#compute the factorial of the number using while loop

# num = 5  
# factorial = 1
# while num > 0:
#     factorial *= num
#     num -= 1

# print(factorial)    

##########################
# keep asking the user for input until they enter a number between 1 to 10



# while True :
#     inp = int(input("Enter a number :"))
#     if inp >= 1 and inp <= 10:
#         print("valid")
#         break

################### table dynamically
# num = int(input("enter a number"))

# for i in range(1,11):
#     print(f"{num} multiplies by {i} =", num*i)



############### reverse a string usiong loop 

# str = "Aniket"
# reversed_str = ""
# for char in str:
#     reversed_str = char + reversed_str
# print(reversed_str)


# num = 5  
# factorial = 1
# while num > 0:
#     factorial *= num
#     num -= 1
# print(factorial)

# check number is a prime number or not
# num = int(input("Enter a number: "))
# is_prime = True 

# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             is_prime = False
#             break

# print(is_prime)

#  Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]
# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print("duplicate item found:", item)
#         break
#     unique_item.add(item)

#1. Write a Python program to count the number of vowels in a given string.

# str = "aniket"
# # vov = ["a", "e" , "o", "i", "u"]
# for i in str:
#     vov = "aeiou"
#     count_vov = 0 
#     if i == vov:
#         count_vov += 1
#     print(count_vov)

#  Write a Python program to count the number of digits in a given number.





# x = "helloeh"

# occursence = 0 

# for i in x:
#     if i == "h":
#         occursence += 1


# print("occurennce of h" ,occursence)
   
#  Write a Python program that takes a list of strings and converts each string to uppercase.

# lst = ["annkad", "ada", "akdase"]
# for i in lst:
#     print(i.upper())    

# Write a Python program to count positive and negative numbers in a list.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]       
# positive_count = 0
# negative_count = 0          
# for num in numbers:
#     if num > 0:
#         positive_count += 1
#     elif num < 0:
#         negative_count += 1     
# print("Positive numbers:", positive_count)
# print("Negative numbers:", negative_count)
    

# Write a Python program to remove duplicates from a list using a for loop.

# items = [1, 2, 2, 3, 4, 4, 5]
# unique_items = [] 
# for item in items:
#     if item not in unique_items:
#         unique_items.append(item)

# print(unique_items)

# inp = input("enter your message :")
# vovels = "aeiou"
# count_vov = 0
# for i in inp:
#     if i in vovels:
#         count_vov += 1

# print(count_vov)        
        



# x = "hello1234"
# num = "0123456789"
# count = 0 
# for i in x:
#     if i.isdigit():
#         count +=1

# print(count)   
# 
num_lst = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
new_lst = []
for i in num_lst:
    if (i % 2 ) == 0:
        temp = int(str(i) * i)
        new_lst.append(temp)
        temp = ""
    else:
        new_lst.append(i)

print(new_lst)
