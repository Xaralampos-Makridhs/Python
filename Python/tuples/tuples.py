#create a tuple

mytuple1=(1,2,3,4,5)

mytuple2=1,2,3,4,5 # without ()

#single element tuple 
mytuple3=(5,) #single element tuple

mytuple4=(1,2,3,4)
mytuple4[1]=4 #This cause TypeError error.The tuple elements cannot change

mytuple5=(3,1,2)
print(mytuple5[0]) #prints the first element

#mixed tuple
mixed_tuple=(1,"hello",3.14,[1,3,4],(1,4,5))

#nested tuples
nested_tuples=((1,3),(4,2),(5,7))
print(nested_tuples[0]) #printsd 1,3

#index
mytuple6=(3,1,2)
print(mytuple5[2]) #prints the last element

#negative index
my_tuple=(1,2,3,4)
print(my_tuple[-1]) #prints the last element (4)

#slicing
mytuple7=(1,2,3,4,5)
print(mytuple7[1:4]) #prints (2,3,4) [start:end-1]

#count
mytuple8=(1,2,3,4,5,6)
print(mytuple8.count(2)) #prints 1 because there is one 1 in our tuple

#index
mytuple9=(1,2,3,4,5)
print(mytuple9.index(3)) #prints 2 becaouse 3 is in the third place in the tuple(we start from 0)

#compares with in
mytuple10 = (1, 2, 3)
print(2 in my_tuple)  #prints True
print((1, 2) == (1, 2))  #prints True
