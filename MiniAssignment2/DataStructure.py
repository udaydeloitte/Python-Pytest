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


