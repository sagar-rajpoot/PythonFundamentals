data={'apple':30,'mango':20,'banana':50}
print(data);

# it will print all Keys
for x in data:
    print(x);

# for keys only 
for x in data.keys():
    print(x);

# for Values only
for x in data.values():
    print(x);

print(data['apple']);

data['apple']=245;
print(data['apple']);


emp = {'name':'sagar singh', 'skills':['aws','terraform','spark','python']}

for x in emp:
    print(x);

for y in emp.values():
    for z in y:
        print(z);

