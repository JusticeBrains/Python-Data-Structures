from collections import  ChainMap

"""
ChainMap groups multiple dictionaries into a single mappings
"""

pets = {"dogs":2,"cats":4}
towns = {"NY":800, "Accra":200}
chain = ChainMap(pets, towns)

print(chain)
print(chain["dogs"])