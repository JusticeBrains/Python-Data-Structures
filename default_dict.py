from collections import  defaultdict

"""
Returns default values of missing keys

"""

# create a dictionary of list class
pet = defaultdict(list)

print(pet)

pet['dogs'].append('Roller')
pet['dogs'].append('Messi')
pet['dogs'].append('Ricky')
pet['cats'].append('Deni')
pet['cats'].append('Resh')

print(pet)

print(pet['dogs'])
print(pet['cats'])

print(pet['dogs'])
print(pet['cows'])