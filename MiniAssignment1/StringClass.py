from itertools import combinations
from collections import Counter

#String Class

class StrCls:
    def __init__(self,inp_string):
        self.inp_string=inp_string

    def length(self):
        return len(self.inp_string)

    def convert(self):
        outputlist=[]
        for i in self.inp_string:
            outputlist.append(i)
        return outputlist

#obj of string class
inputofstrclass=input("Enter String in number(0-9) format for string class: ")
obj_strcls=StrCls(inputofstrclass)

print("Length of String: ",obj_strcls.length())

print("Converted into list of chars: ",obj_strcls.convert())
print("----------------------------------------")
#pair possible class inherited string cls

class Pairpossible(StrCls):
    def __init__(self, inpString):

        self.inpstring=inpString

    def allpairs(self):
        comb=combinations(self.inpstring,2)

        outputcomb=[]

        for i in comb:
            outputcomb.append("".join(i))

        return list(set(outputcomb))
inputforpairclass=input("Enter string for pairpossible class in 0-9 format: ")
obj_pair=Pairpossible(inputforpairclass)

print("All Possible Pairs are: ",obj_pair.allpairs())

print("----------------------------------------")
class SearchCommonElements(Pairpossible):

    def __init__(self,inpstr1,inpstr2):

        self.inpstr1=inpstr1
        self.inpstr2=inpstr2

    def search(self):
        d=dict(Counter(self.inpstr1))

        ans=[]

        for i in set(self.inpstr2):
            if i in d:
                ans.append(i)

        return ans

print("String of StringClass is: ",obj_strcls.inp_string)

print("String of PairpossibleClass is: ",obj_pair.inpstring)

obj_SearchCommonEle = SearchCommonElements(obj_strcls.inp_string, obj_pair.inpstring)

print("Common Ele are: ",obj_SearchCommonEle.search())
print("----------------------------------------")
#EqualSumPairClass

class EqualSumPair(Pairpossible):

    def __init__(self,txt):
        self.txt=txt

    def equalsum(self):
        d={}

        for i in self.txt:
            cal=int(i[0])+int(i[1])
            if cal not in d:
                d[cal]=[i]
            else:
                d[cal].append(i)
            count=0
            for i in d:
                if len(d[i])==1:
                    count+=1

        return count

#object for euqalsumpaircls

obj_equalsum= EqualSumPair(obj_pair.allpairs())

print("Total Count of pairs whose sum are unique is: ",obj_equalsum.equalsum())

