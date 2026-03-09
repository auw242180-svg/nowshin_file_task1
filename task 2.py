with open ("students.csv", "r") as file:

l = file.readlines()

for line in l:  
    i=line.strip().split(",")
    name=i[0]
    sec=i[1]
    age=i[2]

    

    print(f"{name}  is in section {sec} , her age is {age} age")

file.close()
