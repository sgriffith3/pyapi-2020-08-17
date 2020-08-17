# Make a list of names (3 or more)
names = ["curly", "moe", "larry"]

# - print out each name from the list
print(names[0])
print(names[1])
print(names[2])
# - using a slice, print out the last 2 names from the list ([::])
print(names[1:])
print(names[-2:])



# Make a list of car types (3 or more)
cars = ["bmw", "audi", "chevy"]

# - Append the following list to yours:
dream_cars = ["lambo", "bugatti", "bentley"]
cars.append(dream_cars)
 
# - Extend the following list into yours:
more_likely = ["ford", "toyota", "honda"]
cars.extend(more_likely)

print(cars)
# ['bmw', 'audi', 'chevy', ['lambo', 'bugatti', 'bentley'], 'ford', 'toyota', 'honda']
#    0      1       2                     3                    4       5         6
#                             0           1         2

# - print out "bentley" from your combined list
print(cars[3][2]) 

# - print out toyota from your combined list
print(cars[5])
