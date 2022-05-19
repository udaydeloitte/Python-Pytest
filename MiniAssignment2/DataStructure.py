from collections import Counter
# Return all the duplicate value list of arraylist s from
# Input:
arrlist= [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]

for i in arrlist:
    d=Counter(i)    #d=dict to count occurance of each ele.
    for j in d:
        if d[j]>1:
            print(j,"-->",d[j], end=" ")
    print()

print("-----------------------------------------------------")

#Given I / P

list1 = ["Hello ", "take "]

list2 = ["Dear", "Sir"]

#o/p=['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
ans=[]
for i in list1:
    for j in list2:
        ans.append(i+" "+j)
print(ans)

print("------------------------------------------------------")

#  Given a nested list extend it by adding the sub list["h", "i", "j"]in such a way that it will look like the following list

# Given List:
givenlist = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

subList =["h", "i", "j"]

# Expected output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
givenlist[2][1][2].extend(subList)

print(givenlist)

print("-------------------------------------------------------")

# Map the dictionary in the following manner

key = ["Ten","Twenty","Thirty"]

value = [10,20,30]

output_dict={}
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
for i in range(len(key)):
    output_dict[key[i]]=value[i]

print(output_dict)
#Using Zip Method
print(dict(zip(key,value)))

print("--------------------------------------------------------")

# Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#USING UPDATE METHOD
dict1.update(dict2)
print(dict1)

#Algorithmic Way
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
for i in dict2:
    if i not in dict1:
        dict1[i]=dict2[i]

print(dict1)
print("------------------------------------------------------------")

#Rename key city to location in the following dictionary

sampleDict = {

  "name": "Kelly",

  "age":25,

  "salary": 8000,

  "city": "New york"

}
sampleDict["location"]=sampleDict["city"]

del sampleDict["city"]
print(sampleDict)
print("--------------------------------------------------------------")

# Convert Dictionary to list
# The original dictionary is : {‘HuEx: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4, 5]}
# The converted list is : [[‘HuEx, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]
original_dict={'Huex':[1,3,4],'is':[7,6],'best':[4,5]}
converted_list=[]
for i in original_dict:
    temp=[i,original_dict[i]]
    converted_list.append(temp)
print(converted_list)