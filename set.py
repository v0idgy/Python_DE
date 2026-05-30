# # a = [10,20,30,40,50]
# # list_set = set(a) ## Converting list to set
# # print(list_set) 


# ch_set = set("hello world") ## Converting string to set
# # # print(ch_set)

# # # for val in ch_set:
# # #     print(val)
# # print(type(ch_set))

# ch_set = list(ch_set) ## Converting set to list
# print(type(ch_set))
# for id in range(len(ch_set)):
#     print(ch_set[id], end = " ")


# num_set = {1,2,3,4,5}
# for value, char in enumerate(num_set):
#     print(char, end = " ")  



# a = set()

# # print(a)

# a.add("Gourav") ## Adding element to set
# a.add("Gourav") ## Adding duplicate element to set
# # print(a)

# a.update(["Saurabh", "Satyarth", "Gourav"]) ## Adding multiple element to set
# print(a)


# b = set([0,1,2,3,4,5])
# print(b)
# b.pop() ## Removing random element from set
# print(b)


# b.discard(2) ## Removing specific element from set, if element is not present it will not raise error
# print(b)
# b.remove(2) ## Removing specific element from set, if elements is not present it will raise error
# print(b)

# set1 = {1,2,3,4,5}
# set2 = {1,2,3,4,5,6,7,8}

# print(set1.issubset(set2)) ## Check if set1 is subset of set2
# print(set2.issubset(set1)) ## Check if set2 is subset of set1 


set1 = {1,2,3}
set2 = {3,4,5}

print(set1 | set2) ## Union of set1 and set2
print(set1 & set2) ## Intersection of set1 and set2
print(set1 - set2) ## Difference of set1 and set2


