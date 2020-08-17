import pprint

pets = {"cats": [{"name": "garfield",  "age": 7, "colors": ["orange", "brown"]}, {"name": "snowball", "age": 2, "colors": ["white"]}]}

# garfield is orange and brown
print(f'{pets["cats"][0]["name"]} is {pets["cats"][0]["colors"][0]} and {pets["cats"][0]["colors"][1]}.')

pprint.pprint(pets)
