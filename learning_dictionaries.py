# {"key": "value"}

pets = {"dog": "mudge", "fish": "bingo"}

print(pets)

print(f"My fish's name is {pets['fish']}.")


pets.update({"fish": "beta"})

print(pets)

pets.update({"cat": "garfield"})

print(pets)

pets["lizard"] = "sid"

print(pets)

pets["dog"] = "henry"

print(pets)

del pets["cat"]

print(pets)

print(pets.keys())

for pet in pets.keys():
    print(pet)
    print(f"The {pet}'s name is {pets[pet]}")

print(pets.values())

print(pets.items())

for k, v in pets.items():
    print(f"The {k}'s name is {v}")


# Not gonna work well
dogs = {"name": "henry", "age": 7, "name": "mudge", "age": 4}
print(dogs)


# "Multiple" values
cats = {"names": ["garfield", "max", "steve"], "ages": [3, 7, 2]}
for ind, cat in enumerate(cats["names"]):
    print(cat)
    print(cats["ages"][ind])


lizards = [{"name": "sid", "age": 9}, {"name": "lizzy", "age": 2}]
for liz in lizards:
    print(liz["name"], liz["age"])
















