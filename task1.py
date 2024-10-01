userfruits = int(input("How is your favourite fruit: "))
listfruits = []

for i in range(userfruits):
    fruits = input("enter fruit: ")
    listfruits.append(fruits)

    if fruits == "apple":
       print("HAPPY EATING!")
    elif fruits == "banana":
           break

print(listfruits)