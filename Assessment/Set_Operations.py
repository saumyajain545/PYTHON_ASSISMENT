# Program for set operations

set1 = set(map(int, input("Enter elements of set1: ").split()))
set2 = set(map(int, input("Enter elements of set2: ").split()))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Symmetric Difference:", set1 ^ set2)
print("Subset:", set1.issubset(set2))

#output
#Union: {1, 2, 3, 4, 5}
#Intersection: {3}
#Symmetric Difference: {1, 2, 4, 5}
#Subset: False
