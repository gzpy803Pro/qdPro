class A():
    def hi(self):
        print('---A hi---')
        # super().hi()

class B(A):
    def hi(self):
        print('---B hi----')
        super().hi()

class C():
    def hi(self):
        print('---C hi---')
        super().hi()

class D(C, B):
    def hi(self):
        print('---D hi-----')
        super().hi()

d = D()
# d.hi()
# print(D.mro())
if hasattr(d, 'hi'):
   hi = getattr(d, 'hi') 
   hi()
