#create set
#every set has unique items
my_set = {1, 2, 3}

#empty set
set_empty = set()

#add()
my_set.add(4)  #adds 4 to the set

#remove()
my_set.remove(2)  #removes 2 from the set; raises KeyError if the item is not in the set

#discard()
my_set.discard(3)  #removes 3, but does not raise an error if the item is not in the set

#pop()
my_set.pop()  #removes and returns a random value from the set

#clear()
my_set.clear()  #clears the set

#copy()
my_set_copy = my_set.copy()  #creates a copy of the set

set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union() or |
result = set1.union(set2)  #{1, 2, 3, 4, 5}
#or result = set1 | set2

#intersection() or &
result = set1.intersection(set2)  #{3}
#or result = set1 & set2

#difference() or -
result = set1.difference(set2)  #{1, 2}
#or result = set1 - set2

#symmetric_difference() or ^
result = set1.symmetric_difference(set2)  #{1, 2, 4, 5}
#or result = set1 ^ set2

#issubset()
result = set1.issubset(set2)  #returns True if set1 is a subset of set2

#issuperset()
result = set1.issuperset(set2)  #returns True if set1 is a superset of set2

#isdisjoint()
result = set1.isdisjoint(set2)  #returns False because they have common elements (3)