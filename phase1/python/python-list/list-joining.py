l1 = [1,2,3,4]
l2 = [4,5,6,7]

list1 = [*l1 , *l2] #by unpacking operator
print(list1) 

list2 = [items for sublist in [l1, l2] for items in sublist]
print("New list: ",list2)
