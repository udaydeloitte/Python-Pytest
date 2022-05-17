from itertools import permutations
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

obj_strcls=StrCls("1234")
print("Length of String: ",obj_strcls.length())
print("Converted into list of chars: ",obj_strcls.convert())

class Pairpossible(StrCls):
    def allpairs(self):
        perm=permutations(self.inp_string)
        outputperm=[]
        for i in perm:
            outputperm.append(i)
        return outputperm
obj_pair=Pairpossible("987")
print(obj_pair.allpairs())
