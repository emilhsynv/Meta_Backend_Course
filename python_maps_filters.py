menu = ["espresso", "mocha", "capuchino", "cortado", "americano"]

def find_cofee(cofee):
    if cofee[0] == "c":
        return cofee

# Uncomment to see how map() function works:
map_cofee = map(find_cofee, menu)
print(map_cofee)
for x in map_cofee:
    print(x)

# Uncomment to see how filter() function works:

#filter_coffee = filter(find_cofee, menu)
#print(filter_coffee)
#for x in filter_coffee:
    #print(x)