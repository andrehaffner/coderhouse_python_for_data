
print("Welcome to the fill list program!\n")
myList = list()

n = 0
while n < 5:
    print(myList)
    item = input("Add item: ")
    myList.append(item)
    n += 1
print("\n", myList)
print("\nProgram ended.")
