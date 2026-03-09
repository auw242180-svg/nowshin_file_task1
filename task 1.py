# Part A
with open("student info.txt", "w") as file:

file.write("C20\n")
file.write("C21\n")
file.write("C22\n")

file.close()


# Part B
with open ("student info.txt", "a") as file:

file.write("C23\n")
file.write("C24\n")
file.write("C25\n")
file.write("C26\n")

file.close()


# Part C
with open("student info.txt", "r") as file:

for line in file:
    print(line.rstrip())   

file.close()
