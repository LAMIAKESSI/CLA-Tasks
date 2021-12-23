# 1 Create a list that contains all the even numbers between 1 and 299
EvenNumbers = [n for n in range(1,300) if n % 2 == 0]
print(EvenNumbers)
    
# 2 Iterate through the previously created list and print first the length of the list then all the squared values of the list
print(" The list length is :", len(EvenNumbers))
for i in EvenNumbers:
    print("The squared value of ", i, "is : ", i**2)

# 3 check if 57 is in the list using one line 
if (57 in EvenNumbers): print("57 exists in the list")
else: print("57 does not exist in the list")
