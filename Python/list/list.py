#create a simple list
mylist=[1,2,3,4,5,6,7,8,9,10]
print(mylist)


#create a mixed list  [int,string,double,boolean]
mixedlist=[1,"apple",3.14,True]
print(mixedlist)

#acces to a list item
print(mylist[0]) #prints 1
print(mylist[2]) #prints 3

print(mylist[-1]) #prints the last item in list (4)

#change an item in the list
mylist[3]=25
print(mylist)

#add an item in the list
mylist.append(23) #in the end
print(mylist)

#insert an item
mylist.insert(2,15) # insert(index,value), index 2 => third place
print(mylist)

#remove an item from list
mylist.remove(2) #removes the first 2 
print(mylist)

mylist.pop(2) #removes the item from index 2
print(mylist)

#if you use pop without parametre removes the last item
mylist.pop()

#combine lists
list1=[1,2,3,4]
list2=[4,6,7,8]

combined=list1+list2
print(combined)

#copy a list
copiedlist=mylist.copy()
print(copiedlist)
#or copiedlist=mylist[:]

#reverse list

mylist.reverse()
print(mylist)
#or mylist[::-1]

#length
print(len(mylist))

#access
for item in mylist:
    print(item)


#slicing

#list[start:end-1]
print(mylist[1:4])
print(mylist[:3])
print(mylist[3:])
print(mylist[:])
#negative indexes prints reverese the list

#list methods

#SORT
mylist.sort()
print(mylist) #sorting in ascending order

mylist.sort(reverse=True)
print(mylist) #sorting in descendig order

#COUNT
count_10=mylist.count(10)
print(count_10)#counts how many 10 list has

#INDEX 
index_of_10=mylist.index(10) #prints the index from the first 10
print(index_of_10)

#CLEAR 
mylist.clear()
print(mylist) #prints []





