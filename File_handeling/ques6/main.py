filename = "abc.txt"


with open(filename, "a") as f:
    while True:
        name = input("enter student name: ")
        if name == "":
            print("Stopped")
            break
        marks = input(f"enter marks of {name}: ")

        f.write(f"{name},{marks}\n")
        print("Data sucessfully added") 

with open(filename, "r") as f:
    for line in f:
        parts = line.strip().split(',')
        # print(parts)
        name = parts[0]
        marks = int(parts[1])

        if marks > 80:
            print(f"{name}: {marks}")





