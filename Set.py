myset={4,"abc",4,"bcd",5.6}
print(myset);

# Set vs List 
# Set will eliminate duplicates and It is Unordered so cant apply index based Operations 
# so myset[0] Does not make sense but we can add things there
# so Mutable and Unordered and does not accept Duplicates.

for x in myset:
    print (x)


myset.add("aws")
print(myset);