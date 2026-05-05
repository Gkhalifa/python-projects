shopping_list = []
for x in range(1,6):
    item = input("what item would you like to add to the shopping list? ")
    shopping_list.append(item)
print("Your shopping list: ")
for x in range(0,5):
    print(f"{x+1}. {shopping_list[x]}")
