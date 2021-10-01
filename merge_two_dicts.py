d1 = {'James': 25, 'Roland': 27, 'Daniel': 19}
d2 = {'Paul': 45, 'Flex': 39, 'William': 39, 'James': 46}

# using dict unpacking approach
d3 = {**d1, **d2}
print(d3)

# using the union operator
d4 = d1 | d2 
print(d4)

# updates d1 with d2 using the update operator (|=)
# works like the concatenation +=
d1 |= d2

print(d1)

