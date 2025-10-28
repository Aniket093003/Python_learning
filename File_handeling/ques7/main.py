filename = "Data.txt"
def main():
    with open(filename, 'a') as f:
        employ_count = 0
        while True:
            employ_ID = input("enter employ ID: ")
            if employ_ID == "":
                break
            employ_name = input("enter employ name: ")
            employ_salary = input(f"enter {employ_name} salary: ")

            f.write(f"{employ_ID}, {employ_name}, {employ_salary}\n")
            employ_count += 1
            print("sucessfully added data of employ")
            print(f"total employs: {employ_count}")

def emp_with_high_salary(filename , threshold=50000):
    print(f"\n Employs with salary above {threshold}")

    with open(filename , 'r') as f:
        for line in f:
            parts = line.strip().split(",")
            # print(parts)
            name = parts[1]
            salary = int(parts[2])

            if salary > threshold:
                print(f"{name}: {salary}")




if __name__ == "__main__":
    main()
    emp_with_high_salary("Data.txt", 50000)