list_ints = [0,1,4,5]
print(list_ints)

print(list_ints[2])

print(list_ints[-2])

print(len(list_ints))

empty_list = []

nest_list = [[1,2,3],[2],[3,5,6]]
print(len(nest_list))
print(len(nest_list[1]))

name_list = ["Brandon","Carter","Scott","Cayden"]
for names in name_list:
    print(names)

i=0
while i < len(name_list):
    print(name_list[i])
    i+=1

i=0
for i in range(len(name_list)):
    print(name_list[i])
   
old_list = [0,3,5,6]
list_additions = [0,3]

old_list += list_additions

old_list = 5 * [3]

print(old_list[1:3])
