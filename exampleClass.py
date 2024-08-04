
class ExampleClass:

    mylist = []

    def GetListSize(self):
        return len(self.mylist)

    def AddToList(self, val):
        self.mylist.append(val)

    def GetValueAtIndex(self, index):
        return self.mylist[index]


#######
# test the ExampleClass

exCls = ExampleClass()

print("list size:", exCls.GetListSize())
exCls.AddToList("val1")
exCls.AddToList("val2")
exCls.AddToList("val3")
print("list size:", exCls.GetListSize())
print("val at index 0", exCls.GetValueAtIndex(0))
print("val at index 0", exCls.GetValueAtIndex(1))