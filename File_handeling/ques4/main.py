with open("test.txt", 'w') as f:
    f.write("""This is the first line of the file.
The file is being read sequentially, one line at a time.
Python's file object supports iteration, making this process very clean and memory-efficient.
This is the final line.
""")
    
with open("test.txt", 'r') as f:
    n = int(input("enter number of lines you want to print:"))
    line_number = 1
    for line in f:
        if line_number > n:
            break
        print(f"Line {line_number}: {line.strip()}") 
        line_number += 1

    

