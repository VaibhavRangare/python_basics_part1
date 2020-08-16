"""
Tuple
Unordered
Indexed
Mutable
Duplicates allowed
"""
items = {
    "name": "Castor Troy",
    "age": "38",
    "movie": "Face Off"
}
print(items)
for name in items:
    print(name)
    print(items[name])

heros = {
    "hero1":{
        "name": "Castor Troy",
        "age": "38",
        "movie": "Face Off"
    },
    "hero2":{
        "name": "Sean Archer",
        "age": "38",
        "movie": "Face Off"
    }
}

print("name:"+ items["name"]) 

for name in heros:
    print(heros[name])
    print(heros[name]["name"])

print(heros.keys())
print(heros.items())

    