# x = [1,2,3]
# y = [4,5,6]
# print(x+y)

# for i in x : print(i**2)

# a = "   123   "
# print(a.strip())

# x = set(x)

# print(max(x))

# for i in range(1,21,1):
#     print(i)

# def even_check(x):
#     if x%2 == 0 :
#         print("number is even")

# even_check(4)
# a = 10
# b ='20'
# print(a+b)
# import math
# print(math.square(5))

# inp = "python"
# output = ""
# for i in inp:
#     output = i + output
# print(output)

# str = "aniket"
# count = 0


# vov = "AEIOUaeiou"
# for i in str:
#     for j in vov:
#         if i == j:
#             count += 1

# print(count)\


# print(max(lst))
# remove_duplicates(lst)




# def check_anagrams(str1,str2):
#     try1 = []
#     try2 = []
#     for i in str1:
#         try1.append(i)
#     for j in str2:
#         try2.append(j)
#     if sorted(try1) == sorted(try2):
#         print("anagram,")
#     else:
#         print("not an anagram")

# check_anagrams("listen", "silent")


# def second_largest_number(n):
#     largest = float()
#     second_largest = float()

#     for num in n:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif largest > num > second_largest:
#             second_largest = num
#     print(second_largest)
# lst = [1,2,3,4,5]
# second_largest_number(lst)



# def remove_duplicates(n):
#     seen = []
#     result = []
#     frequency = []
#     for item in n:

#         if item not in seen:
#             seen.append(item)
#             result.append(item)
#     for i in result:
#         count = n.count(i)
#         frequency.append(count)

#     output = dict(zip(result,frequency))
#     print(frequency)
#     print(result)
#     print(output)


# lst = [1,2,4,2,1,8,4]
# remove_duplicates(lst)




