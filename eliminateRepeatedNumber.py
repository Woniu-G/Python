#This is a small program talking about 3 ways to eliminate the repeated number in a list
#One way to solve this problem is through creating a new list
def eli(l):
    s=[]
    for i in l:
        if i not in s:
            s.append(i)
    print(s)
list1 = [1,2,3,4,5,6,5,4,3,2,1,0]
# eli(list1)#result list is [1, 2, 3, 4, 5, 6, 0]
#
# #another way to think about it is making it a set
# s=set(list1)#converting to set would automaticly eliminate duplicate and order it as well
# listS=list(s)#we do want a list, so convert set back to list
# print(listS)#result list [0, 1, 2, 3, 4, 5, 6]

#last way is kind of tricky, becasue dictionary alone is defining with a key and value
d=dict.fromkeys(list1)
print(d)
#by converting it dictionary,we altomatic eliminated repeated key
print(list(dict.fromkeys(list1)))#and converback give us what we want
