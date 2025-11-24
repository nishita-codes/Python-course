# list ek ordered collection hoti hai jisme aap multiple items store kar sakte ho

# SYNTAX
# my_list = [item1, item2, item3, ...]


marks = [3,5,7, "harry" , True]

print(marks)
print(marks[0])  # first item
print(marks[2])  # third item   
print(marks[-1]) # last item
print(marks[-3]) # third last item--------> print(marks[len(marks)-3])

# OPERATIONS
# 1.append----> add item at the end of the list
marks.append(9)

# 2. insert----> add item at specific index
marks.insert(1, "nishita")

# 3. remove----> remove specific item
marks.remove(7)

# 4. pop----> remove item at specific index
marks.pop(2)

# 5. sort----> sort the list (only works if all items are of same type)
num_list = [5,2,9,1,7]
num_list.sort()

# 6. reverse----> reverse the list
num_list.reverse()  

# 7. len----> get the number of items in the list
length = len(marks) 



