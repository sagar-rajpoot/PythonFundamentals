Friends=["sagar","sandeep","Munnu"]

for a in Friends:
    print(a)

#nested list
mylist = [
    [1,2,3],
    [4,5,6],
    [7,8]
]

print(mylist[0])
print(mylist[0][1])

for a in mylist:
    for b in a:
        print(b)

mylist=[1,2,3,4]
print(mylist)
mylist.append(5)
print(mylist)

# You can enter anything at any index - Rest will pushed to next indexes 
mylist.insert(0,'python')
print(mylist)

# Similarly You can delete also 
del mylist[0]
print(mylist)

#I want get data from list Starting from index 1 till last and each time want to move 2 steps at a time
print(mylist[0::2])
