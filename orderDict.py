from collections import OrderedDict

"""
OrderedDict from the collections module is a dictionary subclass
that remembers insertion order of keys
"""
people = OrderedDict(Accra="McLean", Kumasi="Akua",Tarkoradi="Makiki")

print(people)
"""
OrderedDict has no append method
"""
#add an item to the dictionary
# OrderedDict doesnot use the append method to add an item
people['NY'] = 'Rosa'

print(people)

print(people.keys())

print(people.values())

"""
Return the Values from the people dictionary
"""
for person in people.values():
    print(person)

for place in people.keys():
    print(place)

# get the key as place and value as person
for place, person in people.items():
    print(f"{person} lives at {place}")

# get a value based on the key
print(people.get('NY'))
# overrides the value of NY with the new value
people['NY'] = "Rakiki"
print(people)