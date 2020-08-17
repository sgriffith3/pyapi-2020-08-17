# Shopping List
#
# Milk
# Eggs
# Bread
# Bacon
# Cheese


shopping_list = ['milk', 'eggs', 'bread', 'bacon', 'cheese']
# Indexes          0       1        2        3        4
# Reversed        -5      -4       -3       -2       -1

print(shopping_list)

print(type(shopping_list))

# Example f-string
print(f"The shopping list includes the items: {shopping_list}")

print(f"The first item of the list is: {shopping_list[0]}")

print(f"The second through fourth items of the list are: {shopping_list[1:4]}")

print(f"The items from index 2 on (of the list) are: {shopping_list[2:]}")

print(f"Every other item in the list are: {shopping_list[::2]}")

print(f"Every other item in the list starting at eggs are: {shopping_list[1::2]}")

print(f"The last item of the list is: {shopping_list[-1]}")

print(f"I want to eat some: {shopping_list[-2:-5:-2]}")

print(f"I want to eat some: {shopping_list[3:0:-2]}")


more_stuff = ['trash bags', 'ziplocs', 'crayons']

shopping_list.append(more_stuff)

print(shopping_list)

# ['milk', 'eggs', 'bread', 'bacon', 'cheese', ['trash bags', 'ziplocs', 'crayons']]

# Outer List
#   0        1       2         3        4                      5
# Inner List
#                                                    0           1           2
#                                                  [5][0]       [5][1]     [5][2]

print(f"Sam needs some more {shopping_list[5][2]}") 

for item in shopping_list:
    if isinstance(item, list):
        for inner in item:
            print(inner)
    else:
       print(item)


even_more = ['dog food', 'bone', 'yoga mat']

shopping_list.extend(even_more)

print(shopping_list)

