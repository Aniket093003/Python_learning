f1 = "abc.txt"
f2 = "xyz.txt"
with open(f1, "w") as f:
    f.write("python is a programing language and a easy language")

with open (f1, "r") as f:
    file_data = f.read()
# print(file_data)

with open(f2, "w") as f:
    f.write(file_data)

print("sucessfull")

f.close()
