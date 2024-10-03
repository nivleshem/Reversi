
class ExampleClass:

    def __init__(self):
        counter = 45
        jjj = 67
        self.sum = counter


    def foo(self):
        print(self.jjj)




#######
# test the ExampleClass

#exCls = ExampleClass()
#exCls.foo()

def foo(v1):
    v1.append(4)
    v1.append(5)
    v1.append(6)
    print(v1)

v1 = [1, 2, 3]

print("Before foo() v1", v1)
foo(v1.copy())
print("After foo() v1", v1)


