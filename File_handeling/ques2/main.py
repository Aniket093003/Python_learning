f1 = "a.txt"
f2 = "b.txt"
f3 = "c.txt"

with open(f1, "w") as f:
    f.write("10")
with open(f1 , 'r') as f:
    f1_data = int(f.read())
print("file 1 created")

with open(f2, "w") as f:
    f.write("5")
with open(f2 , 'r') as f:
    f2_data = int(f.read())

print("file 2 created")



with open(f3, "w") as f:
    f.write(str(f1_data + f2_data))

print("file 3 created")


