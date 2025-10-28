with open("abc.txt", "w") as f:
    f.write("""Python is a programming language
            It is easy to use""")
    
with open("abc.txt", 'r') as f:
    word_to_find = input("enter the word: ")
    for line_number, line in enumerate(f , 1):
        print("2")
        if word_to_find in str(line):
            print("3")
            print(f"found on line {line_number}: {line.strip()}")
