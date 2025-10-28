


with open("test.txt", 'w') as f:
    f.write("""
This is the first line of the file.
The file is being read sequentially, one line at a time.
Python's file object supports iteration, making this process very clean and memory-efficient.
This is the final line.
""")

with open("test.txt", 'r') as f:
    line_number = 1
    for line in f:
        print(f"line {line_number}: {line.strip()}")
        line_number += 1