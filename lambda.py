people = [
    {"name": "chris", "house": "Gryffindor"},
    {"name": "Fred", "house": "Ravenclaw"},
    {"name": "Bill", "house": "Slythrin"}
]

def f(person):
    return person["name"]

#people.sort(key=f)

people.sort(key=lambda person: person["name"])
print(people)