import names
import string, os

# 1 read all the file concent in one variable
file = open("./student_names.txt")
students = file.read()
print(students)
file.close()

# 2 Write a list of random names to your file

for i in range(10):
    name = names.get_full_name()
    students = students + '\n' +name
file = open(".\student_names.txt","w")
file.write(students)
file.close()

# 3 Print the first n lines of the file

n = int(input(" Type the number of the first lines : "))
file = open("./student_names.txt")
for i in range(n):
    line = file.readline()
    print(line)
file.close()

# 4 Print the last n lines of the file
n = int(input(" Type the number of the last lines : "))
file = open("./student_names.txt")
lines = file.readlines()
last_lines = lines[-n:]
for i in last_lines:
    print(i)
file.close()
    
# 5 Check if the name x is in the file
x = input(" Entre the name you want to chack : ")
file = open("./student_names.txt")
students = file.readlines()
exist = False
for i in students:
    if (x == (i.strip())):
        exist = True
        print('The name exists in the file')
        break
if (exist == False):
    print('The name does not exist in the file')  
        
# 6 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
# if not os.path.exists("./unit1/homeworks/CLA_text_files"):
#    os.makedirs("./unit1/homeworks/CLA_text_files")
# for letter in string.ascii_uppercase:
#    with open("./unit1/homeworks/CLA_text_files/" + letter + ".txt", "w") as f:
#        f.writelines(letter)


