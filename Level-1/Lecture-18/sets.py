# ages = {10,10,11,12,1,34}
# """
# 1. set dont hold duplicate values 
# 2. set also doesnt follow any order 
# 3. you cannot use indexes with the sets 
# """
# print(ages[0])

# ex {"mango","pear","kiwi",}
akshaya = {"mango", "strawberries", "apples", "pomogranete", "pineapples"}
vinuja = {"pomogranete" , "dragonfruit", "strawberries", "papaya", "bananas"}
aryan = {"mango", "watermelon", "strawberries", "oranges", "apples"}

# 1. unqiue fruits among all of them (union)
# print(akshaya.union(vinuja,aryan))

# 2. find the common fav fruit (intersection)
# print(akshaya.intersection(vinuja,aryan))
# print(akshaya.intersection(aryan))

# set difference A-B means all the items from A except for elements from B 
# print(akshaya.difference(vinuja))

# print(akshaya.symmetric_difference(aryan))

# A is subset of B i.e, All the elements in a are part of B but not all the elements of B are part of A 
body = {"eyes","ears","mouth","nose","tongue","legs","hands"}
head = {"eyes","ears","mouth","nose","tongue"}
# print(head.issubset(body))
# print(body.issuperset(head))
print(head.isdisjoint(body))