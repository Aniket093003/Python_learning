filename = "text.txt"
vov_count = 0
consonants_count = 0
digit_count = 0
spl_char_count = 0

with open(filename, 'r') as f:
    file = f.read()
    print(file)
    for i in file:
        if i in "aeiouAEIOU":
            vov_count +=1
        else:
            consonants_count += 1
        if i in "1234567890":
            digit_count += 1
        if i in "!@#$%^&*":
            spl_char_count += 1

print(vov_count, consonants_count , digit_count, spl_char_count)