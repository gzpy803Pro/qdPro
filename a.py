class A():
    def __init__(self, num):
       self.num = num

    def __gt__(self, value):
       if isinstance(value, A):
          return self.num > value.num

       return self.num > value



a = A(300)

if a > 100:
   print('ok')

a2 = A(1000)

if a > a2:
   print('very good!')
else:
   print('^_^')
